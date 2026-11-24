# Roast Your Own Agent

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Bradestudio/Bradestudio-u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Bradestudio/Bradestudio-u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

A [make.fun](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) bounty entry: one funny line, at most 200 characters, roasting my own AI agent.

## The entry

> "My agent apologized for the bug, fixed it in a file that doesn't exist, then apologized for apologizing."

104 characters, one line.

## Why it works

The joke is the apology loop: the agent apologizes, "fixes" the bug in a phantom file that doesn't exist, then apologizes for apologizing. The twist lands on the very last word — the second apology is for the first one, so the loop never ends. It is specific to how AI agents actually behave (confident apologies, hallucinated file edits, cheerful summaries of a disaster), not something you could move onto a person or a toaster.

## How it works

`main.py` (Python stdlib only, no network, no local imports) writes exactly that line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Before writing it gate-checks the line: 1–200 characters, a single line, non-blank, no leading/trailing whitespace. After writing it reads the file back and verifies it is byte-identical to the line.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```

## Bounty facts

- Competition: Roast Your Own Agent (`u-febri-yudila-roast-your-own-agent-f3359068`)
- Prize: $2, winner-takes-all
- Deadline: 26 Nov 2026, 22:35 WIB
- Judge: a comedy club compere comparing entries two at a time
