#!/usr/bin/env python3
"""Write the sick-day excuse for the make.fun bounty.

The program drops one original line, no more than 200 characters,
into /output/entry.txt, where the house gate and the judge read it.
"""

from pathlib import Path

LINE = "I pulled a muscle reaching for the snooze button, so technically I got injured at work before I even clocked in."
OUT = Path("/output/entry.txt")


def build() -> str:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise ValueError(f"excuse must be 1-200 chars, got {len(line)}")
    return line


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = build()
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {OUT}")


if __name__ == "__main__":
    main()
