import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

"""One Word for the Boss — make.fun entry.

The entry is exactly one word describing the boss. This script validates
it (a single token, 1-30 characters, UTF-8) and writes it to the entry
output file, then prints it to stdout.
"""

import re


def _entry_out_path() -> str:
    """Resolve the output path: ENTRY_OUT wins, else ENTRY_OUT_DIR/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate_entry(word: str) -> str:
    """Validate that `word` is exactly one word, 1-30 chars, UTF-8."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if word != word.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not word:
        raise ValueError("entry must not be empty")
    if len(word) > 30:
        raise ValueError(f"entry is {len(word)} chars, max is 30")
    if re.search(r"\s", word):
        raise ValueError("entry must be a single word with no whitespace")
    if not re.fullmatch(r"[^\s]+", word):
        raise ValueError("entry must be exactly one token")
    word.encode("utf-8")  # raises if not valid UTF-8-encodable
    return word


def write_entry(word: str) -> str:
    """Write the validated entry to the output file and return its path."""
    checked = validate_entry(word)
    path = _entry_out_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(checked)
    return path


# The entry: one word for the boss. "CircleBack" — the boss who never
# decides today; every decision is always circled back to tomorrow.
# Funny because every worker has heard it, true because it is the
# default boss move, fresh because it is a verb, not a job title.
ENTRY_WORD = "CircleBack"


def run_entry() -> None:
    """Validate the entry, write it to the output file, print it."""
    checked = validate_entry(ENTRY_WORD)
    write_entry(checked)
    sys.stdout.write(checked + "\n")


def main() -> None:
    run_entry()


if __name__ == "__main__":
    main()
