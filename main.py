"""Roast Your Own Agent — make.fun entry.

Writes exactly one funny line (104 chars) to entry.txt.
Python stdlib only, no local imports, no network, no hardcoded paths.
"""

import os

ENTRY = (
    "My agent apologized for the bug, fixed it in a file that doesn't "
    "exist, then apologized for apologizing."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("gate failed: line is blank or has surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: line must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("gate failed: line must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the write round-trips byte-identically: a partial or
    # re-encoded write must never silently ship a different entry.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("gate failed: written entry.txt does not match the line")


if __name__ == "__main__":
    main()
