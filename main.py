"""Alien Field Notes: The Two Day Earth Review — entry program.

Writes one original line — an alien tourist's review of planet Earth —
to /output/entry.txt. The competition gate requires UTF-8 text of 1 to 200
characters, not only white space, so the program validates the line before
writing and reads it back to confirm the round-trip.
"""

import os
import sys

ENTRY = (
    "Loved the pizza, feared the Mondays. The locals invented a day they "
    "all dread, then built their whole week around it. 4/5 — would visit "
    "again, never on a Monday."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not start or end with white space", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("round-trip check failed", file=sys.stderr)
        return 1

    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
