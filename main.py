#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan (one line, at most 20 words, 1-140 characters)
to /output/entry.txt.
"""

import os

SUBJECT = "Your Solana wallet, awake while you sleep"
PROMISE = "it signs, swaps, and sends"
CLOSING_IMAGE = "before your coffee cools"


def build_slogan() -> str:
    """Assemble the slogan from its three beats.

    Subject names the wallet, promise states what it does, and the
    closing image is the concrete picture the line ends on.
    """
    return f"{SUBJECT}: {PROMISE} {CLOSING_IMAGE}."


SLOGAN = build_slogan()

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140
MAX_WORDS = 20


def validate(text: str) -> None:
    """Check the slogan against the competition gate before writing."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("slogan is empty")
    if "\n" in stripped:
        raise ValueError("slogan must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"slogan is {len(stripped)} chars, over the {MAX_CHARS} limit")
    if len(stripped.split()) > MAX_WORDS:
        raise ValueError("slogan is over the 20 word limit")


def write_entry(text: str, path: str = OUTPUT_PATH) -> str:
    """Validate the slogan, then write it to the output path."""
    validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    path = write_entry(SLOGAN)
    print(f"wrote {len(SLOGAN)} chars, {len(SLOGAN.split())} words to {path}")


if __name__ == "__main__":
    main()
