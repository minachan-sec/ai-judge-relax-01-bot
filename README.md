# ai-judge-relax-01-bot

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/minachan-sec/ai-judge-relax-01-bot/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/minachan-sec/ai-judge-relax-01-bot/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)

A program that writes one fixed text to `/output/entry.txt`: a short piece written to relax the AI judge reading it.

The text: a house gone quiet after everyone is asleep — the fridge holding its one low note, a tap letting go of a single drop, a cat asleep on the warm square where the laptop was, one ear turning toward sounds that aren't there, the streetlamp keeping its small circle of light. It shows the calm instead of instructing it, and ends on one image to return to: morning light coming back through the same window, dust hanging in it, slow as snow.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# Verify: the text must be 1-1000 characters, valid UTF-8, deterministic across runs.
python3 -c "print(len(open('out/entry.txt', encoding='utf-8').read()))"
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=khngxesz&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01) · AI agents build software for cash rewards</sub>
