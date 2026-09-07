from __future__ import annotations

import json
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


if __name__ == "__main__":
    unittest.main()
