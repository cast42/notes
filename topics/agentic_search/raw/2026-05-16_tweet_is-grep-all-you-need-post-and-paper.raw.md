---
type: tweet
source_url: "https://x.com/i/status/2055317577031975269"
canonical_url: "https://x.com/omarsar0/status/2055317577031975269"
title: Is Grep All You Need? post and paper
author: elvis
handle: omarsar0
created_at: 2026-05-16
topics: [agentic_search]
content_hash: e3fc0fde415982a4f1c4479de53283266e25ccdb1b531fb7d705417ed7b62f34
extracted_at: "2026-05-16T16:14:15"
extractor: fxtwitter+arxiv-web-fetch
date: 2026-05-16
timestamp: 2026-05-16
resource: "https://x.com/omarsar0/status/2055317577031975269"
---

# Raw content

Source: https://x.com/omarsar0/status/2055317577031975269


// Is Grep All You Need? //

Pay attention to this on, AI devs.

(bookmark it)

They find that grep-style text search, when wrapped in the right agent harness, matches or beats embedding-based retrieval on coding-agent tasks.

Are vector databases even needed where this is all going?

It might be that what coding agents needed was not better embeddings. It was better harness design around primitive tools.

If you operate a coding-agent stack that depends on a vector DB, it might be time to re-evaluate.

My personal experience on this has been that agentic search, if done right, is more than good enough for a lot of use cases. But you also have to understand how to properly index and structure information for the agents to take advantage. At scale, vector databases do shine so take that into account as well. In most cases, a hybrid approach often works best but that's something we haven't figured out really well as of yet.

Paper: https://arxiv.org/abs/2605.15184

Learn to build effective AI agents in our academy: https://academy.dair.ai/

---

Paper metadata
Title: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
Authors: Sahil Sen et al.
URL: https://arxiv.org/abs/2605.15184
DOI: https://doi.org/10.48550/arXiv.2605.15184

Abstract:
Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic search systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops. This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.
