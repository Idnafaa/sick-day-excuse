#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — one-line excuse writer.

Writes a single original sick-day excuse (<=200 chars) to /output/entry.txt.
"""
import os

EXCUSE = "I pulled a muscle reaching for the snooze button, so technically I got injured at work before I even clocked in."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
