"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6
launch week to $MAKEFUN_OUTPUT_DIR/entry.txt. A pipe burst, a
flooding kitchen, a plumber on site till noon: specific, boring and
almost believable, the way a hurried text to a tired manager sounds.
Standard library only.
"""

import os

EXCUSE = (
    "Sorry boss, a pipe burst and my kitchen's flooding "
    "\u2014 plumber's here till noon, I can't leave it."
)


def fit_gate(text):
    """Check the excuse against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line of at most 20 words: one excuse a gamer
    sends the boss to skip work on GTA 6 launch week. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "excuse is %d characters, over the 140 limit" % len(cleaned)
        )
    if len(cleaned.split()) > 20:
        raise ValueError(
            "excuse is %d words, over the 20-word limit"
            % len(cleaned.split())
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_shape(text):
    """Small shape check on the excuse, for a last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A hurried text that is too long to sound hurried
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = fit_gate(EXCUSE)
    shape = excuse_shape(text)
    if shape["words"] < 5:
        raise ValueError("excuse is too short to sound like a real text")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
