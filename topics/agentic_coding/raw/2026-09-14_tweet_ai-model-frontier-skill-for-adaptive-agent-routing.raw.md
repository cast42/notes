---
type: "tweet"
source_url: "https://x.com/JnBrymn/status/2099606852942143647"
canonical_url: "https://x.com/JnBrymn/status/2099606852942143647"
title: "AI model frontier skill for adaptive agent routing"
author: "John Berryman"
handle: "JnBrymn"
created_at: "2026-09-14"
date: "2026-09-14"
topics: ["agentic_coding"]
tags: [agent-skills, model-routing, pareto-frontier, model-selection, context-windows]
resource: "https://x.com/JnBrymn/status/2099606852942143647"
generated: {"by": "process:note-ingest", "at": "2026-09-15T05:28:49+00:00"}
sources: [{"id": "original", "resource": "https://x.com/JnBrymn/status/2099606852942143647"}, {"id": "skill", "resource": "https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier"}, {"id": "artificial-analysis-api", "resource": "https://artificialanalysis.ai/data-api/docs"}]
description: "A reusable skill that turns live model quality and price data into auditable Pareto frontiers for adaptive agent-model routing."
content_hash: "0fb70049e1ddce17d1862fe5019b973486bdb45c3c007314fce4603eb7db8445"
extracted_at: "2026-09-15T05:28:49+00:00"
extractor: "fxtwitter+github-skill"
---

# Raw content

Source: https://x.com/JnBrymn/status/2099606852942143647


## X post capture

URL: https://x.com/JnBrymn/status/2099606852942143647
Author: John Berryman (@JnBrymn)
Published: 2026-09-14T21:10:57Z

Post text:
This is a useful skill. I've scheduled ChatGPT to periodically check the Artificial Analysis AI api, pull data for models, and the create this fancy Pareto plot of the models for each frontier lab.

AND THEN it updates pi and omp config so that it can use these models.

Now when codex hits a window limit I jump over and start using some of those models in the upper left.

Here tis https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier

(anyone want to PR some other agent harnesses?)

Media:
- photo: https://pbs.twimg.com/media/HSNL_HrXwAA8C7Y.jpg?name=orig (2880x1800)

## Linked skill capture

URL: https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier
Raw URL: https://raw.githubusercontent.com/arcturus-labs/agent-skills/main/skills/update-ai-model-frontier/SKILL.md

---
name: update-ai-model-frontier
description: Retrieve Artificial Analysis model data and update per-company and combined cost-versus-quality Pareto frontiers, including API-key setup, reports and charts, and optional Pi or Oh My Pi model configuration.
---

# Update AI model frontier

On every normal skill run, retrieve or reuse a complete AA snapshot, produce `aa-frontiers.md` and the CSV/JSON outputs, run the chart script, and embed the finished plot and report in the current chat. Finish by asking what the user wants to do next. Default to the 15-company watchlist below, plus a combined watchlist frontier and an entire-catalogue frontier. Use Artificial Analysis (AA) data only for scores and prices.

## Setup

Prerequisites: Python 3.10+ (standard library only), outbound HTTPS to artificialanalysis.ai, a writable output/cache directory, and an AA organisation API key exported as `ARTIFICIAL_ANALYSIS_API_KEY`. Free-tier access is sufficient. Never include a real key in this skill, reports, command arguments, or source control.

Manual setup: open https://artificialanalysis.ai/api-key-management-redirect, sign in or create an account, select the organisation that owns the quota, and create/copy a key. Store it in a secret manager or export it in your shell configuration. If the key is stored in a shell profile, source that profile in the same shell invocation as the script; it must be exported for Python to inherit it. Do not print its value to check it.

Agent-assisted setup: use the available browser tools to open the same page and navigate the current UI. Reuse an existing authorised key/session when possible. Let the user complete passwords, MFA, CAPTCHA, or email verification when required. Ask for an organisation choice only if ambiguous. With the user's authorisation to obtain a key, proceed through ordinary setup, subject to the active tool's credential-creation rules. If those rules require a final confirmation, pause at the actual create action and explain that requirement; otherwise don't add a redundant approval step. Do not rotate/delete existing keys, purchase a subscription, or grant unrelated scopes. Use secure storage if available; otherwise have the user save/export the key locally and resume. There is no documented API for bootstrapping key creation; browser assistance still requires any authentication challenges presented by the site.

Current API reference: https://artificialanalysis.ai/data-api/docs. Use `/api/v2/language/models/free`; the similarly named `/language/models` requires Pro. Setup and API behaviour were verified September 11, 2026; consult the docs if the service changes.

