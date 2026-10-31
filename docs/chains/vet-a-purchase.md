# Worked Chain: vet-a-purchase

*For any "should I buy this?" that's big enough to think about. Built to talk you out of it first.*

A complete, copy-and-run chain — the one most people keep. Its design rule:
**facts before feelings, and the case against before the case for.** Privacy
note as always: product names and prices are fine; your finances, address,
and account details are not.

```text
=== CHAIN NAME: vet-a-purchase ===
WHAT IT'S FOR: turning "should I buy [thing]?" into criteria I chose,
               facts I gathered myself, and an honest yes/no.
WHAT YOU NEED TO START: the item; one line on why you want it; raw
               material you pasted from real sources (a review, the
               seller page, a forum thread) or summarize-in-your-own-
               words notes about it.

--- STEP 1 ---  (model: any)
ASK: "I'm thinking about buying: [BLANK: item] . My cold reason:
      '[BLANK: e.g. 'my current one takes 40 min to commute instead of 15']'.
      Before ANY talk of the product itself: help me write 5 checkable
      criteria for whether this purchase succeeds. Format: criterion —
      how I'd know in a month if it passed or failed."
CHECK: do the criteria test *outcomes*, not specs? 'Under $400' might
      be one; 'is highly rated' is not — that's popularity, not outcome.
PASTE INTO: step 2

--- STEP 2 ---  (model: any)
ASK: "Here are the 5 success criteria: [PASTE FROM STEP 1]
      For each criterion, tell me what FACT I should check about this
      specific product and where I'd realistically find it (a spec
      page, a manual, a return policy, a forum). Do NOT invent the
      facts — list what to look up. Format: bullet per criterion."
CHECK: nothing invented? Any bullet claiming a spec/price/rating is a
      red flag — strike it and ask for the lookup source only.
PASTE INTO: step 3's note section (you'll fill the answers yourself)

--- STEP 3 ---  (model: your best available)
ASK: "Here are the criteria and the facts I gathered on my own:
      [BLANK/not-verified notes: [BLANK: your gathered facts]]
      First, argue AGAINST the purchase: using only my notes, name the
      2 strongest reasons not to buy, each tied to a criterion.
      Second, only if it survives that: score each criterion pass/
      borderline/fail with one line of reason. End with: buy, wait, or
      skip — and the one thing I should verify myself before paying."
CHECK: does it cite only your pasted facts? Any confident number or
      claim you didn't paste means the fence failed — rerun with
      'using only these facts' leading the prompt.
PASTE INTO: end of chain — verdict material, not the verdict itself

--- WATCH OUT FOR ---
- The verdict is input to YOUR decision, never the decision (honest-limits
  chapter). A chain can talk you out of a bad buy brilliantly — and it is
  not a warranty for a good one.
- Invented specs are the #1 bad link here. The fix is always Rule 2:
  'Using only these facts.'
- If you have no gathered facts yet, stop after step 2 and go gather —
  running step 3 on vibes defeats the whole design.
- Runs fine entirely on a free model; upgrade only if step 3 feels
  mushy on your material.
```

## How it uses the manual's moves

- **Criteria before product:** step 1 makes *you* define success before any
  spec-sheet seduction — gather-then-shape with the gathering done by hand.
- **Facts from sources, not the model:** step 2 is a lookup list, not an
  answer sheet — the anti-hallucination spine of this chain.
- **Draft-then-check, in position:** step 3 argues *against* before scoring —
  the chain's picky-editor move, pointed at your wallet.

## A worked run, abridged

Item: a $230 cordless vacuum to replace a corded one "because the cord
drives me nuts."

- **Step 1 criteria** (after editing): under $250 all-in; battery covers
  the whole apartment in one charge; *I use it 4+ times in the first
  month*; returns accepted locally; no proprietary-battery lock-in.
- **Step 2 lookup list:** return window on the seller's page; runtime at
  real suction vs. eco; whether the battery is a standard pack; what
  owners say at month twelve (search one owner-forum thread).
- **Facts gathered by hand:** runtime 22 min at full suction vs. 44 eco;
  battery proprietary ($65 spare in a year, probably); returns fine.
- **Step 3's against-case:** "your criteria say floor-plan coverage in one
  charge — 22 minutes at real suction fails that for your layout; the
  $230 becomes $295 if the pattern of lock-in batteries holds." Verdict:
  **wait** — with one verify-yourself item: measure the apartment's
  continuous vacuuming time (it's 9 minutes, it turns out).
- Outcome: not bought now; the ticket to revisit in six months is saved.
  That is a chain working exactly as designed.

When you do buy (or skip), save the file with your criteria — your own
worded success-criteria turn out to be reusable for *next* year's purchase
of the same category, and that's when the chain file starts paying rent.

[Next: prep-a-meeting →](prep-a-meeting.md)
