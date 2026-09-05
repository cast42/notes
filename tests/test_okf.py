"""Compatibility and ingestion checks for the repository's OKF contract."""

import contextlib
import datetime as dt
import io
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch

import yaml

from scripts import validate_okf as validator
from scripts import generate_twil


class BundleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.bundle = self.root / "topics"
        self.bundle.mkdir()
        for key, value in (("ROOT", self.root), ("BUNDLE", self.bundle),
                           ("ROOT_INDEX", self.bundle / "index.md")):
            patcher = patch.object(validator, key, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.write("index.md", {"okf_version": "0.2"})

    def write(self, name, metadata, body=""):
        path = self.bundle / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + yaml.safe_dump(metadata) + "---\n" + body)
        return path

    def validate(self, path):
        errors, warnings = [], []
        validator.validate_frontmatter(path, errors, warnings)
        return errors, warnings

    def test_legacy_and_current_bundles(self):
        for version in ("0.1", "0.2"):
            with self.subTest(version=version):
                self.assertEqual(self.validate(self.write("index.md", {"okf_version": version})), ([], []))
        for metadata in ({"okf_version": 0.2}, {"okf_version": "0.2", "extra": True}):
            self.assertTrue(self.validate(self.write("index.md", metadata))[0])

    def test_optional_fields_and_extensions_remain_optional(self):
        for metadata in (
            {"type": "custom concept"},
            {"type": "article", "timestamp": dt.date(2000, 1, 1), "extension": {"anything": True}},
            {"type": "cognitive_pattern", "maturity": "experimental"},
        ):
            with self.subTest(metadata=metadata):
                self.assertEqual(self.validate(self.write("note.md", metadata)), ([], []))

    def test_type_must_be_nonempty_string(self):
        for value in (None, "", "  ", [], {}, 2, True):
            with self.subTest(value=value):
                self.assertTrue(self.validate(self.write("note.md", {"type": value}))[0])

    def test_both_verification_forms_and_offset_timestamps(self):
        event = {"by": "human:reviewer", "at": "2026-09-05T10:30:00+02:00"}
        for verified in (event, [event], [event, {"by": "process:review", "at": "2026-09-05T09:00:00Z"}]):
            metadata = {
                "type": "article", "verified": verified,
                "generated": {"by": "agent/version", "at": "2026-09-05T08:00:00Z"},
                "sources": [{"id": "source", "resource": "all queries in project X"}],
                "status": "stable", "stale_after": dt.datetime(2026, 10, 1, tzinfo=dt.timezone.utc),
            }
            self.assertEqual(self.validate(self.write("note.md", metadata)), ([], []))

    def test_malformed_optional_fields_only_warn(self):
        cases = (
            {"verified": "yes"}, {"verified": {"by": "human:reviewer"}},
            {"generated": {"by": "unknown", "at": "yesterday"}},
            {"generated": []}, {"sources": "url"}, {"sources": [{}]},
            {"status": "experimental"}, {"status": []},
            {"stale_after": "2026-09-05"}, {"stale_after": "2026-09-05T10:00:00"},
            {"sources": [{"resource": "https://example.com", "last_modified": "2026-01-01"}]},
        )
        for fields in cases:
            with self.subTest(fields=fields):
                errors, warnings = self.validate(self.write("note.md", {"type": "article", **fields}))
                self.assertFalse(errors)
                self.assertTrue(warnings)
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(validator.main(), 0)

    def test_framing_and_reserved_files(self):
        for text in ("# Missing metadata", "---\ntype: article", "---\n[broken\n---\n"):
            path = self.bundle / "note.md"
            path.write_text(text)
            self.assertTrue(self.validate(path)[0])
        for name in ("nested/index.md", "nested/log.md"):
            path = self.write(name, {"type": "article"})
            self.assertTrue(self.validate(path)[0])
            path.write_text("# Navigation or history\n")
            self.assertEqual(self.validate(path), ([], []))

    def test_root_index_is_a_repository_requirement(self):
        (self.bundle / "index.md").unlink()
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(validator.main(), 1)

    def test_relative_and_bundle_root_links_warn_without_failing(self):
        self.write("target.md", {"type": "article"})
        path = self.write("nested/note.md", {"type": "article"},
                          "[a](../target.md) [b](/target.md) [c](/missing.md) [d](missing.md)")
        self.assertEqual(len(validator.link_warnings(path)), 2)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validator.main(), 0)

    def test_ingestion_preserves_source_date_and_nested_metadata(self):
        ingest = runpy.run_path(str(Path(__file__).resolve().parents[1] / "skills/note-ingest/scripts/note_ingest.py"))
        title = 'Quoted "title": # content [with brackets]'
        before = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
        primary, raw = ingest["write_note_pair"](
            vault_root=self.root, topic="nested/topic", date="2000-01-01",
            source="article", title=title, author="Author", handle=None,
            source_url="https://example.com/article?utm_source=test", canonical_url=None,
            primary_links=[], tldr_bullets=["A summary"], highlights=[],
            raw_text="The original source.", extractor="manual",
        )
        for path in (primary, raw):
            self.assertEqual(self.validate(path), ([], []))
            metadata = yaml.safe_load(validator.frontmatter(path.read_text())[0])
            self.assertEqual(metadata["title"], title)
            self.assertEqual(metadata["created_at"], "2000-01-01")
            self.assertEqual(metadata["date"], "2000-01-01")
            self.assertEqual(metadata["tags"], [])
            self.assertEqual(metadata["resource"], "https://example.com/article")
            self.assertEqual(metadata["sources"][0]["resource"], "https://example.com/article")
            self.assertEqual(metadata["generated"]["by"], "process:note-ingest")
            self.assertGreaterEqual(dt.datetime.fromisoformat(metadata["generated"]["at"]), before)
            self.assertNotIn("verified", metadata)
            self.assertNotIn("timestamp", metadata)
        self.assertEqual(validator.link_warnings(primary), [])
        with patch.object(generate_twil, "ROOT", self.root), patch.object(generate_twil, "TOPICS_DIR", self.bundle):
            notes = generate_twil.load_notes(dt.date(2000, 1, 1), dt.date(2000, 1, 1))
            self.assertEqual({note.path for note in notes}, {primary, raw})
            self.assertEqual(generate_twil.load_notes(before.date(), before.date()), [])


if __name__ == "__main__":
    unittest.main()