## Definitions

- Quality (maximize): `evaluations.artificial_analysis_intelligence_index`, AA's existing general composite benchmark. Record its version. It is a benchmark proxy, not a guarantee of prose style or research quality. Do not invent personalized weights or substitute coding-only scores.
- Cost (minimize): USD per million tokens, `(3 × price_1m_input_tokens + price_1m_output_tokens) / 4`. This fixed 3:1 input/output blend excludes caching, tool charges, human time, and variable reasoning-token consumption. It is not cost per task or self-hosting cost.
- A model is dominated when another eligible model costs no more and scores no lower, with at least one strict improvement. The Pareto frontier retains all undominated models, including exact ties. This is not a convex-hull calculation. Treat reasoning configurations as separate AA records. Compare raw values, rounding only for presentation.
- Exclude missing/nonfinite scores or prices, and negative prices; report exclusions. Retain explicit zero prices with a caveat about conditions/free endpoints. Never equate null with zero. Do not compare historical scores across changed index versions without explaining the change.

Watchlist: Meta; DeepSeek; OpenAI; Anthropic; Alibaba/Qwen; Google; xAI (AA may label it SpaceXAI); Mistral; Z AI; Moonshot AI/Kimi; MiniMax; NVIDIA; Xiaomi; Amazon; Cohere. The script maps known aliases. Missing companies generate warnings for investigation, not silent omissions.

## Run

Resolve the script path relative to this skill directory. Example after loading the key into the environment:

```sh
python3 /absolute/path/to/update-ai-model-frontier/scripts/update_frontiers.py --output-dir /absolute/path/to/outputs/ai-frontier
python3 /absolute/path/to/update-ai-model-frontier/scripts/plot_frontiers.py /absolute/path/to/outputs/ai-frontier/aa-frontiers.json --output /absolute/path/to/outputs/ai-frontier/aa-frontiers.png
```

Fetch each page once, then compute company frontiers sequentially from the same complete snapshot. Do not request the API separately for each company. Pagination is dynamic: never assume the first page or four pages is the entire catalogue. The script validates page sequence, duplicate IDs, total-page consistency, and index version before producing reports.

The default cache lasts 24 hours. Report the snapshot timestamp even when reused. Use `--refresh` when a fresh fetch is requested; use `--snapshot path/to/snapshot.json` for reproducible offline regeneration. A refresh normally costs one request per page, plus any bounded retries. AA currently documents 100 free requests per fixed 24-hour window shared by the relevant user/organisation quota scope. The script bounds transient retries, checks remaining quota, and stops on 429 with reset details. Do not repeatedly retry quota or authentication failures. It never silently substitutes stale cache after a failed refresh.

## Results and recovery

Overlay recorded thinking variants for every model already on a displayed company frontier. Use `eligible_models` from the report JSON, matching company plus the model name with only explicit thinking qualifiers removed; preserve version, size, and fallback distinctions. Add thin company-colored connecting lines and thinking-symbol markers at each variant's own measured cost/quality. Do not impute missing prices/scores or introduce unrelated model families. Preserve the original frontier curves, dotted combined frontier, axes, and main frontier labels. Added thinking variants remain unlabeled. Skip families without other eligible records. Regenerate old report JSON if it lacks `eligible_models`.

Normalize each eligible record's `thinking_level` with `scripts/thinking_levels.py` from the explicit AA model name and record that provenance. Keep no reasoning, minimal, low, medium, high, extra high, and max distinct. Non-reasoning takes precedence over an accompanying effort label. Explicit reasoning without an effort and unlabeled models both use `unspecified`, displayed as Unknown/unspecified, never assumed to have no reasoning. These labels do not imply equal compute across vendors. Preserve all eligible records with this field in JSON, not just frontier survivors. Plot thinking levels with distinct marker shapes and a lower-right in-plot legend; keep company colors and model-name callouts.

Label every main plotted company-frontier point with its model name; do not label supplemental thinking-level points. Put names beside their markers with automatic nearby collision-aware positioning; use no leader lines or outer label columns. Remove thinking-level qualifiers from displayed names because marker shape already encodes them; preserve the full original name in data. Keep all frontier points visible and labeled. Retain a scalable SVG.

Present the report directly in the current chat, including the combined watchlist table and company frontier lists, timestamp, source, index version, cost definition, and material coverage warnings. Also retain/link `aa-frontiers.md`, CSV, and JSON for sharing and reuse. A download link alone is not the report. When the user asks only for a chart, show that chart without repeating every table.

