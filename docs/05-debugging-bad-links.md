# Debugging Bad Links

*When a chain goes wrong, find the broken seam instead of starting over.*

## The first rule: don't restart the chain

Your instinct when a chain produces nonsense is to go back to step 1 with a
better prompt and run everything again. Resist. Chains are short, and their
steps are checkable — which means when something's wrong, the wrongness is
*findable*. A chain isn't a black box; it's a line of labeled jars. You just
taste-test backwards until you find the bad batch.

## The reverse walk: find the earliest sane answer

Debug a chain by walking **backwards** from the failure:

```text
Step 4's answer is garbage
  → Read step 4's INPUT (what step 3 produced).
    Is step 3's answer sane?
      NO  → the broken link is the 2–3 seam. Fix step 3 or its input.
      YES → the problem is step 4's prompt itself.
```

Keep walking back until you find the **earliest answer that's still sane**.
The broken link is always the seam at or just after that point. This is why
chapter 1 insisted steps be checkable in thirty seconds — checkable steps
make the reverse walk take minutes, not evenings.

The diagnosis table that handles 90% of bad chains:

| Symptom at a seam | Usual cause | Usual fix |
|---|---|---|
| Downstream answer ignores part of the paste | Unframed or unlabeled paste | Add a framing line: "Here is the [X] as notes:" |
| Downstream invents facts not in the paste | The paste is thin or the prompt invites elaboration | Add "Using only these facts" (chapter 2, Rule 2) |
| Downstream answer is mushy, hedges everything | Upstream answer was mushy | Fix upstream: ask for lists/choices, not opinions |
| Downstream misses the point entirely | Paste is too long/dense for the model | Run the condensing step (chapter 4) |
| Same bad step, fresh prompt, still bad | The *task* isn't sliced small enough | Re-slice: split the step along its "and"s |

## The five usual suspects

In order of how often they're guilty:

1. **Step 1 was too big.** The classic. The fix isn't a better prompt — it's
   re-slicing (chapter 1). If step 1's answer is generic, every downstream
   step polishes genericness.
2. **An unframed paste.** The downstream model guessed what your paste was.
   Fix: label the material ("Here are the flights I found, as notes:").
3. **No output shape.** A downstream step needed a list and got prose. Fix:
   "Format: bullet list, one item per criterion."
4. **Scope creep.** The paste carries leftovers from earlier conversation,
   and the model blends them in. Fix: "Using only what's pasted here."
5. **A step was too big.** Mid-chain this looks like "step 3 gave a summary
   that's somehow also a plan and also advice." Same cure as #1 — split it.

## The rerun-one-step trick

Since every step is an independent prompt, you can rerun a single step in
isolation. Take the *exact same input* (copy it verbatim) and either:

- rerun it in a **fresh chat** (no history — proves whether the step is
  worded well or was poisoned by conversation context), or
- rerun it with the paste **condensed first** (proves whether the seam was
  too heavy for the model).

Two isolated reruns tell you which of those it is — no guessing. This is the
whole debugging method for model-switch bugs, and it's nearly free.

## The tape trick: label your runs

When running a chain live, keep a plain running log in your notes file:

```text
[step2 output] ...looks fine, but it dropped the budget criterion
```

Three lines of notes per run gives you a next run that starts already
debugged — and when you save the chain template afterward, those notes become
the `WATCH OUT FOR` section (chapter 3). Debugging experience converts into
chain maintenance. That's the compounding trick the whole manual hangs on.

## When a chain is broken on purpose

One honest exception: sometimes the chain is working fine and the *answer*
is bad — because the real problem wasn't checkable (chapter 1's bar). Eg: "is
this stock a good buy" can be sliced and chained all day and remain a bad
question for a text model. That's not a broken link; that's the honest-limits
chapter's territory, and it deserves the next chapter's full attention.

[Next: Saving chains you reuse →](06-saving-chains-you-reuse.md)
