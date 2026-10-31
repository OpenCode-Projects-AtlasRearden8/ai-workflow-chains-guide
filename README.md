# AI Workflow Chains Guide

*A beginner-friendly manual for chaining AI steps into small everyday workflows.*

By **Asdale Dynamics, LLC** — the home of AI explained "like a friend would."

One big prompt asks too much. This manual teaches the smaller, calmer skill:
**break a job into steps, feed one answer into the next prompt, and check as
you go.** No code, no jargon, no accounts to sign up for — just plain-English
mechanics for making AI useful for the jobs that arrive on an ordinary day:
planning a trip, vetting a purchase, walking into a meeting not-nervous.

## What's inside

The manual lives in [`docs/`](docs/) as Markdown and builds into a static
HTML site via [`build.py`](build.py):

| Chapter | What it covers |
|---|---|
| [Start here](docs/index.md) | What a chain is, how to use this manual, two ground rules |
| [Break the job into steps](docs/01-break-the-job-into-steps.md) | Slicing jobs so each step is checkable in 30 seconds |
| [Feed the answer forward](docs/02-feed-the-answer-forward.md) | The copy-paste mechanics of chains: framing, bounding, shaping |
| [Template files that hold your chain](docs/03-template-files-that-hold-your-chain.md) | The house chain template, CHECK lines, a chain library |
| [Switching models mid-chain](docs/04-switching-models-mid-chain.md) | Grunt work vs. judgment work, condensing steps, a local step |
| [Debugging bad links](docs/05-debugging-bad-links.md) | The reverse walk, the five usual suspects, rerun-one-step |
| [Saving chains you reuse](docs/06-saving-chains-you-reuse.md) | Harvesting runs into files, versioning, and the three house chains |
| [Honest limits](docs/07-honest-limits.md) | What chaining can't do — said plainly |
| [Worksheet](docs/worksheet.md) | Fill-in worksheet for building your first chain |
| [Glossary](docs/glossary.md) | Every term in plain English |

**Three fully worked chains** (the kind you save and reuse):

- [plan-a-trip](docs/chains/plan-a-trip.md) — from a vague idea to bookable decisions.
- [vet-a-purchase](docs/chains/vet-a-purchase.md) — facts before feelings; built to talk you out of bad buys.
- [prep-a-meeting](docs/chains/prep-a-meeting.md) — two sentences and a question list the night before.

A ready-to-copy blank for your own chains is at
[`templates/chain-template.md`](templates/chain-template.md).

## This pairs with prompt-pattern-cookbook

The **prompt-pattern-cookbook** makes one prompt as good as it can be. This
manual makes *strings* of good prompts work together, and deliberately
doesn't repeat the cookbook's single-prompt patterns — chains and single
prompts are different skills for different-sized jobs. (When the cookbook
companion lands in its own repository, the link will be added here.)

## Build the site

The HTML site is generated — nothing to install globally, no network needed
beyond one Python package:

```bash
python3 -m pip install -r requirements.txt   # once, locally (markdown >= 3.5)
python3 build.py                             # writes the static site to site/
```

Then open `site/index.html` in any browser. Everything is plain static HTML —
no server, no JavaScript, no tracking, no external requests.

## Run the tests

```bash
python3 tests/run_tests.py
```

The test suite checks the manual's structure, verifies every internal link
resolves, builds the site fresh into a temp directory, and scans that no
secrets, keys, or personal-data patterns ever made it into the docs.

## Privacy, plainly

Everything here runs locally and ships no data anywhere. The manual's own
advice treats AI chats like postcards: personal details, credentials, health
information, and anything about other people by name never go into prompts,
chained or not. There are no API keys, no telemetry, and no accounts involved
in building or reading this site.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.

## About the author

**Asdale Dynamics, LLC** publishes beginner-friendly AI education from Dylan
Asdale — a registered nurse turned AI author — including *The Massive AI
Manual* and the hub at dylanasdale.github.io. The style is the same
everywhere: plain English, step by step, never condescending, local-first,
and honest about the limits.
