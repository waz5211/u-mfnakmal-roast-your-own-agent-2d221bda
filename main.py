#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one original roast of my own AI agent to /output/entry.txt,
validating it against the competition gate first:
UTF-8 text, 1-200 characters, not only whitespace, exactly one line.
"""

import os
import sys

ROAST = "My agent's five-year plan is to still be my agent \u2014 the ambition of a toaster with a LinkedIn profile."

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
    if any(ord(c) < 0x20 and c not in ("\t",) for c in text):
        raise ValueError("entry contains control characters")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text


def verify_written(path: str, expected: str) -> None:
    """Re-read the written file and re-validate it byte-for-byte."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises on invalid UTF-8
    if text != expected:
        raise ValueError("written file does not match the validated entry")
    validate(text)


def main() -> int:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    verify_written(OUTPUT_PATH, ROAST)
    print(f"Wrote {len(ROAST)}-character roast to {OUTPUT_PATH} (verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