Generate and embed a chart with `scripts/plot_frontiers.py REPORT_JSON --output OUTPUT_DIR/aa-frontiers.png` using a Python runtime with matplotlib. Each company has a distinct color, its frontier models are dots at (cost, quality), and solid lines connect its sorted frontier. Overlay the combined frontier of the same displayed companies as a dark dotted line. Do not substitute a convex hull or the entire-catalogue frontier when the chart shows only the watchlist. Use one panel with linear cost and quality axes, without a zoom panel. Default chart companies: OpenAI, Anthropic, Meta, xAI/Grok, Alibaba/Qwen, DeepSeek, and Z AI. Recalculate the dotted combined frontier from these displayed companies only; keep the broader 15-company report unless the user changes its scope. Label the snapshot, units, and source; explain that lines connect discrete choices rather than represent interpolated models. Save PNG and SVG and visually inspect the PNG before showing it in chat. Core report generation remains standard-library-only; missing matplotlib produces an actionable chart dependency error.

Availability columns are deliberately qualified: `has-api` is inferred from reported token pricing; `self-hosted` is unknown because the free API omits licensing. These are independent properties and can both be true when verified. Do not infer self-hosting eligibility from a company name or report unknown as false. If verified tags are requested, explain this source limitation and use authorised additional evidence, preserving its provenance separately.

Errors have actionable codes: `KEY_MISSING` → load/export the saved key or guide setup; `AUTH` → check the organisation/key; `TIER` → confirm free endpoint and access; `RATE_LIMIT` → use a suitable existing snapshot or wait for the supplied reset time; `NETWORK` → check network/sandbox access; `SCHEMA` → inspect current AA docs before adapting the parser; `FILESYSTEM` → choose a writable output directory. Follow the environment's network approval process if restricted; don't treat a sandbox failure as an invalid key.

## Follow-up questions and next action

After presenting the report and embedding the plot, always ask a concise next-step question, such as: "What would you like to do next—update Pi or Oh My Pi with selected models, compare cost per task or latency, or explore another result?" This is an interactive handoff, not authorisation to modify an agent harness on a report-only run. If the user already requested a next action, complete it and then ask what comes next. Keep the default chart design unless the user requests a different presentation.

Support questions from the same snapshot without spending additional API requests. Examples: "How much more does max thinking cost per benchmark task?", "Which frontier models respond fastest?", "Which thinking levels are missing?", and "What changes if we compare benchmark cost per task instead of token price?"

Retain the full API payload in `snapshot.json`, including records excluded from the token-price frontier. The processed JSON and CSV expose benchmark task/total cost and median response, first-token, first-answer-token, and output-speed fields for eligible records. For alternative-metric analyses, start from the raw snapshot when necessary: missing token price must not exclude a record that has the requested metric. Recalculate coverage for each analysis; missing data is unknown, never zero.

`artificial_analysis_intelligence_index_cost.cost_per_task.total_cost` is AA's cost per Intelligence Index benchmark task in USD. It is neither a personalized task cost nor the 3:1 token-price blend. `performance.median_end_to_end_response_time_seconds` is standardized response latency (AA documents 500 answer tokens), not elapsed time to finish an Intelligence Index task. The cost and latency measurements describe different workloads. Other performance fields distinguish first-token delay, first-answer delay, and output throughput. Explain these limits when comparing metrics. Coverage varies by model and thinking level; do not place task-cost values on the existing token-price axis. Source: https://artificialanalysis.ai/data-api/docs.

## Agent harness follow-up

For an authorised harness update, use each selected company's own frontier, not only the combined frontier. For a parity request, use the source harness's current selections and defaults rather than replacing them with a newly computed frontier. Respect provider/hosting preferences and preserve unrelated configuration.

Read only the reference for the harness being configured:

- [Pi setup and troubleshooting](https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier/references/pi.md): Pi's model registry, JSON configuration, scoped picker, credentials, and live verification.
- [Oh My Pi setup and Pi parity](https://github.com/arcturus-labs/agent-skills/blob/main/skills/update-ai-model-frontier/references/oh-my-pi.md): OMP's YAML providers, configuration interface, thinking compatibility, selection/default translation, and verification.

The reference procedures are agent-guided; the frontier and chart scripts do not update either harness. A report-only or scheduled research run must not change harness configuration. If the user has already requested an update, complete it using the appropriate reference without asking again. Distinguish catalogue registration, scoped selection, credential readiness, and successful generation in the handoff.
