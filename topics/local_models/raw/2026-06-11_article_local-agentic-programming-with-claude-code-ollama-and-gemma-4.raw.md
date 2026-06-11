---
type: article
source_url: "https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4"
canonical_url: "https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4"
title: Local agentic programming with Claude Code, Ollama, and Gemma 4
author: KDnuggets
created_at: 2026-06-11
topics: [local_models]
content_hash: a110ad7c19525e9e89518885ab73b2da8289de6952c4d218c1fc4aa644c0e5cc
extracted_at: "2026-06-11T07:56:45"
extractor: summarize+web-fetch
---

# Raw content

Source: https://kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4


URL: https://www.kdnuggets.com/local-agentic-programming-on-the-cheap-claude-code-ollama-gemma4
Title: Local Agentic Programming on the Cheap: Claude Code + Ollama + Gemma4

Summarize output:
The article's core claim is that local agentic coding is now practical and cheap if you pair Claude Code with Ollama and Gemma 4 26B MoE, provided you configure the stack correctly. The model is positioned as a major jump over the previous Gemma generation for tool use: it reportedly scores 86.4% on tau2-bench agentic tool use versus 6.6% for Gemma 3 27B, which the author treats as the difference between a model that constantly mangles tool calls and one that can survive a real coding-agent loop. Because Gemma 4 is Apache 2.0 and activates only about 3.8 billion parameters per token, the pitch is that you can run a private coding assistant locally without per-token costs or sending proprietary code to third-party APIs.
*"The Modelfile is not optional"*
Most of the article is really a deployment guide disguised as an argument. Its most important operational point is that Ollama's default 4K context window is far too small for agentic coding, so you need a custom Modelfile that raises context to 64K, lowers temperature to 0.2, and adds a system prompt that reinforces disciplined tool use. Without that override, the model silently loses track of file contents mid-session and makes partial, broken edits. The Claude Code side also needs careful environment settings: the local Anthropic-compatible endpoint must point to `http://localhost:11434`, model routing variables must all target the custom `gemma4-claude` variant, and beta headers should be disabled to avoid protocol errors.
The article also argues for validating the whole stack before touching real code. It includes a verification script that checks Ollama health, model availability, a basic Anthropic Messages API call, and, most importantly, whether the model emits a valid `tool_use` block. In practice, the described local setup is said to handle common engineering tasks well, especially code reading, test generation, targeted edits, and rerunning tests after failures. The main failure modes are misformatted tool parameters, context-window swapping to disk, model unloading between turns, and header mismatches, all of which the author frames as configuration problems rather than fundamental limits. Cloud models still win on large architectural reasoning, but for everyday coding work the article presents this as a usable local alternative.
*"The setup built in this article is a private, zero-per-token-cost coding agent"*


Additional article details captured via web fetch:
- Main stack: Claude Code + Ollama + Gemma 4 26B MoE.
- Strong warning that the custom Ollama Modelfile is necessary, especially to raise context window beyond Ollama's default 4K.
- Suggested Modelfile settings include num_ctx 65536, temperature 0.2, top_p 0.9, repeat_penalty 1.15, and a coding-agent system prompt.
- Anthropic-compatible endpoint for Ollama is described as http://localhost:11434 rather than /v1.
- Article includes a verification script to test Ollama health, model availability, Anthropic Messages API compatibility, and valid tool_use output.
