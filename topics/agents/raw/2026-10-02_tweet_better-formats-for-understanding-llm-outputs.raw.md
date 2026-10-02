---
type: "tweet"
source_url: "https://x.com/karpathy/status/2105819303471976479?s=20"
canonical_url: "https://x.com/karpathy/status/2105819303471976479"
title: "Better Formats for Understanding LLM Outputs"
author: "Andrej Karpathy"
handle: "karpathy"
created_at: "2026-10-02"
date: "2026-10-02"
topics: ["agents"]
tags: [llm-outputs, information-design, human-ai-interaction, agent-skills]
description: "Raw source capture for Karpathy’s post on multimodal formats for understanding LLM outputs and its ASD-STE100 skill follow-up."
resource: "https://x.com/karpathy/status/2105819303471976479"
generated: {"by": "process:note-ingest", "at": "2026-10-02T15:32:19+00:00"}
sources: [{"id": "karpathy_post", "resource": "https://x.com/karpathy/status/2105819303471976479"}, {"id": "alik_reply", "resource": "https://x.com/alik_huseyn0v/status/2105989790017454106"}, {"id": "asd_ste100_skill", "resource": "https://github.com/danyuchn/asd-ste100-skill"}]
content_hash: "e35cc47bd2bd94a419d7db656da93093e0a605f6c7a27ae6bec591398c872e0a"
extracted_at: "2026-10-02T15:31:03+00:00"
extractor: "fxtwitter API; image inspected visually"
---

# Raw content

Source: https://x.com/karpathy/status/2105819303471976479


## Andrej Karpathy — @karpathy — https://x.com/karpathy/status/2105819303471976479

We'll be spending a lot more time trying to understand the outputs of language models. A few thoughts, tips & tricks:

Writing. Something I've had success with: Ask your LLM to explain something in ASD-STE100, it's a controlled language specification originally developed for aerospace maintenance documentation. LLMs well-versed in this language and it comes with heavy constraints on clean writing style that I often find a lot more readable. Sometimes I've tried to soften it a bit e.g. ask for "80% of the way to ASD-STE100" because the spec is quite stringent. But even better:

Diagrams / images. Instead of writing, ask your LLM to create a diagram. These can be a lot easier to process, parse, and understand. But even better:

Web pages. Ask for output "in HTML" to get a beautiful, interactive webpage. LLMs are getting really good at frontend and can create beautiful experiences, animations, etc. But even better:

Explainer videos. The output format I am most bullish on is fully custom / bespoke explainer videos generated on any arbitrary topic. Experiment with things like "Create a 3b1b style video explainer on X. Use my ElevenLabs API key for audio narration". (you'd need an API key for the latter or you can ask your LLM to find you decent free alternatives that use your local compute). This is actually starting to work!

In summary:
- As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of our work will rise up the abstractions into oversight and understanding.
- Luckily, LLMs can help here too because as intelligence and code are increasingly abundant, you can ask for large, custom, discardable software artifacts (e.g. web apps, video explainers) that would have never made sense to create before. Push the boundaries here and you'll be surprised.

Attached infographic description: a visual overview of ASD-STE100, including its writing-rules/dictionary structure, annotated sentence examples, approved and non-approved verb forms, and writing limits.

## Alik Huseynov reply — @alik_huseyn0v — https://x.com/alik_huseyn0v/status/2105989790017454106

@karpathy Someone did it 3 months ago

https://github.com/danyuchn/asd-ste100-skill
