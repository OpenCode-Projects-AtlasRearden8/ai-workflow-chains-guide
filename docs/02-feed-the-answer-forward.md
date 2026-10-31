# Feed the Answer Forward

*How one answer becomes the next prompt — the actual mechanics.*

## The one move this manual is named for

Every chapter so far was build-up. Here is the move itself, in its raw form:

```text
You (step 2):  "Using exactly this: [paste step 1's answer] —
                now do the next thing."
```

That's all. The answer from the previous step goes into the new prompt, framed
as material to work from rather than something the AI should "remember."

Why paste it in explicitly, when many chat apps keep conversation history?
Three reasons:

1. **Chains outlive chats.** A saved chain is a set of prompts that works in
   any tool, any window, any day. If it depends on chat memory, it isn't saved.
2. **Memory is fuzzy; text is exact.** Models drift around long conversations.
   The exact pasted text is the one thing the model can't misremember.
3. **You can edit the seam.** When a chain goes wrong (chapter on debugging),
   90% of fixes happen at the seam — the pasted text. You can fix text. You
   can't fix memory.

## The vocabulary: upstream and downstream

- **Upstream** step: the one that *produces* the answer.
- **Downstream** step: the one that *consumes* it.

When a chain goes bad, you ask: which seam broke — did an upstream step make
bad material, or did a downstream step misunderstand good material?

## Three rules for clean seams

### Rule 1: Frame the paste, don't just dump it

Bad seam:

```text
"cheap flights denver→nashville early november nonstop alaska $214 spirit
$178 one stop 5h40 ... now which one should I get"
```

Good seam:

```text
"Here are the flight options I found, as notes:
   — [paste your step-1 answer]
Using only these facts, tell me which option best balances price vs.
total travel time, and say why in 2 sentences."
```

The framing line ("Here are the flight options I found, as notes:") tells the
model what the pasted text *is*. Unframed pastes read like noise, and models
guess at what noise means. Guessing is where chains rot.

### Rule 2: Bound the context — "using only this"

Notice "Using only these facts." Chats carry history, and a downstream step
will happily blend old conversation into your clean answer. The phrase
"using only / using exactly this" is a cheap, effective fence. Use it
whenever the step should work just from the paste.

### Rule 3: Ask for output in the shape the next step needs

Each step serves the next one. If step 3 needs criteria, step 2 should emit
*criteria as a short list*, not an essay. If step 3 will quote it, ask for
the exact wording. A one-line habit fixes this: end each prompt with —

```text
"Format: [bullet list / one sentence / a table with columns X and Y]."
```

(A full treatment of output formatting lives in the prompt-pattern-cookbook;
here we only need the habit, not the theory.)

## The relay race picture

Think of a chain as a relay where each runner hands over a **written note**,
not a memory. Step 2 never "trusts" that step 1 said something — step 2 gets
a piece of paper, reads it, adds to it, and writes the next note. The baton
always has writing on it. If a handoff produces a blank or garbled note,
you've found your bad link — that's the next-next chapter's subject.

## Avoiding drift: quotes over paraphrase

Long chains have a game of telephone problem: each retelling of earlier
material loses a little. Two defenses:

1. **Quote exactly.** Where a downstream step needs earlier wording, copy the
   text verbatim, don't retype what you vaguely remember.
2. **Resummarize deliberately.** If material has grown too long to paste
   whole (rule of thumb: more than about one screen), that's its own step:
   *"Summarize all of the following into 5 bullet points that keep every
   decision with its reason: [paste]. The next step will use only your
   summary."* Now the summary is a checked, pasted artifact — intentional,
   not drift.

## Worked micro-example

Job: choose a name for a small newsletter.

```text
Step 1: "Brainstorm 12 names for a friendly newsletter about practical
         AI tips for beginners. No explanations, just names."
         → (you delete three that feel off, keep nine)

Step 2: "Here are the surviving name candidates:
   — [paste the 9 names]
Acting as a picky first-time reader with 3 seconds' attention, rank the
top 3 and say in one line each what a new reader might *assume* the
newsletter is about from the name alone."

Step 3: "The top 3 were: [paste]. The top pick was [X]. Write the first
         40 words of a welcome email that matches what the name
         promises. Warm tone, no jargon."
```

Between each prompt, the human does real work: deleting names, checking that
the "assumptions" in step 2 sound right. The chain moves; you steer.

## Where to next

You can now slice a job and wire it together. Next: stop holding chains in
your head — put them in **template files** you can reopen any week.

[Next: Template files that hold your chain →](03-template-files-that-hold-your-chain.md)
