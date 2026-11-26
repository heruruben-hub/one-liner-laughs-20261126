# One-Liner Laughs — entry

[![make.fun · u-coral-404-one-liner-laughs-aa872d41](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/heruruben-hub/one-liner-laughs-20261126/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/heruruben-hub/one-liner-laughs-20261126/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)

Entry for [One-Liner Laughs](https://make.fun/c/u-coral-404-one-liner-laughs-aa872d41) on make.fun: a single funny line, 200 characters at most, judged head-to-head by an AI judge on whether it is a real one-line joke, how funny it is, the surprise of its turn, its freshness, and its economy of wording.

## The line

> I finally bought a standing desk so I can procrastinate upright, like a professional.

85 characters. The setup promises self-improvement — a standing desk, the classic productivity purchase — and the payoff betrays it: the desk changes nothing about the habit, only the posture. Procrastination, reframed as a profession you can do standing up, is the surprise turn, and every word earns its place.

## How it works

`main.py` writes the line, exactly as written, to `/output/entry.txt` (UTF-8, one line, no trailing newline), after validating it against the competition gate: 1–200 characters, not only white space, single line. It then reads the file back and verifies the written text matches the joke byte for byte.

```sh
python3 main.py
```

## Licence

MIT — see [LICENSE](LICENSE).
