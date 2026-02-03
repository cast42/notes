# The creator of Clawd: “I ship code I don’t read” — notes

Source (YouTube): https://www.youtube.com/watch?v=8lF7HmQ_RgY
Channel: The Pragmatic Engineer
Guest: Peter Steinberger (aka @steipete)
Length: 1:54:04

## What stuck with me

- **Closing the loop** (agent must be able to run/verify/debug its own work)
- **Gating** (a local “full gate” before merge: build + lint + tests)
- **Weaving the code** (integrating features into existing architecture, sometimes reshaping the architecture to fit)
- **PRs are “prompt requests”** (and prompts can be higher-signal than the diff)
- **Build open source to learn by doing** (and to demonstrate you can work this way)
- **Codex > Claude Code** for complex codebases (slower, reads more, better system integration)

---

## Who Peter is (life story, as told in the episode)

This is a rough timeline based on what Peter says in the interview (timestamps from the YouTube transcript UI).

- **Rural Austria, early tinkering**: got hooked on computers as a teenager and kept building/experimenting.  
  Timestamp: ~00:02:01+

- **Working while studying**: describes coming from a poor family and needing to finance his studies via work; early professional experience included Microsoft MFC nightmares and quietly switching stacks when needed.  
  Timestamp: ~00:03:13–00:04:25

- **Early iPhone moment (“it clicked”) → building apps**: a frustration with a web experience on the iPhone pushes him to download Xcode and build.  
  Timestamp: ~00:04:43–00:06:10

- **First commercial success**: he ships an app, charges for it, and makes meaningful money quickly (“$10k in the first month”).  
  Timestamp: ~00:07:10

- **PSPDFKit origin story**: after other work/freelancing, he gets pulled into a magazine/iPad PDF-viewer problem, rewrites it, and extracts the PDF component as a product.  
  Timestamp: ~00:09:40–00:12:25

- **Scaling PSPDFKit**: he builds and scales PSPDFKit into a serious developer-tools business. The episode discusses product taste/polish, tech stack, pricing, writing, and culture.  
  Timestamp: ~00:19:14 onward

- **Burnout + stepping away**: he describes burning too hard, CEO stress, and needing time to decompress, including long stretches not turning on a computer.  
  Timestamp: ~00:29:42–00:34:54

- **Return to building, now centered on LLMs/agents**: comes back and sees AI as “good enough to see the potential,” then goes all-in on agentic workflows.  
  Timestamp: ~00:34:54–00:49:10

---

## The core idea: “close the loop”

Peter keeps returning to a simple requirement: agents are effective when the work product can be validated quickly.

- **What it means**: if the agent can compile, run tests, lint, and observe failures, it can iterate toward correct behavior.
- **Why it matters**: without fast feedback, agent output becomes “vibe coding” and you end up manually patching and steering.

Key quote (approx):
- “*The good thing how to be effective with coding agent is always like you have to close the loop. It needs to be able to debug and test itself.*”  
  Timestamp: ~00:57:31–00:57:38

Peter points out why code is a sweet spot for LLMs: validation is cheap relative to other domains.

---

## Gating: local “full gate” as the merge filter

Instead of waiting on slow remote CI, Peter emphasizes a local gate that runs quickly and is directly tied to the agent’s work.

- In the transcript he calls out a “gate” / “full gate” concept as: lint + build + tests.
- The practical effect: merge fast, accept that main may “slip” sometimes, but keep the loop tight.

Key quote (approx):
- “*Full gate is like linting and building and and checking and running all the tests.*”  
  Timestamp: ~01:39:34–01:39:40

---

## Weaving the code (and “builder” mindset)

A repeated theme: Peter doesn’t obsess over each line; he obsesses over the system.

- He describes much of application code as “boring plumbing,” where the real leverage is in architecture.
- He uses the phrase **“weave in the code”** for integrating a change into the existing structure.

Key quote (approx):
- “*…then we weave in the code. It’s literally… weaving in code into an existing structure.*”  
  Timestamp: ~01:38:17–01:38:26

---

## “PRs are prompt requests” (and why prompts matter)

Peter reframes contributions:

- A traditional PR diff is often lower value than the intent + prompt.
- He’d rather receive a **prompt request** that clearly describes what to build.

Key quotes (approx):
- “*Pull requests… I see them more as prompt requests…*”  
  Timestamp: ~01:37:00+
- “*I read the prompts more than I read the code…*”  
  Timestamp: ~01:48:06–01:48:12

This matches the broader shift: review moves from line-by-line diffs to validating outcomes + gate results + architectural fit.

---

## How he uses agents to code (workflow)

### Tools + why he prefers Codex for complex work

From the discussion:

- He experiments across tools (Claude Code, Cursor, Gemini, etc.).
- His claim: **Codex is slower because it reads more**; that makes it better at weaving features into an existing codebase.

Key quote (approx):
- “*Codex… will just be silent and just read files for 10 minutes…*”  
  Timestamp: ~00:47:29–00:47:35

And:
- “*Codex is just so much better because it… reads more… sees a bigger picture of your codebase… weaves in new features better.*”  
  Timestamp: ~00:47:07–00:47:29

### Parallel agents

He runs multiple agents in parallel and “juggles” them:

- “*I use between five and 10 agents in parallel…*”  
  Timestamp: ~00:46:24–00:46:33

It’s more mentally taxing but keeps him in flow.

### Conversation before “build”

He repeatedly emphasizes a conversation-first mode:

- explore options
- reason about tradeoffs
- only then trigger implementation

Key quote (approx):
- “*I have a conversation with the model… what options do we have…*”  
  Timestamp: ~00:47:47–00:48:19

---

## How to learn this style (Peter’s advice)

### Learn by doing in public

Peter suggests working in open source and building real things.

Key quote (approx):
- “*Someone who’s active on GitHub and does open source…*”  
  Timestamp: ~01:43:05+

### Develop “system understanding”

He argues the differentiator isn’t typing code; it’s knowing:

- what questions to ask
- how to structure systems so they are testable
- how to set up feedback loops

Key quote (approx):
- “*Everything is just the right question away.*”  
  Timestamp: ~00:52:46–00:52:52

### Prompts are the new artifact

He recommends capturing prompts (or “prompt requests”) because they show the thinking/steering.

---

## Practical checklist I want to try

- [ ] For any feature: design the validation loop first (tests, CLI runner, quick repro).
- [ ] Add a local “full gate” script: lint + build + unit tests + minimal integration checks.
- [ ] Treat PRs as *intent artifacts*: request a prompt/goal + constraints, not just a diff.
- [ ] When using an agent: stay in “conversation mode” until the system design feels right.
