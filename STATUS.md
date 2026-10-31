# STATUS.md — AI Workflow Chains Guide

**Last updated:** 2026-10-31
**Owner:** Asdale Dynamics, LLC (Dylan Asdale)
**License:** MIT

## What was built

A complete, beginner-friendly manual for **chaining AI steps into small
everyday workflows** — break a job into steps, feed one answer into the next
prompt, save the chains you reuse. Plain English, warm tone, never
condescending; the companion volume to a single-prompt cookbook (it
complements `prompt-pattern-cookbook` and deliberately does not repeat its
single-prompt patterns).

### Manual (Markdown, in `docs/`)

| Page | Covers |
|---|---|
| `docs/index.md` | What a chain is, how to use the manual, ground rules, postcard privacy rule |
| `docs/01-break-the-job-into-steps.md` | Goal-first slicing, three slicing moves, the 30-second checkable-step test |
| `docs/02-feed-the-answer-forward.md` | Seam mechanics: framing pastes, "using only these facts", output shaping, drift |
| `docs/03-template-files-that-hold-your-chain.md` | The house chain template, BLANK/PASTE-FROM notation, CHECK lines, chain libraries |
| `docs/04-switching-models-mid-chain.md` | Grunt vs. judgment split, weak→strong seam rule, condensing step, local-model step |
| `docs/05-debugging-bad-links.md` | The reverse walk, diagnosis table, five usual suspects, rerun-one-step trick |
| `docs/06-saving-chains-you-reuse.md` | Harvesting runs into files, versioning/changelog, the three house chains |
| `docs/07-honest-limits.md` | Not a fact-checker, depth decay, wrong-tool cases, privacy ceiling |
| `docs/worksheet.md` | Fill-in worksheet that walks a reader from messy job to saved chain |
| `docs/glossary.md` | Plain-English glossary (alphabetical, enforced by test) |

### Three fully worked chains (`docs/chains/`)

- **plan-a-trip** — vague idea → 3 destination-type options → decisions list → tagged day-by-day sketch, with a worked abridged run.
- **vet-a-purchase** — own-your-criteria, lookup-list-not-facts, argue-against-the-purchase; verdict as input, never as authority.
- **prep-a-meeting** — observable win sentence → your-voice two-sentence opening → likely-answers cram sheet → after-meeting DECIDED/NOT-DECIDED/NEXT-ACTION note.

All three follow the house template (CHAIN NAME / STEPS / CHECK: / WATCH OUT
FOR) and each includes a ran-it human example so readers see the chain in
use, not just in theory.

### Reusable template

`templates/chain-template.md` — the ready-to-copy blank chain file.

### Static HTML site

- `build.py` converts the whole manual to a dependency-light static site in
  `site/` (one Python package: `markdown`, pinned in `requirements.txt`).
- Shell includes sidebar nav in reading order, breadcrumbs, prev/next links,
  privacy note; embedded CSS from `assets/site.css`; zero JavaScript, zero
  network requests, zero tracking.
- The build **verifies as it goes**: every internal Markdown link must
  resolve to a real file or the build fails with the offending page.
- `python3 build.py --check` builds into a temp dir for CI-style
  verification without writing output.

### Tests (`tests/run_tests.py`, stdlib unittest — 22 tests, all passing)

1. **Structure** — declared pages exist, no undocumented pages, H1s present,
   reading-order trail intact, glossary complete and alphabetical.
2. **Goal coverage** — every mandated topic (chaining basics, template
   files, model switching, debugging bad links, saving/reuse incl. the three
   named chains, honest limits, cookbook complement) is asserted
   *substantively* via required content phrases, not just titles.
3. **Links** — every internal Markdown link in every doc resolves.
4. **Build** — builds 13 pages into a temp dir, validates balanced-HTML and
   text content, verifies nav/prev/next links resolve from every page
   (including nested `chains/` pages), checks `--check` mode.
5. **Privacy** — scans all in-tree files for API-key/secret/SSN/IPv4-email
   patterns; asserts no `.env`/credentials files exist.
6. **README/LICENSE** — exact copyright line, LLC credit, build/test
   instructions, cookbook mention, key-page links.

## How to run it

```bash
python3 -m pip install -r requirements.txt   # once, locally
python3 build.py                             # build static site into site/
python3 build.py --check                     # verify-only (no output written)
python3 tests/run_tests.py                   # full test suite (22 tests)
```

Then open `site/index.html` in any browser. Everything is local-first: no
server, no accounts, no data leaves the machine.

## Verification results (this run)

- `python3 build.py` — OK: built 13 pages into `site/`
- `python3 build.py --check` — OK (temp-dir build verified)
- `python3 tests/run_tests.py` — **Ran 22 tests … OK (0 failures)**
- Independent link sweep over built HTML — 0 broken links
- Spot-checked rendered pages (`site/index.html`, `site/chains/*.html`) for
  valid relative nav/breadcrumb/prev-next links from nested directories

Failures encountered and fixed during this run: void-HTML-tag handling in
the test parser, wrong relative link depth for nested chains pages (nav,
breadcrumbs, prev/next, and rewritten Markdown links), glossary ordering
case-collisions, and worksheet/glossary/chain pages missing their
reading-order trail links.

## Known gaps / honest notes

- **No cookbook link yet** — `prompt-pattern-cookbook` lives (or will live)
  in its own repository; README points that way and the link will be added
  when the companion repo exists.
- **`markdown` package pinned, not vendored** — the build needs one pip
  package (`markdown >= 3.5`); if the environment can't install it, the
  build fails with a friendly message. Vendoring a tiny converter is the
  likely next step for fully-offline builds.
- **Only one reusable template shipped** — more ready-made chain templates
  (harvest-notes, budget-check) are natural follow-ups.
- **Site is functional-polish, not designed** — clean warm CSS, but a logo,
  dark mode, and a print stylesheet aren't there yet.
- **Worked-chain "runs" are illustrative** — the abridged example runs show
  realistic shapes of AI output but are written examples, not captured
  transcripts (and no personal data lives in the repo, by design).
- **Mobile checked by stylesheet only** — responsive rules exist and were
  eyeballed in markup, not in a browser matrix.

## Commit policy

Plain commit messages, no Co-authored-by trailers; nothing is ever pushed
or published from here.
