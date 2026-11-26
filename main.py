"""The One-Line Exit — make.fun entry.

Writes a single-line resignation letter to /output/entry.txt.
Pure standard library only.

The joke: an IT support worker resigns with the trade's own ritual
phrase — "turn it off and on again" — except this time the thing
being switched off is themself. The punchline lands in the last
clause, and the letter still reads like one a person could send.
"""

import os

# One line, 140 characters or fewer.
LINE = (
    "Please accept my resignation: I have turned it off and on again "
    "one last time, and this time, it is me."
)


def build_line() -> str:
    """Return the entry text, enforcing the gate's shape rules."""
    text = LINE.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"line is {len(text)} chars, must be 1-140")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main() -> None:
    text = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    # Confirm what was written is exactly the line we built.
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        assert fh.read() == text


if __name__ == "__main__":
    main()
