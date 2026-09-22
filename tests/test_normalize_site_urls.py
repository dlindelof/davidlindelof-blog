from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.normalize_site_urls import (
    normalize_internal_url,
    normalize_site,
    validate_site,
)


SITE_URL = "https://blog.davidlindelof.com"


class NormalizeInternalUrlTests(unittest.TestCase):
    def test_normalizes_internal_index_pages(self) -> None:
        cases = {
            "index.html": "./",
            "./index.html#top": "./#top",
            "../../index.html": "../../",
            "/posts/example/index.html?view=full#notes": "/posts/example/?view=full#notes",
            "https://blog.davidlindelof.com/posts/example/index.html": (
                "https://blog.davidlindelof.com/posts/example/"
            ),
            "http://blog.davidlindelof.com/index.html": (
                "https://blog.davidlindelof.com/"
            ),
        }

        for original, expected in cases.items():
            with self.subTest(original=original):
                self.assertEqual(normalize_internal_url(original, SITE_URL), expected)

    def test_preserves_external_index_pages(self) -> None:
        external = "https://example.com/docs/index.html?lang=en"
        self.assertEqual(normalize_internal_url(external, SITE_URL), external)


class NormalizeSiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name)
        post_dir = self.output_dir / "posts" / "example"
        post_dir.mkdir(parents=True)

        (self.output_dir / "index.html").write_text(
            """<!doctype html><html><head>
<link rel="canonical" href="https://blog.davidlindelof.com/">
</head><body>
<a href="./posts/example/index.html">Post</a>
<a href="https://example.com/docs/index.html">External</a>
</body></html>
""",
            encoding="utf-8",
        )
        (post_dir / "index.html").write_text(
            """<!doctype html><html><head>
<link rel="canonical" href="https://blog.davidlindelof.com/posts/example/">
</head><body><a href="../../index.html">Home</a></body></html>
""",
            encoding="utf-8",
        )
        (self.output_dir / "sitemap.xml").write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://blog.davidlindelof.com/index.html</loc></url>
  <url><loc>https://blog.davidlindelof.com/posts/example/index.html</loc></url>
</urlset>
""",
            encoding="utf-8",
        )
        (self.output_dir / "search.json").write_text(
            json.dumps(
                [
                    {"href": "posts/example/index.html", "objectID": "unchanged"},
                    {"href": "posts/example/index.html#notes"},
                ]
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_normalizes_and_validates_generated_site(self) -> None:
        counts = normalize_site(self.output_dir, SITE_URL)

        self.assertEqual(counts["html_hrefs"], 2)
        self.assertEqual(counts["sitemap_urls"], 2)
        self.assertEqual(counts["search_hrefs"], 2)
        self.assertEqual(validate_site(self.output_dir, SITE_URL), [])

        homepage = (self.output_dir / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="./posts/example/"', homepage)
        self.assertIn('href="https://example.com/docs/index.html"', homepage)

        search_data = json.loads(
            (self.output_dir / "search.json").read_text(encoding="utf-8")
        )
        self.assertEqual(search_data[0]["href"], "posts/example/")
        self.assertEqual(search_data[1]["href"], "posts/example/#notes")

    def test_validation_rejects_a_mismatched_canonical(self) -> None:
        normalize_site(self.output_dir, SITE_URL)
        post_path = self.output_dir / "posts" / "example" / "index.html"
        post_path.write_text(
            post_path.read_text(encoding="utf-8").replace(
                "https://blog.davidlindelof.com/posts/example/",
                "https://blog.davidlindelof.com/wrong/",
            ),
            encoding="utf-8",
        )

        errors = validate_site(self.output_dir, SITE_URL)
        self.assertTrue(any("expected" in error for error in errors))

    def run_script(
        self, *args: str, quarto_env: dict[str, str] | None = None
    ) -> subprocess.CompletedProcess[str]:
        env = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith("QUARTO_")
        }
        env.update(quarto_env or {})
        script = Path(__file__).resolve().parents[1] / "scripts" / "normalize_site_urls.py"
        return subprocess.run(
            [sys.executable, str(script), "--site-url", SITE_URL, *args],
            cwd=self.output_dir,
            env=env,
            capture_output=True,
            text=True,
        )

    def test_preview_does_not_require_a_complete_output_directory(self) -> None:
        # Preview may start with no rendered pages (or only stale branch output).
        output_dir = self.output_dir / "not-rendered-yet"
        result = self.run_script(
            quarto_env={"QUARTO_PROJECT_OUTPUT_DIR": str(output_dir)},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("preview/incremental", result.stdout)
        self.assertFalse(output_dir.exists())

    def test_full_render_uses_quartos_output_directory(self) -> None:
        result = self.run_script(
            quarto_env={
                "QUARTO_PROJECT_OUTPUT_DIR": str(self.output_dir),
                "QUARTO_PROJECT_RENDER_ALL": "1",
            },
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(validate_site(self.output_dir, SITE_URL), [])

    def test_missing_canonical_only_blocks_full_render_or_explicit_validation(self) -> None:
        normalize_site(self.output_dir, SITE_URL)
        post_path = self.output_dir / "posts" / "example" / "index.html"
        stale_page = "<html><head></head><body>Stale page</body></html>"
        post_path.write_text(stale_page, encoding="utf-8")
        preview_env = {"QUARTO_PROJECT_OUTPUT_DIR": str(self.output_dir)}
        cases = [
            ("preview", [], preview_env, 0),
            ("full render", [], {**preview_env, "QUARTO_PROJECT_RENDER_ALL": "1"}, 1),
            ("standalone", ["--output-dir", str(self.output_dir)], {}, 1),
            ("explicit check", ["--check"], preview_env, 1),
        ]
        for name, args, env, expected in cases:
            with self.subTest(name=name):
                result = self.run_script(*args, quarto_env=env)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                if expected:
                    self.assertIn("no canonical URL", result.stderr)
        self.assertEqual(post_path.read_text(encoding="utf-8"), stale_page)


if __name__ == "__main__":
    unittest.main()
