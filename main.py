"""One Word, First Thought — make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the first thought that lands — "Meanwhile".

Pure Python 3.13 standard library only; no network, no randomness,
fully deterministic: the same word on every run.
"""

import os
import sys

WORD = "Meanwhile"


def validate_word(word: str) -> str:
    """Return the word if it is exactly one word of 1-24 code points.

    Raises ValueError for anything that is blank, contains whitespace,
    or is longer than 24 Unicode code points.
    """
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or word.strip() == "":
        raise ValueError("word must not be blank")
    if len(word) != len(word.strip()):
        raise ValueError("word must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("word must contain no control characters")
    if not 1 <= len(word) <= 24:
        raise ValueError("word must be 1-24 Unicode code points")
    return word


def main() -> int:
    word = validate_word(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file holds exactly the word, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
