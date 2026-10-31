# Break the Job into Steps

*The first chain skill: slicing, not solving.*

## Why step one of every chain is your own thinking

Chains fail for one reason far more than any other: the **first step wasn't
small**. People hand the AI a task like "plan my retirement" or "fix my resume"
and then wonder why the answer is generic. Big questions get generic answers,
chained or not — chaining just makes the genericness compound.

So before any chain exists, you slice the job. Here's the test we'll use all
through this manual:

> **A step is the right size when you can check the answer to it in under
> thirty seconds.**

Not "agree with it." Just *check* it — read it and go "yes, that's roughly
right" or "nope, back up." Checking is fast. Solving is slow. Every slice in
your chain should be a checkable slice.

## The three slicing moves

Most jobs break down with one of three moves. You rarely need more.

### Move 1: Goal-first (distill, then decide)

**Idea:** first ask the AI to help you *state* the problem, then work on the
stated version.

```text
Step 1: "Here's my messy brain-dump: [paste]. In one or two sentences,
         what am I actually trying to decide or do?"
Step 2: "The goal is: [answer]. What are the 3–5 decisions or pieces
         I'd need to handle? One line each."
Step 3+: one step per piece, taken one at a time.
```

Good for: anything where you started confused. Which is most things.

### Move 2: Draft-then-check (separate making from judging)

**Idea:** ask for the thing, then ask a *second* question to critique the
first answer — as if a different, pickier person wrote it.

```text
Step 1: "Write a first draft of [thing]."
Step 2: "You're a skeptical editor. Here's the draft: [paste].
         List its 3 weakest points."
Step 3: "Revise the draft to fix those points: [paste draft + points]."
```

Good for: writing, plans, comparisons — anything where the first version is
"fine" but you know in your gut it isn't done.

### Move 3: Gather-then-shape (get raw material, then organize it)

**Idea:** first ask for a *list* (facts, options, criteria), then ask for the
*judgment* built on that list.

```text
Step 1: "What 6–8 questions should I ask to evaluate [thing]? List only."
Step 2: "Using those questions: [paste], now compare [A] and [B] honestly."
```

Good for: research-ish jobs, vetting purchases, prep work. Notice step 1 asks
for *no opinions* — that's deliberate. Mixing "collect facts" and "judge
facts" in one prompt gets you mushy output.

## How small is small enough?

A good step:

- Asks for **one** kind of output (a list, a draft, a decision — not all three).
- Can be **answered in a couple of sentences to a page**, not a report.
- Has an answer you can **check without expert knowledge** (or at least know
  whether it *sounds* sane).

A too-big step usually contains a hidden "and". "Plan my trip **and** stay in
budget **and** keep my kid entertained" is three jobs. Slice along the "and"s.

## Walkthrough: slicing a real job

Job: *"I need to get my school paperwork sorted this week and I keep putting
it off."* (ADHD-friendly note: we slice so tiny you can start while tired.)

```text
Slice 1: What paperwork? — "Here's the pile of stuff I mentioned:
          [describe]. Group this into simple buckets like 'needs a
          signature', 'needs a call', 'can wait'."   ← checkable ✓

Slice 2: Which bucket first? — "Here are the buckets: [paste].
          Which single one would make the rest of the week easier?
          Defend it in 2 sentences."                        ← checkable ✓

Slice 3: First action only. — "For [chosen bucket] only, give me the
          literal first 3 actions, in the order I'd do them, with
          phone numbers/websites where I'd find them."      ← checkable ✓
```

That's a real chain — three small questions, each answer pasted into the
next. And notice Slice 3 says "the literal first 3 actions." Small-step
thinking loves concrete over abstract, first over fifth.

## The one habit to keep

After slicing, **say the chain out loud in one breath**: "First I ask for the
buckets, then I ask which bucket, then I ask for first actions." If you
can't say it in one breath, you've sliced too fine — merge two steps.

## Where to next

Slicing gets you the steps. The next chapter is the mechanical part: how the
answer from step 1 physically becomes part of the prompt in step 2 — the
copy-paste move that makes it a *chain* and not just three questions.

[Next: Feed the answer forward →](02-feed-the-answer-forward.md)
