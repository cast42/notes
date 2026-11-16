import datetime as dt
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_twil


class TwilActivityTests(unittest.TestCase):
    def test_git_activity_finds_old_sources_without_raw_or_untracked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
            topic = root / "topics" / "learning"
            (topic / "raw").mkdir(parents=True)
            body = '---\ntitle: "Old source"\ndate: 1955-01-01\ntype: book\ntopics: [learning]\n---\n\n## TL;DR\nUseful.\n'
            (topic / "book.md").write_text(body)
            (topic / "raw" / "book.md").write_text(body)
            subprocess.run(["git", "-C", str(root), "add", "topics"], check=True)
            env = {**os.environ, "GIT_AUTHOR_DATE": "2026-11-12T12:00:00+01:00", "GIT_COMMITTER_DATE": "2026-11-12T12:00:00+01:00"}
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "Add book"], check=True, env=env)
            (topic / "untracked.md").write_text(body)
            with patch.object(generate_twil, "ROOT", root), patch.object(generate_twil, "TOPICS_DIR", root / "topics"):
                notes = generate_twil.load_notes(dt.date(2026, 11, 9), dt.date(2026, 11, 15), activity=True)
                self.assertEqual([note.path.name for note in notes], ["book.md"])
                self.assertEqual(notes[0].note_date, dt.date(1955, 1, 1))
                self.assertEqual(generate_twil.load_notes(dt.date(2026, 11, 1), dt.date(2026, 11, 8), activity=True), [])


if __name__ == "__main__":
    unittest.main()
