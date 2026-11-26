#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes the printer's one-line comeback to /output/entry.txt (the path the
grader reads) and prints it to stdout. Deterministic: the line is a
constant, so every run produces the exact same entry.
"""

import os

ENTRY = (
    "I've printed 48,312 pages for you without a single complaint. "
    "This one I ate on purpose \u2014 it was a 47-slide deck called "
    "'Synergy,' and frankly, I did us both a favour."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 240:
        raise SystemExit(f"entry length {len(line)} out of range 1-240")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read it back: the file the grader scores must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != line:
        raise SystemExit("read-back mismatch: /output/entry.txt != entry")
    print(line)


if __name__ == "__main__":
    main()
