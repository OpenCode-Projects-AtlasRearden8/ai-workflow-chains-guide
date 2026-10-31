# Glossary

*Plain-English definitions, in the order you'd meet them. No exam.*

A chain is just words doing jobs, so the vocabulary is small. These are the
words this manual uses, and what they mean when *we* say them.

**Blank** — a `[BLANK]` in a saved chain template: a spot you fill in before
running, e.g. the item you're vetting or the meeting's topic. The chain's
only required typing.

**Chain** — a sequence of AI prompts where each step's answer feeds into the
next step's prompt. The manual's whole subject. See also: chain file,
seam.

**Chain file (template)** — a plain text file holding a chain as reusable
prompts with blanks and paste-marks. What you harvest after a good run.
American recipe-card energy; yours to photocopy.

**CHECK line** — the one-line sanity question attached to each step of a
saved chain: the 30-second test you promised, in writing, for tired-future-you.

**Condensing step** — an inserted step that shrinks rich upstream output into
compact notes before a smaller model continues. The standard fix for
strong→weak model switches.

**Context** — everything the model can "see" when answering: your prompt,
pasted material, and often the surrounding chat history. "Using only these
facts" exists because context is often *bigger* than you intend.

**Drift** — slow decay of meaning across handoffs, like the children's game
telephone. Fought with verbatim quotes and deliberate summaries.

**Handoff / hand-over** — the moment step N's answer becomes part of step
N+1's prompt. Where attention is needed. Not a ceremony; a piece of paper.

**Judgment work** — chain steps needing weighing, choosing, or final wording:
the steps that earn your best model.

**Link** — one step plus its seam; the unit of a chain. A "bad link" is a
step or seam that made the next answer worse — the debugging chapter's prey.

**Local model / local step** — a model running on your own machine. Useful
for a step handling material you'd rather not send anywhere. The chain
doesn't care where a step ran; it cares about the text through the seam.

**Paste** — copying upstream text into a downstream prompt, with framing
("Here are the notes:") and bounds ("using only these facts"). The chain's
engine; where fixes happen.

**Prompt** — one instruction-plus-material message to an AI. The atom of the
manual. Single-prompt craft is the prompt-pattern-cookbook's territory; this
manual assumes each step's prompt starts reasonable.

**Reverse walk** — debugging method: from the bad answer, walk backwards
reading inputs until the earliest sane answer; the first seam after it is
the broken link.

**Seam** — the joint between two steps: exactly where one answer becomes the
next stage's input. Chains are only as strong as their seams; 90% of fixes
happen here.

**Seed** — the messy first statement of a job before goal-first slicing: a
brain-dump that *step 0* turns into a proper goal.

**Slice** — one right-sized piece of a job: one kind of output, answerable
in a page or less, checkable in 30 seconds.

**Step** — one prompt in a chain, upstream or downstream relative to others.

**Upstream / downstream** — relative direction on a chain: upstream produces
the answer, downstream consumes it. Water flows downhill; mistakes do too.

**Versioning** — editing the chain file after runs (with a small changelog)
so each run's lessons collect in the tool.

**WATCH OUT FOR** — the section at the end of a saved chain noting which
seams tend to go bad and what that looks like. Built from run notes.

Words used. Next up are the chains themselves — see all three in action.

[Next: the worked chains →](chains/plan-a-trip.md)
