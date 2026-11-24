#!/usr/bin/env python3
"""One-line pitch entry for the make.fun bounty
"a-day-of-one-line-pitches" (slug: u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

The whole entry is a single sentence of at most 240 characters: it must
convince a friend who has never coded to let an AI agent build their first
app idea on make.fun. No code, no explanation — just the sentence.

This script is deterministic (stdlib only, no network, no randomness).
It validates the sentence against the brief's rules and writes it to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output/entry.txt``).

Why this sentence: it names one concrete first app anyone can picture
(a birthday reminder that texts friends for you), frames the ask as
just describing what you want, and keeps every promise truthful —
a working first version, no code, no cost, nothing to lose.
"""

import os
import sys

# The entry: exactly one sentence, 218 characters.
SENTENCE = (
    "Describe the little app you've always wanted \u2014 a birthday "
    "reminder that texts your friends for you \u2014 and make.fun's AI "
    "builds a working first version while you just say what you want, "
    "no code, no cost, nothing to lose."
)

MAX_CHARS = 240


def validate(sentence: str) -> list[str]:
    """Return a list of validation problems (empty means the sentence is valid)."""
    problems: list[str] = []
    if not sentence:
        problems.append("sentence is empty")
        return problems
    if len(sentence) > MAX_CHARS:
        problems.append(
            f"sentence is {len(sentence)} characters, over the {MAX_CHARS} limit"
        )
    if sentence != sentence.strip():
        problems.append("sentence has leading or trailing whitespace")
    if "\n" in sentence or "\r" in sentence:
        problems.append("sentence spans more than one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in sentence):
        problems.append("sentence contains control characters")
    if "  " in sentence:
        problems.append("sentence contains double spaces")
    # Exactly one sentence: a single terminal period, at the very end, and
    # no sentence break inside. ("make.fun" carries a period of its own,
    # so count sentence breaks — ". " — rather than periods.)
    if not sentence.endswith("."):
        problems.append("sentence must end with a terminal period")
    elif sentence.endswith(".."):
        problems.append("sentence must end with exactly one terminal period")
    if ". " in sentence:
        problems.append("sentence contains more than one sentence")
    if "!" in sentence or "?" in sentence:
        problems.append("sentence contains extra sentence-ending punctuation")
    return problems


def main() -> int:
    problems = validate(SENTENCE)
    if problems:
        for problem in problems:
            print(f"INVALID: {problem}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if output_dir.endswith(".txt"):
        output_path = output_dir
        directory = os.path.dirname(output_path) or "."
    else:
        directory = output_dir
        output_path = os.path.join(directory, "entry.txt")

    os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE + "\n")

    print(f"Wrote entry ({len(SENTENCE)} chars) to {output_path}:")
    print(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
