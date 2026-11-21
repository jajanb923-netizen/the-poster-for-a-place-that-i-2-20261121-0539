# Velmora — The City Beneath the Aurora Sea

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/jajanb923-netizen/the-poster-for-a-place-that-i-2-20261121-0539/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/jajanb923-netizen/the-poster-for-a-place-that-i-2-20261121-0539/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for a place that does not exist: **Velmora, the city beneath
the aurora sea** — one crystal lighthouse on a rocky islet, its beam sweeping
a mirror sea, a lone rowboat rowing toward the light. Built for the make.fun
bounty [The Poster for a Place That Isn't There](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539).

## Run it

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, deterministic, no network).
`draw.py` is the Pillow program that draws the poster; `main.py` copies the
rendered image to the output path, the same pattern as the news-image
entries. Run `python3 draw.py` to re-render `entry.png` from scratch.
