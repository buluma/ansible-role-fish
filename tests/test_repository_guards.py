"""Exercise the repository and signing-key guards with representative inputs."""

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

ROLE = Path(__file__).resolve().parents[1]


def task_named(path, name):
    tasks = yaml.safe_load((ROLE / path).read_text())
    for task in tasks:
        if task.get("name") == name:
            return task
        for nested in task.get("block", []):
            if nested.get("name") == name:
                return nested
    raise AssertionError(f"Task not found: {name}")


def run_guard(task, variables):
    play = [{"hosts": "localhost", "gather_facts": False, "vars": variables, "tasks": [task]}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml") as playbook:
        yaml.safe_dump(play, playbook)
        playbook.flush()
        return subprocess.run(
            ["ansible-playbook", "-i", "localhost,", "-c", "local", playbook.name],
            capture_output=True,
            text=True,
            check=False,
        )


class RepositoryGuardsTest(unittest.TestCase):
    def test_supported_and_unsupported_platforms(self):
        task = task_named("tasks/install-Debian.yml", "install-Debian | Ensure the fish repository supports this platform")
        for distro, major, version, release, expected in [
            ("Debian", "13", "13", 3, False),
            ("Debian", "12", "12", 4, True),
            ("Debian", "11", "11", 4, False),
            ("Ubuntu", "25", "25.04", 3, False),
            ("Ubuntu", "24", "24.04", 3, True),
        ]:
            with self.subTest(distro=distro, version=version, release=release):
                result = run_guard(task, {"ansible_facts": {"distribution": distro, "distribution_major_version": major, "distribution_version": version}, "fish_release_version": release})
                self.assertEqual(result.returncode == 0, expected, result.stdout + result.stderr)

    def test_rejects_unusable_signing_keys(self):
        task = task_named("tasks/install-key.yml", "install-key | Reject expired or revoked primary keys")
        for status, expected in [("e", False), ("r", False), ("d", False), ("-", True)]:
            with self.subTest(status=status):
                result = run_guard(task, {"_fish_key_info": {"stdout_lines": [f"pub:{status}:2048:1:TEST:1:2::::::"]}, "_fish_key_url": "example"})
                self.assertEqual(result.returncode == 0, expected, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
