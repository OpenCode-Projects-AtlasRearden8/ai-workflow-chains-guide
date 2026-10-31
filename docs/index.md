# AI Workflow Chains: A Friendly Manual

*A plain-English guide to linking AI steps together for everyday jobs.*

## Who this is for

If you've ever typed a prompt into an AI chat, you already know more than you
think. This manual teaches the next small step up: **chaining** — instead of
asking an AI one big question, you break the job into a few small questions,
and each answer feeds into the next question.

That's it. That's the whole trick. Everything else in this manual is how to do
it without making a mess.

You don't need to code. You don't need an account anywhere special. You don't
need to memorize anything. If you can copy and paste, you can run a chain.

## What you'll learn

- **Break a job into steps** — and know how small is small enough.
- **Feed one answer into the next prompt** — the actual copy-paste mechanics.
- **Template files that hold your chain** — so a chain survives past Tuesday.
- **When to switch models mid-chain** — cheap model for grunt work, strong
  model for judgment calls.
- **Debugging bad links** — when step 3 output looks like garbage, find the leak.
- **Saving chains you reuse** — with three fully worked examples:
  *plan-a-trip*, *vet-a-purchase*, and *prep-a-meeting*.
- **Honest limits** — what chaining can't fix, and when you should stop.

## How to read this manual

Read the chapters in order the first time. After that, each chapter stands on
its own, so you can jump straight to what you need.

| If you want to... | Read |
|---|---|
| Understand the basic idea | [Break the job into steps](01-break-the-job-into-steps.md) |
| Wire answers together | [Feed the answer forward](02-feed-the-answer-forward.md) |
| Save a chain to a file | [Template files that hold your chain](03-template-files-that-hold-your-chain.md) |
| Use different AIs for different steps | [Switching models mid-chain](04-switching-models-mid-chain.md) |
| Fix a chain that's gone wrong | [Debugging bad links](05-debugging-bad-links.md) |
| Keep chains for later | [Saving chains you reuse](06-saving-chains-you-reuse.md) |
| Know the downsides | [Honest limits](07-honest-limits.md) |
| Write your own first chain | [The chain worksheet](worksheet.md) |
| Look up a word | [Glossary](glossary.md) |
| Run a finished chain today | [plan-a-trip](chains/plan-a-trip.md), [vet-a-purchase](chains/vet-a-purchase.md), [prep-a-meeting](chains/prep-a-meeting.md) |

## Where this fits with the prompt-pattern-cookbook

This manual is the companion to the **prompt-pattern-cookbook**. The cookbook
is about **single prompts** — making one question to an AI as good as it can
be. This manual is about **strings of prompts** — taking good prompts and
linking them end to end.

We deliberately don't repeat the cookbook's patterns here. When a single step
of a chain would benefit from a prompt technique (like asking for a specific
format), we point you that way instead of re-explaining. A chain of weak
prompts is still a weak chain — the chapters here assume each link *starts*
reasonable, and focus on what happens **between** links.

## What a chain actually looks like

A chain is just three honest questions asked in order:

```text
Step 1: "Here's my messy thought: [paste]. In one sentence, what am I
         actually trying to do?"

Step 2: "The goal is: [Step 1's answer]. List the 5 decisions I'd need
         to make. One line each."

Step 3: "The decisions are: [Step 2's answer]. For decision 1 only,
         give me 3 practical options with pros and cons."
```

Notice what's happening: each step is *easy* for the AI, because it's only
doing one thing. And each step is easy for *you* to check, because one short
answer is easy to read and sanity-check. That's the quiet superpower of
chains: **small steps are checkable steps.**

## Two ground rules before we start

1. **You are the editor, not the stenographer.** Every answer the AI gives
   gets read by you before it goes into the next prompt. If you wouldn't
   repeat it to a friend, don't feed it to the next step.
2. **Local-first, privacy-first.** We treat AI chats like postcards, not
   sealed letters: assume anything you paste could be seen. Personal details,
   medical info, passwords, and anything you'd be embarrassed to have read
   back to you don't go into prompts. We'll remind you of this where it
   matters, because it always matters.

Ready? The next chapter starts with the skill everything else builds on:
knowing how to slice a job into steps that are the right size.

[Next: Break the job into steps →](01-break-the-job-into-steps.md)
