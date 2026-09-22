#!/usr/bin/env python3
"""Keep generated site URLs consistent with Quarto's canonical URLs.

Quarto generates a trailing-slash canonical for a page whose output file is
``index.html``. Its sitemap and some generated links still use the physical
filename, however. After a full render, this step removes that conflicting
signal and verifies the result. Preview and incremental renders may reuse
stale output, so they defer this whole-site check until the next full render.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit
from xml.etree import ElementTree


INDEX_FILE = "index.html"
HREF_PATTERN = re.compile(
    r"(?P<prefix>\bhref\s*=\s*)(?P<quote>['\"])(?P<url>[^'\"<>]*)(?P=quote)",
    re.IGNORECASE,
)
SITE_URL_PATTERN = re.compile(r"^\s*site-url\s*:\s*(?P<url>[^#]+?)\s*$", re.MULTILINE)


class CanonicalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canonicals: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "link":
            return

        attributes = {name.lower(): value for name, value in attrs}
        rel = (attributes.get("rel") or "").lower().split()
        href = attributes.get("href")
        if "canonical" in rel and href:
            self.canonicals.append(href)


def read_site_url(config_path: Path) -> str:
    match = SITE_URL_PATTERN.search(config_path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"No site-url found in {config_path}")

    site_url = match.group("url").strip().strip("'\"").rstrip("/")
    parsed = urlsplit(site_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid site-url in {config_path}: {site_url}")
    return site_url


def normalize_internal_url(value: str, site_url: str) -> str:
    """Replace a final index.html with the equivalent trailing slash."""

    parsed = urlsplit(value)
    canonical_site = urlsplit(site_url)

    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return value
    if parsed.netloc and parsed.netloc.lower() != canonical_site.netloc.lower():
        return value

    if parsed.path == INDEX_FILE:
        clean_path = "./"
    elif parsed.path.endswith(f"/{INDEX_FILE}"):
        clean_path = parsed.path[: -len(INDEX_FILE)]
    else:
        return value

    scheme = parsed.scheme
    netloc = parsed.netloc
    if netloc:
        scheme = canonical_site.scheme
        netloc = canonical_site.netloc

    return urlunsplit((scheme, netloc, clean_path, parsed.query, parsed.fragment))


def normalize_html_file(path: Path, site_url: str) -> int:
    source = path.read_text(encoding="utf-8")
    replacements = 0

    def replace_href(match: re.Match[str]) -> str:
        nonlocal replacements
        original = match.group("url")
        normalized = normalize_internal_url(original, site_url)
        if normalized == original:
            return match.group(0)

        replacements += 1
        quote = match.group("quote")
        return f"{match.group('prefix')}{quote}{normalized}{quote}"

    normalized_source = HREF_PATTERN.sub(replace_href, source)
    if replacements:
        path.write_text(normalized_source, encoding="utf-8")
    return replacements


def normalize_sitemap(path: Path, site_url: str) -> int:
    source = path.read_text(encoding="utf-8")
    replacements = 0
    location_pattern = re.compile(r"(?P<open><loc>)(?P<url>[^<]+)(?P<close></loc>)")

    def replace_location(match: re.Match[str]) -> str:
        nonlocal replacements
        original = match.group("url")
        normalized = normalize_internal_url(original, site_url)
        if normalized == original:
            return match.group(0)

        replacements += 1
        return f"{match.group('open')}{normalized}{match.group('close')}"

    normalized_source = location_pattern.sub(replace_location, source)
    if replacements:
        path.write_text(normalized_source, encoding="utf-8")
    return replacements


def _normalize_json_hrefs(value: object, site_url: str) -> int:
    replacements = 0
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "href" and isinstance(child, str):
                normalized = normalize_internal_url(child, site_url)
                if normalized != child:
                    value[key] = normalized
                    replacements += 1
            else:
                replacements += _normalize_json_hrefs(child, site_url)
    elif isinstance(value, list):
        for child in value:
            replacements += _normalize_json_hrefs(child, site_url)
    return replacements


def normalize_search_index(path: Path, site_url: str) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    replacements = _normalize_json_hrefs(data, site_url)
    if replacements:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return replacements


def normalize_site(output_dir: Path, site_url: str) -> dict[str, int]:
    if not output_dir.is_dir():
        raise ValueError(f"Site output directory does not exist: {output_dir}")

    counts = {
        "html_hrefs": sum(
            normalize_html_file(path, site_url)
            for path in sorted(output_dir.rglob("*.html"))
        ),
        "sitemap_urls": normalize_sitemap(output_dir / "sitemap.xml", site_url),
        "search_hrefs": normalize_search_index(output_dir / "search.json", site_url),
    }
    return counts


def sitemap_locations(path: Path) -> list[str]:
    root = ElementTree.parse(path).getroot()
    return [
        (element.text or "").strip()
        for element in root.iter()
        if element.tag.rsplit("}", 1)[-1] == "loc"
    ]


def output_file_for_url(url: str, output_dir: Path, site_url: str) -> Path | None:
    parsed = urlsplit(url)
    canonical_site = urlsplit(site_url)
    if parsed.scheme != canonical_site.scheme or parsed.netloc != canonical_site.netloc:
        return None

    site_prefix = canonical_site.path.rstrip("/")
    if site_prefix and not parsed.path.startswith(f"{site_prefix}/"):
        return None

    relative_path = parsed.path[len(site_prefix) :].lstrip("/")
    if parsed.path.endswith("/"):
        relative_path += INDEX_FILE
    return output_dir / unquote(relative_path)


def canonical_urls(path: Path) -> list[str]:
    parser = CanonicalParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.canonicals


def validate_site(output_dir: Path, site_url: str) -> list[str]:
    errors: list[str] = []
    sitemap_path = output_dir / "sitemap.xml"
    search_path = output_dir / "search.json"

    try:
        locations = sitemap_locations(sitemap_path)
    except (ElementTree.ParseError, OSError) as error:
        return [f"Cannot read {sitemap_path}: {error}"]

    for location in locations:
        if normalize_internal_url(location, site_url) != location:
            errors.append(f"Sitemap URL is not canonical: {location}")
            continue

        output_file = output_file_for_url(location, output_dir, site_url)
        if output_file is None:
            errors.append(f"Sitemap URL is outside site-url: {location}")
        elif not output_file.is_file():
            errors.append(f"Sitemap URL has no output file: {location}")
        else:
            declared = canonical_urls(output_file)
            if declared != [location]:
                errors.append(
                    f"{output_file} declares {declared or 'no canonical URL'}; "
                    f"expected {location}"
                )

    for html_path in sorted(output_dir.rglob("*.html")):
        source = html_path.read_text(encoding="utf-8")
        for match in HREF_PATTERN.finditer(source):
            href = match.group("url")
            if normalize_internal_url(href, site_url) != href:
                errors.append(f"{html_path} links to non-canonical URL: {href}")

    try:
        search_data = json.loads(search_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        errors.append(f"Cannot read {search_path}: {error}")
    else:
        pending: list[object] = [search_data]
        while pending:
            value = pending.pop()
            if isinstance(value, dict):
                href = value.get("href")
                if isinstance(href, str) and normalize_internal_url(href, site_url) != href:
                    errors.append(f"Search index links to non-canonical URL: {href}")
                pending.extend(value.values())
            elif isinstance(value, list):
                pending.extend(value)

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the generated site without modifying it",
    )
    parser.add_argument("--config", type=Path, default=Path("_quarto.yml"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site")),
    )
    parser.add_argument("--site-url", help="override website.site-url from the config")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    # Quarto sets RENDER_ALL only for a full render. Preview can render no
    # pages at startup, leaving stale pages and sitemap entries in the output.
    # Standalone invocations and explicit --check must still validate strictly.
    # https://quarto.org/docs/projects/scripts.html#pre-and-post-render
    if (
        not args.check
        and "QUARTO_PROJECT_OUTPUT_DIR" in os.environ
        and os.environ.get("QUARTO_PROJECT_RENDER_ALL") != "1"
    ):
        print("Skipping whole-site URL normalization for preview/incremental render.")
        return 0

    try:
        site_url = (args.site_url or read_site_url(args.config)).rstrip("/")
        counts = None if args.check else normalize_site(args.output_dir, site_url)
        errors = validate_site(args.output_dir, site_url)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"URL normalization failed: {error}", file=sys.stderr)
        return 1

    if errors:
        print("URL normalization validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if counts is None:
        print("Canonical URL validation passed.")
    else:
        print(
            "Normalized generated URLs "
            f"({counts['html_hrefs']} HTML links, "
            f"{counts['sitemap_urls']} sitemap entries, "
            f"{counts['search_hrefs']} search links) and validated canonicals."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
