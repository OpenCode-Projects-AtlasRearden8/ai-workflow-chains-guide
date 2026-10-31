# Template Files That Hold Your Chain

*Stop re-inventing the chain every time. Write it down, fill in the blanks.*

## Why chains go in files

By now you can wire a chain together live in a chat window. But if the only
copy of your chain lives in a chat history, you've built a sandcastle at
high tide. A chat window is for *running* a chain. A **template file** is for
*keeping* one.

A template file is just a plain text file (or a note on your phone, or a
Google Doc — plain text travels best) that contains:

1. The name of the chain and what it's for.
2. **Steps, in order**, each step written as a prompt with a `[BLANK]` in it.
3. Notes about which blanks get filled from the previous step.
4. Anything to watch out for (where this chain tends to go wrong).

That's it. No app, no code. Here is the house template we use for every chain
in this manual — including the three worked chains later (a ready-to-copy
blank lives at `templates/chain-template.md` in this repository):

## The house chain template

```text
=== CHAIN NAME: [what you call it] ===
WHAT IT'S FOR: [one sentence, in your own words]
WHAT YOU NEED TO START: [inputs you gather before step 1]

--- STEP 1 ---
ASK: "[the prompt, with [BLANK] spots marked]"
CHECK: [how you sanity-check this answer in under 30 seconds]
PASTE INTO: step [N]   (or: end of chain — this is the final answer)

--- STEP 2 ---
ASK: "[the prompt, containing: [PASTE FROM STEP 1]]"
CHECK: [the 30-second check]
PASTE INTO: ...

--- STEP 3 --- ...

--- WATCH OUT FOR ---
[the links that most often go bad, and what a bad link looks like]
```

Two naming conventions do all the work:

- **`[BLANK]`** — you supply this before the chain starts (a date, a product
  link, a meeting topic).
- **`[PASTE FROM STEP N]`** — mark the exact spot where the previous step's
  answer goes.

When you run the chain, you find-and-replace blanks with real text. That's the
whole "technology." It works in a notes app, a text editor, or printed on
paper with a pen — which, for a tired brain, is a feature.

## The CHECK line is not optional

Every step in the template has a `CHECK:` line, and the template refuses to
work without it. Why: when you run a chain you're not just passing answers
forward, you're **vouching** for them. The CHECK line is your vouching
ritual — the 30-second test from chapter 1, written down while you're fresh,
to follow when you're tired.

Write checks as questions you can actually answer:

- ❌ `CHECK: make sure it's good` (vague — can't be done in 30 seconds)
- ✅ `CHECK: are all five criteria actually about vetting a *tool*, not likes?`

## Keeping a chain library

Once you have a template, saving chains becomes a one-folder job:

```text
my-chains/
  plan-a-trip.md
  vet-a-purchase.md
  prep-a-meeting.md
  harvest-note-template.md
```

Each file uses the house template. When a run teaches you something (step 3
kept ignoring your budget — add "under $X" to the prompt), you *edit the
file*, not just that run. Your chains get better after every use. That's the
quiet payoff: a chain is **a document you maintain**, so every run either
outputs your answer or improves the tool.

## Anatomy of a saved chain, line by line

Let's look at one real step from the vet-a-purchase chain (full version in
the chains section):

```text
--- STEP 2 ---
ASK: "Here are the 6 criteria I care about for buying [BLANK: item]:
        [PASTE FROM STEP 1]
      Score how reliable this specific seller seems: [BLANK: seller link
      or screenshots]. Score each criterion 1–5, no total score."
CHECK: no criterion is silently dropped; scores come with one-line reasons
PASTE INTO: step 3
```

Read what this one step encodes: the instructions, the seams (paste-from
marks), the inputs you must gather (seller link), the format boundary ("no
total score" — a guard against the AI inventing certainty), and the check.
A step that fits in ten lines can carry all of that. Small steps, big notes.

## Where to next

One chain, one good model — that's most small jobs. But sometimes the middle
of a chain needs a different *kind* of brain than the start. Next chapter:
switching models mid-chain without breaking it.

[Next: Switching models mid-chain →](04-switching-models-mid-chain.md)
