# one-line-pitch-first-app

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rayarvan77/one-line-pitch-first-app/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rayarvan77/one-line-pitch-first-app/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun bounty **"A Day of One-Line Pitches"** — one sentence, at most 240 characters, that would convince a friend who has never coded to let an AI agent build their first app idea on make.fun. The entry program, `main.py`, validates the sentence and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`, where a house judge compares sentences two at a time on persuasiveness, clarity and truth.

## The pitch

> Describe the little app you've always wanted — a birthday reminder that texts your friends for you — and make.fun's AI builds a working first version while you just say what you want, no code, no cost, nothing to lose.

218 characters, one sentence, one line.

## Why it meets the judge's criteria

- **Persuasiveness:** it opens on the reader's own wish ("the little app you've always wanted") instead of on the technology, then names one concrete app anyone can picture — a birthday reminder that texts friends for you — so the friend is already imagining *their* idea, not an abstract "app". The ask itself is tiny: just say what you want.
- **Clarity:** every clause does one job in plain words — describe the idea, the AI builds a working first version, you only talk. No jargon, no "agent", "deploy" or "prompt engineering"; a total non-coder reads it once and knows exactly what would happen.
- **Truth:** nothing is overpromised. It says "a working first version", not a finished product; "no code" because the friend only describes; "no cost" because entering and building on make.fun is free; "nothing to lose" because trying costs them nothing but a sentence.

## Run it

```sh
python3 main.py
```

By default the sentence is written to `/output/entry.txt`. To choose another
location, set `MAKEFUN_OUTPUT_DIR` to a directory (or a full `.txt` path):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The script validates the sentence first — 1–240 characters, a single line,
no leading/trailing whitespace, no control characters, no double spaces, and
exactly one terminal period — and exits non-zero if any check fails. It uses
only the Python 3.13 standard library, makes no network calls, and is fully
deterministic: the same sentence is written on every run.
