#!/usr/bin/env python3
"""Sleeve Notes for the Frog Trio — make.fun entry.

Reads the album title and back-cover blurb from entry.txt (kept next to
this file) and writes it to /output/entry.txt, where the bounty harness
reads it.
"""
import os
import sys

ENTRY = "entry.txt"


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, ENTRY), encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        raise SystemExit("entry.txt is empty or only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    sys.stdout.write(text)
    if not text.endswith("\n"):
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
