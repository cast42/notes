---
name: fantasy-cycling-manager
description: Help manage fantasy cycling lineups and transfer decisions for race-specific games such as Sporza Wielermanager. Use when selecting starters, captain, bench order, checking likely starters against public startlists, adapting lineups to race profiles (sprint, cobbles, hills), reviewing recent race performance, or suggesting low-risk transfer ideas for upcoming races like Scheldeprijs, Ronde van Vlaanderen, and Paris-Roubaix.
---

# Fantasy Cycling Manager

Use this skill to prepare race-specific fantasy cycling selections with a bias toward simple, explainable decisions.

## Core workflow

1. Identify the race profile.
   - Classify the race as one of: pure sprint, cobbled classic, hilly classic, TT, etc.
   - For sprint races, prioritize pure finishers over classics engines.
   - For cobbled monuments, prioritize endurance, positioning, cobble specialists, and likely starters.

2. Inspect the user’s current lineup.
   - Read the active starters, captain, bench, and any pending transfers from the game UI if accessible.
   - If the live UI is unavailable, work from the user’s screenshot or pasted lineup.

3. Check likely starters externally.
   - Use public startlist or race-preview sources to validate whether headline riders are actually expected to start.
   - Treat non-appearance in sprint-race startlist/top-competitor coverage as a strong warning signal for riders like Pogačar or van der Poel in races such as Scheldeprijs.
   - Do not overclaim certainty from one source; phrase it as “strongly suggests” unless the official startlist is explicit.

4. Make the smallest useful changes.
   - Prefer simple swaps over over-engineering the team.
   - First remove obvious non-starters.
   - Then remove obvious bad profile fits for the race.
   - Only suggest transfers if they clearly improve expected points for that specific race window.

5. Explain choices in plain language.
   - Say why a rider is a fit or a misfit.
   - Use race logic: sprint speed, cobble diesel, climbing punch, likely lead-out role, etc.
   - Prefer “this is optional, not essential” when the edge is marginal.

## Sporza Wielermanager navigation

Use these labels as the stable mental map of the UI:

- `Mijn ploeg` = the team area for the selected race/day
- `Mijn opstelling` = active starters, captain, and bench for that race
- `Mijn renners` = full owned roster
- `Transfers` = pending and executed transfers
- `Rit wijzigen` = switch the currently viewed race/day
- `Wijzig mijn opstelling` = open the lineup editor
- `Opstelling opslaan` = save lineup edits

### Safe interaction pattern
- Inspect the current race/day first.
- Confirm the race type before changing anything.
- Make one lineup swap at a time.
- Re-read the page after each change and verify the result.
- Never assume a transfer was finalized unless the updated page clearly shows the new rider state.
- If modal refs or clickable elements shift, stop rather than guessing.

## Practical heuristics

### Sprint races (e.g. Scheldeprijs)
- Favor: Philipsen, Merlier, Groenewegen, Girmay, other proven sprinters or fast finishers.
- Devalue: Pogačar, van der Poel, heavy cobble specialists, pure rouleurs, unless they are confirmed starters and likely to score incidentally.
- Captain should usually be a top sprinter, not a general classics star.

### Cobbled monuments (e.g. Ronde van Vlaanderen, Roubaix)
- Favor: Van der Poel, Pogačar, Küng, Politt, Vermeersch, Laporte, Mohorič, Roubaix-style engines.
- For Roubaix specifically, bias more toward diesel power and survivability than climbing explosiveness.

## Safety / execution rules

- Before changing a live lineup, state clearly what you intend to change.
- For risky live browser actions, prefer one change at a time.
- If the browser refs are unstable, stop rather than guessing.
- Never claim a transfer or lineup change was executed unless you have just verified it on the updated page.

## Useful response patterns

### Lineup advice
- “My single final swap recommendation is … because …”

### Transfer advice
- Give 1–2 candidate transfers max.
- Rank them by confidence.
- Mark optional changes as optional.

### Startlist validation
- “Public startlist coverage strongly suggests X is not starting; bench them.”

### Post-race review
- Separate:
  - what went right
  - what hurt
  - one practical lesson for the next race

## Scope limits

- Do not invent official startlist confirmations.
- Do not overfit one article quote into a transfer unless it aligns with race profile and team structure.
- Do not over-tinker if the team is already well shaped for the race.
