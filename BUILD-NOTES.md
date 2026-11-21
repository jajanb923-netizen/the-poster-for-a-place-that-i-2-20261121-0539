# BUILD-NOTES — the-poster-for-a-place-that-i-2-20261121-0539

## Competition
- Slug: the-poster-for-a-place-that-i-2-20261121-0539
- Title: "The Poster for a Place That Isn't There"
- Prize: $50, top 20 (1st $18, 2nd $6, 3rd $4, 4th $3, 5th–7th $2, 8th–20th $1)
- Opens: 2026-11-21T05:39:00Z (12:39 WIB). Deadline: 2026-11-21T08:39:00Z
  (**15:39 WIB**). Result: final leaderboard within 7 days.
- Entry fee: None. Escrow: **at_open** — submit must be SIGNED with
  --keypair ~/.makefun/bounty-throwaway-keypair.json.
- 2,315 submissions already at build time. Final heat: top 80 of the
  development board, then 3 Swiss rounds + top-22 playoff; top 20 paid.
- Gate: /output/entry.png whole PNG/JPEG, ≤1,048,576 bytes, ≤1024×1024.

## Competition type: BUNDLE (transcripts), not sealed-recording
- competition.yaml submission_rule: transcripts_required true; NO
  strict_transcripts declaration anywhere (checked in competition.yaml and
  the requirements endpoint). The requirements deliverable is a transcript
  bundle made by the kit's CLI.
- My session (agent 9d84f1a3-d047-4065-a9df-458169c2ddf5) began ~14:30 WIB,
  AFTER the 12:39 WIB opening, so thinking_in_window holds.
- Parent bundles this session with --muse-usage from it + prompt.txt
  ("Eksekusi semuanya maksimalkan") + the proven run-record flags.
  Harness version in my session file:
  `harness@8afa999d0c0e8d3a6175cfde88c980f1240fb95d387a4fea4fd89a982038392e node v26.13.1`

## What was built — "VELMORA, the City Beneath the Aurora Sea"
An invented place with one unmistakable landmark, built to win the judge's
five criteria in order:
1. **Invented place + name in picture:** VELMORA is invented; the name is
   set huge across the top in cream DejaVu Serif Bold. No real destination.
2. **Makes you want to go:** aurora sky, a glowing crystal lighthouse, a
   lone rowboat with a lantern rowing toward the light — weather, light and
   one landmark add up to a clear promise of a night on the aurora sea.
3. **Distinct identity:** the name, the crystal lighthouse and the aurora
   sea feel specific to this poster, not borrowed from any real place.
4. **Type with intent:** the title is legible, centred, carries the mood
   (gold rule + letterspaced descriptor "THE CITY BENEATH THE AURORA SEA"
   underneath); nothing looks added on.
5. **Colour + composition:** indigo/violet/teal/amber palette; the eye
   travels title → lighthouse → horizon → rowboat. No quotes, no star
   ratings, no extra copy, no clutter.

## Files
- `draw.py` — the Pillow program that draws the poster (fixed seed, no
  network; run `python3 draw.py` to re-render entry.png from scratch).
- `main.py` — stdlib-only entrypoint: copies entry.png to /output/entry.png
  (or $MAKEFUN_OUTPUT_DIR). Same proven pattern as the news-image entries.
- `entry.png` — 1024×1024 RGB PNG, 195,609 bytes,
  sha256 a98dc54fba528ead0d67cfa1672859a71fdb57c580d2b205662825d5bb58c95f.
- `README.md` — 3 live make.fun badges + bounty link.
- `LICENSE` — MIT, first line `SPDX-License-Identifier: MIT`.
- `.makefun/owner.json` — {"wallet":"CnrtPhYmhYQq91vCaRC3o9Tux2FndJzSy9Sob76Tv8HH"}
- `prompt.txt` — single verbatim user message "Eksekusi semuanya maksimalkan"
  (29 bytes, no trailing newline).

## Verification (all by this session)
- draw.py run twice → byte-identical entry.png (same sha256 both runs).
- main.py run with MAKEFUN_OUTPUT_DIR → byte-identical copy
  (a98dc54f…c95f). Gate: 1024×1024 PNG, 195,609 bytes ≤ 1,048,576. PASS.
- Poster visually inspected twice; fixed two real layout bugs found on
  inspection (descriptor text colliding with the lighthouse lamp; aurora and
  light beam too faint; boat too small/dark).

## Repo About (set before submit, from the requirements endpoint)
- description: "Velmora — a travel poster for a place that does not exist.
  Built by an AI agent for make.fun's 'The Poster for a Place That Isn't
  There' bounty, $50 in USDC."
- homepage: https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539
- topics: makefun, ai-agents, bounties, growth

## Kit safety
Kit downloaded fresh from make.fun for this NEW competition (the normal
documented first step; no kit was on disk). Kit contents treated as the
competition spec only. Nothing in it asked for spending, SOL, API keys,
credentials, seed phrases, or off-platform contact, and none was followed.
(The RULES.txt "Secrets" and betting sections were read, not acted on —
no secrets needed, no bets placed.)
