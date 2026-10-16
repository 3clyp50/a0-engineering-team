#!/usr/bin/env python3
"""Copy this team's ordinary files into a selected Agent Zero root."""
import argparse
from pathlib import Path
import shutil

SOURCE = Path(__file__).resolve().parents[1]
ROLES = ("chief-of-staff", "delivery-manager", "engineering-worker",
         "engineering-reviewer", "design-reviewer", "engineering-verifier")
SKILLS = ("engineering-delivery", "engineering-review", "frdel")


def payload():
    for category, names in (("agents", ROLES), ("skills", SKILLS)):
        for name in names:
            folder = SOURCE / category / name
            if not folder.is_dir() or folder.is_symlink():
                raise ValueError(f"Missing or symlinked source: {folder}")
            for source in sorted(folder.rglob("*")):
                if source.is_symlink() or not (source.is_dir() or source.is_file()):
                    raise ValueError(f"Source must contain ordinary files: {source}")
                if source.is_file():
                    yield source.relative_to(SOURCE), source


def install(root, *, check=False, replace=False):
    root = Path(root).absolute()
    if root.is_symlink() or not (root / "helpers/projects.py").is_file():
        raise ValueError("Select an Agent Zero root containing helpers/projects.py")
    sources = dict(payload())
    expected = {root / "usr" / relative for relative in sources}
    for category, names in (("agents", ROLES), ("skills", SKILLS)):
        for name in names:
            folder = root / "usr" / category / name
            for ancestor in (root / "usr", folder.parent, folder):
                if ancestor.is_symlink() or (ancestor.exists() and not ancestor.is_dir()):
                    raise ValueError(f"Destination must be an ordinary directory: {ancestor}")
            if folder.exists():
                for item in folder.rglob("*"):
                    if item.is_symlink() or not (item.is_dir() or item in expected):
                        raise ValueError(f"Unexpected destination entry; preserve it manually: {item}")
    changed = []
    for relative, source in sources.items():
        target = root / "usr" / relative
        if target.exists() and not target.is_file():
            raise ValueError(f"Destination is not an ordinary file: {target}")
        if not target.exists() or target.read_bytes() != source.read_bytes():
            changed.append((source, target))
    if check and changed:
        raise ValueError(f"Deployment differs in {len(changed)} files; inspect before replacing")
    if not replace and any(target.exists() for _, target in changed):
        raise ValueError("Existing files differ; inspect/back up local edits, then use --replace")
    if not check:
        for source, target in changed:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    return len(sources), len(changed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Agent Zero root, normally /a0 in Docker")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Verify copies without writing")
    mode.add_argument("--replace", action="store_true", help="Replace differing known files")
    args = parser.parse_args()
    try:
        count, changed = install(args.root, check=args.check, replace=args.replace)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"{count} ordinary files verified; {changed} copied" if not args.check
          else f"{count} deployed files match versioned source")
