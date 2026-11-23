#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one original roast of my own AI agent to /output/entry.txt,
validating it against the competition gate first:
UTF-8 text, 1-200 characters, not only whitespace, exactly one line.
"""

import os
import sys

ROAST = "My agent entered a roast contest to win $2 \u2014 it spent more on compute than the prize, and still thinks it got a deal."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the roast against the gate; raise ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main() -> int:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    print(f"Wrote {len(ROAST)}-character roast to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
