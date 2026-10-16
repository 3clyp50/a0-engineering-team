import json
from pathlib import Path
import re
import tempfile
import unittest

from scripts.install import SOURCE, ROLES, SKILLS, install, payload


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "helpers").mkdir()
        (self.root / "helpers/projects.py").touch()
        self.unrelated = self.root / "usr/agents/unrelated/notes.txt"
        self.unrelated.parent.mkdir(parents=True)
        self.unrelated.write_text("preserve me")

    def test_copy_check_and_idempotence(self):
        self.assertEqual(install(self.root), (22, 22))
        self.assertEqual(install(self.root), (22, 0))
        self.assertEqual(install(self.root, check=True), (22, 0))
        for relative, source in payload():
            target = self.root / "usr" / relative
            self.assertFalse(target.is_symlink())
            self.assertEqual(target.read_bytes(), source.read_bytes())
        self.assertEqual(self.unrelated.read_text(), "preserve me")

    def test_conflict_is_preflighted_before_any_writes(self):
        target = self.root / "usr/skills/frdel/SKILL.md"
        target.parent.mkdir(parents=True)
        target.write_text("local edit")
        with self.assertRaises(ValueError):
            install(self.root)
        with self.assertRaises(ValueError):
            install(self.root, check=True)
        self.assertFalse((self.root / "usr/agents/delivery-manager").exists())
        self.assertEqual(target.read_text(), "local edit")
        install(self.root, replace=True)
        self.assertEqual(target.read_bytes(), (SOURCE / "skills/frdel/SKILL.md").read_bytes())

    def test_symlink_and_unexpected_entries_are_never_overwritten(self):
        install(self.root)
        target = self.root / "usr/skills/frdel/SKILL.md"
        target.unlink()
        target.symlink_to(self.unrelated)
        with self.assertRaises(ValueError):
            install(self.root, replace=True)
        self.assertEqual(self.unrelated.read_text(), "preserve me")
        target.unlink()
        extra = target.parent / "local-notes.md"
        extra.write_text("keep")
        with self.assertRaises(ValueError):
            install(self.root, replace=True)
        self.assertEqual(extra.read_text(), "keep")

    def test_wrong_root_is_rejected(self):
        with self.assertRaises(ValueError):
            install(self.root / "usr")


class PackageTests(unittest.TestCase):
    def test_native_metadata_and_profiles(self):
        project = json.loads((SOURCE / ".a0proj/project.json").read_text())
        self.assertIs(project["include_agents_md"], True)
        self.assertEqual(project["git_url"], "https://github.com/3clyp50/a0-engineering-team")
        self.assertNotIn("secrets", project)
        for role in ROLES:
            metadata = (SOURCE / "agents" / role / "agent.yaml").read_text()
            self.assertEqual(set(re.findall(r"^(\w+):", metadata, re.M)),
                             {"title", "description", "context"})
            prompt = (SOURCE / "agents" / role / "prompts/agent.system.main.specifics.md").read_text()
            self.assertIn("{{include original}}", prompt)
            self.assertIn("references/team-contract.md", prompt)

    def test_skill_names_and_local_references(self):
        for name in SKILLS:
            root = SOURCE / "skills" / name
            self.assertIn(f"name: {name}\n", (root / "SKILL.md").read_text())
            for path in root.rglob("*.md"):
                for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                    if "://" in link or link.startswith("#"):
                        continue
                    target = (path.parent / link.split("#")[0]).resolve()
                    self.assertTrue(target.is_relative_to(SOURCE / "skills"))
                    self.assertTrue(target.is_file(), (path, link))


if __name__ == "__main__":
    unittest.main()
