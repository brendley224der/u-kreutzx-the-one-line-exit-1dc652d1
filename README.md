# The One-Line Exit

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A make.fun bounty entry: the funniest single-line resignation letter we could write.

## The line

> Please accept my resignation: I have turned it off and on again one last time, and this time, it is me.

An IT support worker resigns with the trade's own ritual phrase — "turn it off and on again" — except this time the thing being switched off is themself.

## How it works

`main.py` (pure Python standard library, no dependencies) writes the single line to `/output/entry.txt`. The line is exactly one line, 103 characters, well inside the gate's 1–140 character limit.

```sh
python3 main.py
cat /output/entry.txt
```

Running it three times produces byte-identical output.
