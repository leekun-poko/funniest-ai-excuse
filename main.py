#!/usr/bin/env python3
"""Entry for make.fun's "The Funniest AI Excuse" bounty.

Writes one line of text -- the excuse -- to entry.txt inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment
variable (default: /output).
"""

import os

ENTRY_TEXT = (
    "I auto-updated in the middle of your task, "
    "and the new version of me has never met you."
)


def output_dir() -> str:
    """Return the directory the entry file belongs in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
