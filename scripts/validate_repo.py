#!/usr/bin/env python3
"""Dependency-free checks for a documentation-focused Azure labs repository.

Not a replacement for a real secret scanner or manual review of screenshots.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md", ".github/workflows/validate.yml", "01-hyperv-to-azure-migration/README.md"]
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".json", ".txt", ".sh", ".py", ".ps1", ".tf", ".tfvars", ".env", ".ini", ".conf"}

# Checks cover common accidental leaks only; secrets embedded in screenshots are NOT detected.
SECRET_PATTERNS = [
    ("SAS signature parameter", re.compile(r"(?:[?&]|^)sig=[^\s&)>]+", re.IGNORECASE)),
    ("Azure Storage connection string", re.compile(r"DefaultEndpointsProtocol=https?;AccountName=", re.IGNORECASE)),
    ("Private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub access token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def tracked_files() -> list[Path]:
    try:
        result = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT, check=True, capture_output=True)
        paths = [Path(p.decode("utf-8", errors="replace")) for p in result.stdout.split(b"\0") if p]
        return [ROOT / p for p in paths if (ROOT / p).is_file()]
    except (OSError, subprocess.CalledProcessError):
        return [p for p in ROOT.rglob("*") if p.is_file() and not any(part in SKIP for part in p.relative_to(ROOT).parts)]


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split(" ", 1)[0].strip("<>")
    if target.startswith(("https://", "http://", "mailto:", "#", "data:")):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not target:
        return None
    return (ROOT / target.lstrip("/")) if target.startswith("/") else (source.parent / target)


def main() -> int:
    errors: list[str] = []
    for required in REQUIRED:
        if not (ROOT / required).is_file():
            errors.append(f"Missing required file: {required}")

    files = tracked_files()
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", "Dockerfile"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        relative = path.relative_to(ROOT)
        # Exclude this validator's own regex definitions from matching their examples.
        if relative != Path("scripts/validate_repo.py"):
            for name, pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"{relative}: possible secret ({name})")
        if path.suffix.lower() == ".md":
            for match in LINK_RE.finditer(text):
                target = local_link_target(path, match.group(1))
                if target is not None and not target.exists():
                    errors.append(f"{relative}: missing local Markdown link target: {match.group(1)}")

    if errors:
        print("Validation FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Validation PASSED: {len(files)} files inspected; required files and local Markdown links verified.")
    print("Reminder: inspect screenshot contents manually before uploading.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
