# Switching Models Mid-Chain

*Different steps need different brains — here's how to swap without breaking the seams.*

## Why switch at all

Chains make model-switching *natural*, because every step is a separate
prompt you paste text into. Nothing stops you from running steps 1–2 in a
chat on your phone and step 3 in a heavyweight model on your laptop.

The common reasons people switch mid-chain:

- **Cost or limits.** A cheap or free model does fine on grunt work; you
  spend your better (scarcer) model on the judgment steps.
- **Different strengths.** Some models are good at drafting prose, some at
  strict lists and exact instructions, some at long reasoning.
- **Privacy.** You might want a sensitive step done in a *local* model on
  your own machine and the mundane steps in a cloud chat. (Ground rules
  still apply: sensitive content stays out of prompts everywhere.)
- **Availability.** A rate limit or outage hit mid-chain; a smaller model can
  at least keep the chain moving.

## The rule of thumb: grunt vs. judgment

The cheapest useful split, which covers most small jobs:

| Step type | Examples | Model posture |
|---|---|---|
| **Grunt work** | brainstorming 12 names, listing criteria, grouping a messy pile, formatting | cheap / fast / local is fine |
| **Judgment work** | weighing options, deciding what to drop, writing the final words, spotting what's missing | your best available model |

So for a chain like vet-a-purchase: a free model can gather criteria and
extract specs, and you might want the *comparison verdict* step run on the
strongest model you can access. Same chain, two postures.

## What switching actually costs: seam risk

Here's the catch, stated honestly. Seam-friendliness depends on the **text
you pass**, and the text you pass gets produced by the *upstream* model.

- A weak model's output read by a strong model usually works fine: strong
  models are good at reading messy-but-short material.
- A strong model's elaborate output read by a weak model can fail: weak
  models lose threads in long, dense text.

So the safe direction of travel is **weak → strong** or **equal → equal**.
Switching **strong → weak** mid-chain is where chains snap — if you must go
that way, add a condensing step first.

## The condensing step: when you must downgrade

Before handing rich material from a big model to a small one, insert one step
(run on either model, ideally the *small* one so it proves the text is small-
model-proof):

```text
"Reduce everything below into compact notes the next step will work from:
   — [paste upstream answer]
Rules: keep every decision and its reason; drop pleasantries and general
advice; under 150 words; plain bullet list."
```

Now the downstream small model gets tight notes instead of an essay. This one
pattern fixes more strong→weak handoffs than any amount of re-prompting.

## Practical switching recipes

**Recipe A — "run the chain on whatever's available."** Since the chain is a
template file (previous chapter), *the file records which model each step
used*, like this:

```text
--- STEP 2 --- (model: free chat app, works fine)
ASK: "..."
```

The first time you run a chain, note which model ran each step and how the
steps felt. After two runs you'll know exactly which steps earn the upgrade —
and the file remembers for you.

**Recipe B — "the same chain, two postures."** Mark steps as `ANY` (any model
does) or `STRONG` (worth the good model) in the template. Then on a
low-battery, low-patience day, you run only the `ANY` steps and stop — the
chain file tells you where halfway looks like.

**Recipe C — "private step, local model."** If one step handles material
you'd rather not send anywhere (say, tidying a list of your own expenses),
swap in a locally-run model for that step only, and treat its answer like any
other: read it, check it, paste it forward. The chain doesn't care where a
step ran — it only cares about the text going through the seam.

## A short self-test that catches bad handoffs

Whenever you switch models across a seam, spend 20 seconds asking the
*downstream* model one question:

```text
"Before answering, restate in one sentence what the pasted notes above are,
and list any part you find ambiguous."
```

If its restatement is wrong or it flags ambiguity, the seam is broken — fix
the paste (e.g., run the condensing step) before letting it answer the real
question. This costs almost nothing and catches most switching failures
before they poison the chain.

## Where to next

Chains will still break — sometimes because of switching, usually for more
ordinary reasons. Next chapter: finding and fixing a bad link without
starting over.

[Next: Debugging bad links →](05-debugging-bad-links.md)
