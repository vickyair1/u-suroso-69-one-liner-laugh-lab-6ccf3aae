#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line -- the excuse a robot vacuum gives after
eating a sock -- to /output/entry.txt and prints it to stdout.
Deterministic: the same line every run.
"""

import os

LINE = "I didn't eat your sock. I performed an unscheduled ingestion audit, and the sock failed."


def validate(line):
    """Entry gate: exactly one line, 1-200 characters, non-empty."""
    if not line or "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one non-empty line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    return line


def write_entry(line):
    """Write exactly the line to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    line = validate(LINE)
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
