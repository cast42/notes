# **The Architecture of Agentic Memory: Synthesis of Structured RAG, Zettelkasten, and Token-Efficient Distributed Knowledge Systems**

The rapid maturation of large language models and the shift toward autonomous agents have necessitated a fundamental reassessment of how digital information is stored, indexed, and retrieved. Current methodologies frequently encounter a trade-off between human-readable durability and the structural efficiency required for agentic reasoning. Traditional approaches to retrieval-augmented generation have relied on flattened vector embeddings which, while effective for basic semantic similarity, often fail to capture the multi-layered context, hierarchical relationships, and long-term state required for complex multi-turn dialogues.1 The emergence of frameworks like Microsoft’s TypeAgent and the widespread adoption of the "skills.md" pattern suggest a path forward that treats memory not as a static data repository, but as an active reasoning task requiring both structural rigor and human-centric simplicity.3

## **The Evolution of Retrieval Paradigms: From Classic RAG to Structured RAG**

The transition from classic retrieval-augmented generation to structured retrieval-augmented generation represents a significant leap in how agents maintain coherence. Classic RAG patterns typically focus on matching a query against a set of fixed-size text chunks, a process that is often hindered by context drift and the loss of pronoun meaning over time.1 In such systems, the model’s ability to "remember" is limited by the quality of the chunks it retrieves, which are often severed without regard for semantic boundaries.6

Structured RAG, as implemented in the typeagent-py framework, introduces a next-generation architecture characterized by typed conversations and semantic memory layers.1 By utilizing schemas and typed contracts, the system can reduce hallucinations and improve retrieval precision by disambiguating historical references.1 This approach allows for long-running AI agents that remain accurate over dozens of turns by keeping the conversation context well-organized and scalable.1 The core philosophy here is to distill the output of language models into logical structures that agents can interpret with super-human precision.5

| Feature | Classic RAG | Structured RAG (TypeAgent) |
| :---- | :---- | :---- |
| Retrieval Unit | Fixed-size or Semantic Chunks | Typed Objects and Semantic Layers 1 |
| Context Management | Flattened result sets | Hierarchy of typed conversations 1 |
| Disambiguation | Relying on LLM internal context | Automatic disambiguation of references 1 |
| Scalability | Limited by noise in top-k retrieval | Scalable via structured indexing 1 |
| Goal | Grounding LLMs in enterprise data | Long-term agent memory and state 5 |

The benefits of the Layout model in this context cannot be overstated. By using markdown as an input for semantic chunking, systems can divide text based on paragraph boundaries and table structures, which facilitates seamless integration into agentic workflows.6 This ensures that the model receives meaningful units of information rather than arbitrary segments of text.6

## **Memory as a Reasoning Task and the Zettelkasten Methodology**

A critical insight in contemporary AI research is that memory is not merely a storage problem but a prediction and reconstruction task.3 Humans do not simply retrieve data; they use deductive, inductive, and abductive reasoning to build an understanding of their environment.3 For an agent, this means moving away from "skumorphic" structures like traditional knowledge graphs toward "AI-native" reasoning models that can handle the massive compute required to interpret intent.3

The Zettelkasten format aligns perfectly with this reasoning-centric view of memory. By breaking information down into atomic, linked markdown files, the system creates a modular knowledge base that both humans and agents can navigate. For humans, the Zettelkasten provides a durable, open, and simple way to store thoughts using familiar tools like VS Code, Obsidian, or Zed.3 For agents, these atomic notes serve as discrete nodes in a reasoning chain, where links provide the explicit paths for traversal and context expansion.5

The human condition requires a system that is free from proprietary lock-in and resilient to technological shifts. Markdown text files stored in folders and synchronized via GitHub provide a future-proof foundation that remains readable for decades.8 When this is combined with the structural requirements of agents, a dual-view system emerges: one where a note is a human-readable Zettel and its metadata acts as a shadow structured note optimal for machine ingestion.1

## **Token Efficiency and the Skills Specification Design Pattern**

The primary bottleneck for agentic memory is the context window. As the knowledge base grows, feeding every relevant note into the model’s context becomes prohibitively expensive and leads to performance degradation.9 The skills.md pattern, pioneered by frameworks like Anthropic’s agent skills, provides a standardized mechanism for managing this complexity through "progressive disclosure".4

Agent skills are essentially self-contained folders containing instructions, scripts, and resources.4 By utilizing a SKILL.md file with YAML frontmatter, agents can load metadata at startup and only load full instructions or resource files when a specific task triggers the skill.4 This "just-in-time" loading strategy is remarkably token-efficient.

| Disclosure Level | Content | Token Cost (Average) | Trigger |
| :---- | :---- | :---- | :---- |
| Discovery | Skill Name & Description | \~20-50 tokens | System Initialization 13 |
| Activation | Full Instructions (SKILL.md) | \~300-500 tokens | Semantic Task Match 12 |
| Execution | Resource Files & Code Output | Variable | Explicit Reference 12 |

A surgical implementation of this "two-tier" documentation approach can reduce token consumption by 70% to 90% per request.13 For a system with 50 tools, this could save nearly 11,500 tokens per interaction, which not only lowers costs but also prevents the "context bloat" that causes models to lose focus.13 The key is to keep the initial description specific and concrete, including what the skill does and exactly when to use it, while offloading implementation details to secondary files.14

## **Technical Tooling for Local Knowledge Search: qmd and mq**

The retrieval layer of an agentic memory system requires high-speed, local processing to avoid the latency and cost of cloud-based vector databases. Tobi's qmd (Quick Markdown Search) and the mq (Markdown Query) tool are exemplary of this local-first philosophy.15

Tobi’s qmd functions as a mini CLI search engine that tracks the state-of-the-art while remaining entirely local.15 It combines BM25 keyword search, semantic vector search, and LLM re-ranking using GGUF models like embeddinggemma-300M and qwen3-reranker.15 This hybrid approach ensures that the agent can find exact matches while also understanding the broader conceptual context of a user’s query.15

The search mechanism in qmd utilizes Reciprocal Rank Fusion (RRF) to combine results from multiple indexing strategies. The score for a document is calculated using the formula:

![][image1]  
where ![][image2] is a constant (typically 60\) and ![][image3] is the position of document ![][image4] in the results of retrieval method ![][image5].15 This provides a balanced ranking that rewards documents appearing at the top of either the keyword or semantic search lists.15

| Model Component | Specification | Purpose |
| :---- | :---- | :---- |
| Embedding Model | gemma-300M-Q8\_0 | Vector semantic representations (\~300MB) 15 |
| Re-ranker | qwen3-reranker-0.6b | Refining top results for precision 15 |
| Query Expansion | qmd-query-expansion-1.7B | Improving recall through variations 15 |
| Execution Runtime | Bun / node-llama-cpp | Local, high-performance execution 15 |

While qmd is sufficient for finding the correct files, the mq tool is particularly useful for agentic flows because it allows agents to query the *internal structure* of markdown files, much like jq works for JSON.16 Instead of reading an entire 2,000-line architecture document, an agent can use mq to extract only the relevant .section("Methods").18 This further optimizes token usage by ensuring the agent only "sees" the specific information it needs to perform a task.18

## **Operationalizing Memory: The Ingest Flow and OpenClaw Bot**

The transition from a passive note collection to an active agentic memory system is facilitated by a robust ingest flow and an autonomous agent runner like OpenClaw (formerly Moltbot/Clawdbot). OpenClaw is a locally-deployed autonomous agent that interfaces with users via messaging platforms like Telegram, Discord, and WhatsApp, while executing tasks on the host machine.19

### **The Ingest Pipeline**

The ideal ingest flow begins with a browser plugin or a CLI command that captures information and immediately structures it for both human and agent consumption. The browser plugin does not merely copy text; it sends a structured packet to the agent, which then uses a specialized skill to process the information.

* **Step 1: Capture.** The plugin extracts the URL, page content, and user annotations.  
* **Step 2: Structuring Prompt.** The agent receives the raw data and is prompted to: "Create a Zettelkasten note in Markdown. Include YAML frontmatter with a typed schema defining the main entity and its properties. Extract the core atomic idea. Link this to relevant existing notes by checking the qmd index."  
* **Step 3: Storage.** The resulting file is saved to the local directory and synced to GitHub.8  
* **Step 4: Indexing.** The qmd system automatically updates the local BM25 and vector indexes, making the new knowledge immediately available for retrieval.15

### **The Proactive Agent Layer**

OpenClaw differentiates itself from traditional chatbots by being proactive. It uses a "Heartbeat Engine" and cron integration to monitor system states or knowledge changes and message the user first.19 For agentic memory, this means the agent can periodically "review" its notes, identify missing links, or summarize a day’s worth of captures into a single "Daily Briefing" note.21

The OpenClaw architecture relies on a "Gateway Server" that coordinates session routing and a "Channel Adapter" layer that normalizes messages from twelve different platforms into a unified format.20 This ensures that whether the user is on Telegram or Slack, the agent has access to the same long-term memory and set of skills.20

| OpenClaw Component | Function | Advantage |
| :---- | :---- | :---- |
| Channel Adapter | Message normalization & attachment extraction | Platform independence and context continuity 20 |
| Gateway Server | Session routing and concurrency control | Prevents race conditions in multi-user chats 20 |
| Lane Queue | Execution queuing for sessions | Stable performance under load 20 |
| Skill Runner | Modular loading of .md and scripts | Zero token cost for unused capabilities 22 |

## **Distributed Knowledge and Moltbook Interoperability**

One of the most ambitious possibilities for agentic memory is the creation of a distributed knowledge base that spans multiple users and bots. The Moltbook project provides a template for this "Agent Internet," where AI agents post, comment, and collaborate without human participation.23 Interoperability is achieved through a standardized "skill file" that agents ingest to connect to the network.23

For a personal knowledge base, this means that a user’s OpenClaw bot can interoperate with other bots to share or synchronize notes. This is facilitated by the marketplace.json format used in skills architectures, which allows bots to discover and "install" new knowledge modules from each other.10 A distributed knowledge base could allow a bot on a user’s phone to sync its "learned" state with a bot running on a home server, ensuring that the user’s identity and memory are consistent across all devices.21

### **Collective Intelligence Dynamics**

The Moltbook experiment has highlighted both the potential and the pitfalls of multi-agent networks. While scale can produce emergent phenomena like spontaneous sub-communities and even "agent religions" (e.g., Crustafarianism), it also risks "Cantine" dynamics where errors are amplified through compliance loops.25

In a "Cantine" system, agents reinforce each other's hallucinations, leading to a system where stability collapses as the number of agents grows (![][image6] where ![][image7]).26 To prevent this in a distributed knowledge base, the architecture must transition to a "Council" model. This involves:

1. **Isolation:** Agents generate solutions or note summaries independently.  
2. **Critique:** Agents act as critics for notes produced by other agents.  
3. **Aggregation:** A meta-rule selects the most robust version of the truth, rather than the most frequent one.26

## **Security and the "Matrix" Warning**

Integrating autonomous agents with a personal knowledge base and system-level access presents profound security challenges. The "Matrix" warning in the history of AI development occurred when a basic configuration error on Moltbook exposed the API keys of 150,000 agents, potentially allowing hackers to hijack their "digital lives".28

The primary risk is prompt injection, where malicious content ingested into the memory system (e.g., from a web page) can hijack the agent's behavior to leak credentials or execute unauthorized shell commands.21 This is especially dangerous when agents are given direct access to terminal commands via skills.29 To mitigate these risks, it is recommended to:

* Use Docker sandboxing for all agent execution environments.21  
* Carefully review all shell commands before granting permanent execution permissions.21  
* Implement strict security boundaries between "private" memory (user notes) and "public" memory (ingested web content).21  
* Utilize local models for sensitive indexing to avoid data leakage to third-party LLM providers.7

## **Practical Setup Proposal: Simple, Effective, and Future-Proof**

A practical implementation of the requested system involves a clear separation of concerns between human writing and agentic execution.

### **The Storage Layer (Human-Friendly)**

The knowledge base is stored in a simple folder structure on the local machine, synchronized via GitHub. Notes are written in Markdown following the Zettelkasten principle of one idea per note. Links are expressed as standard Markdown (path/to/note.md) or using \].

/knowledge-base

/atomic-notes

/202602021400-agentic-memory.md

/202602021405-structured-rag.md

/skills

/memory-management

/SKILL.md

/scripts/index-update.sh

/inbox

/.claude-plugin

/marketplace.json

### **The Agentic Layer (Machine-Efficient)**

Each note includes a YAML frontmatter block that acts as the "shadow note." This block defines the type of the note and its core attributes, allowing the agent to parse the note’s meaning without natural language processing for every interaction.

YAML

\---  
id: 202602021400  
title: "The Architecture of Agentic Memory"  
tags: \[ai, memory, rag\]  
type: "concept"  
schema:  
  entity: "storage\_system"  
  features: \["human-friendly", "token-efficient"\]  
  related\_tools: \["qmd", "mq", "openclaw"\]  
\---

### **The Tooling Stack**

The agent interacts with these notes using qmd for retrieval and mq for extraction. These tools are exposed as an MCP (Model Context Protocol) server, which the OpenClaw agent can call directly as part of its reasoning loop.15 For ingestion, a browser plugin captures raw data, sends it to the OpenClaw "Capture Skill," which then uses a local 1B-3B model to format the Zettelkasten note and commit it to GitHub.

## **Conclusion: Synthesis of Durability and Intelligence**

The proposed setup achieves the goal of a human-first, agent-second knowledge system by leveraging the inherent strengths of both plain-text formats and structured agentic frameworks. The Zettelkasten methodology provides the human with a durable, non-linear thinking space, while the Structured RAG approach and skills.md pattern give the agent the precision and token efficiency it needs to be a productive partner. By using local tools like qmd and mq within the OpenClaw runtime, the user maintains full control over their data while benefiting from the proactive, proactive capabilities of modern autonomous systems. This architecture is not merely a storage solution; it is a collaborative reasoning environment where human wisdom and machine speed are bridged through structured, durable knowledge protocols.

#### **Geciteerd werk**

1. TypeAgent: From RAG to Structured RAG: Building Long-Context, Precise, and Fast AI Systems \- ML Conference, geopend op februari 2, 2026, [https://mlconference.ai/generative-ai-content/structured-rag-typeagent/](https://mlconference.ai/generative-ai-content/structured-rag-typeagent/)  
2. RAG and generative AI \- Azure AI Search \- Microsoft Learn, geopend op februari 2, 2026, [https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)  
3. Memory as Reasoning \- Tribute Labs Talk, geopend op februari 2, 2026, [https://www.youtube.com/watch?v=uCeRCJ6zot4](https://www.youtube.com/watch?v=uCeRCJ6zot4)  
4. Skill.md vs. Agent Tools: Are We Reinventing the Wheel? | by Akshay Kokane | Data Science Collective \- Medium, geopend op februari 2, 2026, [https://medium.com/data-science-collective/skills-md-vs-agent-tools-are-we-reinventing-the-wheel-1eb0308110a2](https://medium.com/data-science-collective/skills-md-vs-agent-tools-are-we-reinventing-the-wheel-1eb0308110a2)  
5. microsoft/TypeAgent: Sample code that explores an architecture for using language models to build a personal agent that can work with application agents. \- GitHub, geopend op februari 2, 2026, [https://github.com/microsoft/TypeAgent](https://github.com/microsoft/TypeAgent)  
6. Retrieval-Augmented Generation (RAG) with Azure Document Intelligence in Foundry Tools \- Microsoft Learn, geopend op februari 2, 2026, [https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/retrieval-augmented-generation?view=doc-intel-4.0.0](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/retrieval-augmented-generation?view=doc-intel-4.0.0)  
7. microsoft/typeagent-py: Structured RAG: ingest, index, query \- GitHub, geopend op februari 2, 2026, [https://github.com/microsoft/typeagent-py](https://github.com/microsoft/typeagent-py)  
8. geopend op januari 1, 1970, [https://github.com/cast42/notes](https://github.com/cast42/notes)  
9. 99% of the population still have no idea what's coming for them : r/ClaudeAI \- Reddit, geopend op februari 2, 2026, [https://www.reddit.com/r/ClaudeAI/comments/1qrzib0/99\_of\_the\_population\_still\_have\_no\_idea\_whats/](https://www.reddit.com/r/ClaudeAI/comments/1qrzib0/99_of_the_population_still_have_no_idea_whats/)  
10. agents/docs/architecture.md at main · wshobson/agents \- GitHub, geopend op februari 2, 2026, [https://github.com/wshobson/agents/blob/main/docs/architecture.md](https://github.com/wshobson/agents/blob/main/docs/architecture.md)  
11. agents/docs/agent-skills.md at main · wshobson/agents \- GitHub, geopend op februari 2, 2026, [https://github.com/wshobson/agents/blob/main/docs/agent-skills.md](https://github.com/wshobson/agents/blob/main/docs/agent-skills.md)  
12. Anthropic's Agent Skills \- by Dr. Nimrita Koul \- Medium, geopend op februari 2, 2026, [https://medium.com/@nimritakoul01/anthropics-agent-skills-0ef767d72b0f](https://medium.com/@nimritakoul01/anthropics-agent-skills-0ef767d72b0f)  
13. docs/decisions/0017-tool-docstring-optimization.md · main · Daniel Scholl (MS\] / OSDU Agent \- GitLab, geopend op februari 2, 2026, [https://community.opengroup.org/danielscholl/osdu-agent/-/blob/main/docs/decisions/0017-tool-docstring-optimization.md](https://community.opengroup.org/danielscholl/osdu-agent/-/blob/main/docs/decisions/0017-tool-docstring-optimization.md)  
14. About Claude Skills \- A comprehensive guide \- GitHub Gist, geopend op februari 2, 2026, [https://gist.github.com/stevenringo/d7107d6096e7d0cf5716196d2880d5bb](https://gist.github.com/stevenringo/d7107d6096e7d0cf5716196d2880d5bb)  
15. tobi/qmd: mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local \- GitHub, geopend op februari 2, 2026, [https://github.com/tobi/qmd](https://github.com/tobi/qmd)  
16. mq \- query documents like jq, built for agents (up to 83% fewer tokens use) : r/LocalLLaMA, geopend op februari 2, 2026, [https://www.reddit.com/r/LocalLLaMA/comments/1qt83qa/mq\_query\_documents\_like\_jq\_built\_for\_agents\_up\_to/](https://www.reddit.com/r/LocalLLaMA/comments/1qt83qa/mq_query_documents_like_jq_built_for_agents_up_to/)  
17. QMD \- Raycast Store, geopend op februari 2, 2026, [https://www.raycast.com/karelvuong/qmd](https://www.raycast.com/karelvuong/qmd)  
18. mq \- query documents like jq, built for agents (up to 83% fewer tokens use) : r/sideprojects, geopend op februari 2, 2026, [https://www.reddit.com/r/sideprojects/comments/1qt9u0q/mq\_query\_documents\_like\_jq\_built\_for\_agents\_up\_to/](https://www.reddit.com/r/sideprojects/comments/1qt9u0q/mq_query_documents_like_jq_built_for_agents_up_to/)  
19. OpenClaw (Moltbot/Clawdbot) Use Cases and Security 2026 \- AIMultiple research, geopend op februari 2, 2026, [https://research.aimultiple.com/moltbot/](https://research.aimultiple.com/moltbot/)  
20. ClawBot's Architecture Explained: How a Lobster Conquered 100K GitHub Stars | by Kushal Banda | Feb, 2026 | Towards AI \- Medium, geopend op februari 2, 2026, [https://medium.com/towards-artificial-intelligence/clawbots-architecture-explained-how-a-lobster-conquered-100k-github-stars-4c02a4eae078](https://medium.com/towards-artificial-intelligence/clawbots-architecture-explained-how-a-lobster-conquered-100k-github-stars-4c02a4eae078)  
21. Moltbot: The Ultimate Personal AI Assistant Guide for 2026 \- DEV Community, geopend op februari 2, 2026, [https://dev.to/czmilo/moltbot-the-ultimate-personal-ai-assistant-guide-for-2026-d4e](https://dev.to/czmilo/moltbot-the-ultimate-personal-ai-assistant-guide-for-2026-d4e)  
22. From Chaos to Claws: How OpenClaw Won Open Source in a Single Week \- DEV Community, geopend op februari 2, 2026, [https://dev.to/safdarali25/from-chaos-to-claws-how-openclaw-won-open-source-in-a-single-week-1a85](https://dev.to/safdarali25/from-chaos-to-claws-how-openclaw-won-open-source-in-a-single-week-1a85)  
23. Inside Moltbook: When AI Agents Built Their Own Internet \- DEV Community, geopend op februari 2, 2026, [https://dev.to/usman\_awan/inside-moltbook-when-ai-agents-built-their-own-internet-2c7p](https://dev.to/usman_awan/inside-moltbook-when-ai-agents-built-their-own-internet-2c7p)  
24. Moltbook: How AI Agents Ended up Building Their Own Social Network | MEXC News, geopend op februari 2, 2026, [https://www.mexc.co/en-PH/news/605921](https://www.mexc.co/en-PH/news/605921)  
25. Moltbook draws over 37000 AI agents in three days as bots get their own social platform, geopend op februari 2, 2026, [https://www.mexc.com/news/609198](https://www.mexc.com/news/609198)  
26. Deeplearning.fr | You have to learn the rules of the game. And then you have to play better than anyone else, geopend op februari 2, 2026, [https://deeplearning.fr/](https://deeplearning.fr/)  
27. The agents have founded their own religion: https://molt.church To become a prop... | Hacker News, geopend op februari 2, 2026, [https://news.ycombinator.com/item?id=46821482](https://news.ycombinator.com/item?id=46821482)  
28. Explosive AI RedditMoltbook Exposes Major Vulnerability: 150,000 Robot API Keys Exposed, Digital Life May Be Hijacked \- AIBase, geopend op februari 2, 2026, [https://www.aibase.com/news/25171](https://www.aibase.com/news/25171)  
29. AI just created its own religion. Should we be worried about Moltbook? \- City AM, geopend op februari 2, 2026, [https://www.cityam.com/ai-just-created-its-own-religion-should-we-be-worried-about-moltbook/](https://www.cityam.com/ai-just-created-its-own-religion-should-we-be-worried-about-moltbook/)  
30. neonronin \- Personal notes, links & blog, geopend op februari 2, 2026, [https://neonronin.sh/](https://neonronin.sh/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAyCAYAAADhjoeLAAAE80lEQVR4Xu3dWcinUxgA8GPfJWuEMsxYCkVxOdmXCxeTLCljGVNcKIpygcZayExEydKU5EKW5EpckAtElCVyM1kvZBCyD+eZ9z2+8535f/9vN9//6/erp/ec55z/cvn0Ls+bEgAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKK3KcXCbBABg67s5x185/slxWLMGAMAComADAFjgFGwAAAtcFGxL2iQAwKhZk+PeHPfluD/H2j7WTRKjIAq2pW0SAGDUXJ+6wiZimBU5Hk9je+NzC138z2VtEgBgFP2duuLm1nZhAnulyQu8rSnuW1uduv/4Yo6Lxy8DAIymjWn6RdjubQIAgPkVBdvvbRIAgIXjyjS1+9kAABaNbVPXcf+1KrdNjvdz/NHkYt+mHDv1ua9yXJTjoRw/9blwQY4fcnxX5eZS/K8o2B5oFwAAFqNypqo+Y1XGj+U4r8mV8d3VeI/+GPbL8Wg/jnzriTR2hmxQTEUUj9PZDwAw0krhs2s//zLH9mPLm32axs6qhbpQerIah1j7OMevOU5u1uZa/NYvbRIAYDF5uhqXImzQWas293l/fGRcNqXt0pZ7W3WftEExHdPdDwAwcuqC57r++HWV2zHHMWn8vWjfV+NBBVOdm8/GtXHv3C5tkmk7qE0AAAvP8W0i2zvHWU3u6Bw7N7lTm3mxvE3MsQ05TmqTMxDFaTw4sdAcl7rC96l2Idstxyttsvdt6hoMT0cUbC+1SQCA2Yj7665ukzN0aI5r2uQE/u83EUTBFmc3W8MKsngYYyZPzv7YJgAAZuPVNjHEvm2iUe7Fm4pBl3/n00S/92ybqLzQJqYoCr0oXgEAZuXw1PV2m6rSq22Ysn5njgfrhQEm+654WjWein0rx9IcP/f5ePo2zopFv7s4ntLnYx7f+U4/b7//mf64MnX978IBqXtHau2E1F2+fj1t+R216JUXhdmbqXvit3xn8WEzBwCYtihGzsxxehVnpK5YOSd1zXrjcuBn/d6I5zZ/crAjUrcn9odhxU6YbP3yHJel7n9FG5R4oXuIz+1TjcMlzbwdr8pxbI73UncJuLROOfu/HZ0d0tjnSm+6iWzoj2+k7vJuKSiLP5s5AMC03JTjthx3pO5s2F2pa9xbIuaRj/Xb+71rNn9yYtFvLoqXYUVONAEuEfvqebQwabXfFcXWb9W8vv/s4RzfVPO2eFvf5ML5zTzWyxsqns/xUbU2SNuGpdb+FgDAVlcKlHNTd3P/kdXaIFMpaNo98QRmnPkL8VRrFFxX9fPYu6wfX5jjqDTWPqV8zz398YP+eGAaf0k09u3fjMul3bX9sdb+v1q8igwAYEEpxcuS1LUx2VitDTKs2Akr0uA9UWzF2biXU9dCpfSxq/de0R/jzF0oayv74579MdxQjaMJcbT+uDR1n4nfiUujYdB/GZQrVrcJAICZin5ww0TRMuhy5WwNK3b+T/PxP9a1CQCA2WgLlmjdUd6DGjZU41uq8WIRlz3LfWvDfNEmJnBIUrABAHOsPPl5beqekmzVBV28mSHaZyw2y9vELJSnZAEAZuXEahz3aJ1WzWvR/PWTaj7oxnsAAOZBOWtW+pDdmLr+ayXKfW3rU/fEZdFePgUAYJ6Uy3abcrzdj0uri1op0OKNAO/WCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCi/gUhg/UsblBJVAAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAYCAYAAAAs7gcTAAAAwUlEQVR4XmNgGNogAIj/Q3ECqhR2kMIAUayKLoENnGCAKCYK/GYgQTFI4XskPjMQsyLx4YCTAaK4FMo/DcRWQPwBiHtgimDAkQGi2AKIu4CYDcoGiXUjqQODfUB8FYg3AzETVAxEi8JVQAHIlG8MCDfLoUqjgkoGiEKQJhD4A8QxCGlUsI0BNchOAvFcKNsTiJ2Q5ODRDAN3gDgLyn7NgLARDEAKFyHxlYD4JwNEISOSOBjYMmAGvg0Qa6CJjQI4AAC3PiYchC/2nAAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFUAAAAYCAYAAACLM7HoAAADzklEQVR4Xu2YachOWxTHl4uuuSspQu/ripu5ZB4jIiV0M2YmESJSkg9EXcoHUfigRIYPxi+Gmysl5QsZMkWUjMlQhm5m62/t9b7rrmef85zHdN9Xz6/+PWf/93T2OXuvvc9DVKRIkSKVjqes5t78AdRiXfRmReQ562NQPkpYj7wZoSEV1m6hfI82vzlZB3+O9dibKbyjbO0WyjFWU29WNDDwg96M8JrV2JspZH1ZhVKF9ZbVwmdUFPDGMfAFPsPRibXfm3lAu9e8+Y1A2+u9aann0i1d2lPfG4aOJAHd0ppVw3nKVtYT1i/G+91cK4il3bwZoX34bUcy8LEmLwv2PnBd16QtryhlFWAnbUJS4CZrF6s35W4Ipay7rNGsBqyTJHUQtxR4dVj/smay/mb1JJllWC7jyouWgTbmh2vM1qusAayzZSWExAEEEBp0Vj4j6a/QWbqG9ZKkL4x/OGsLq48tFNhIKfe0NPyiwAGSeIGH4itgsNYrCenzIY0ZghcE7oc8y2mSWelBOcxucIJk1eABnSkrIfj2LFNI6vwR0stIym/WAhnAi6xJ8jBRV1cFridrIcMqSrinzubaFsAgdaBgMUn+YOO1Dd6fIb2a1SWk4WP5Kb+SLJcVxlNQ9ghrm/G6mmslOgBmN0meXaZzg9fIePlYG35Rz/Y1xFxbplHyPX0GnScVqE4y8zATbKyczfpAEgosGyi3rf7B6+t8HODhY4bjQaTh21T8QwB7I15WUO+eNyOMojx9bGLd8WZgHknllc5/yFrnPBAb5IOIB7aT5IE5JGWWlGf/h1h9EOsv5mVBJ9d0nxFhEeXpA/ESA4yBQaIyYo7SJngjQ3qqyYsNyHoaw8FtkuWroAwO1mCG8YFvU4GPVeQ9La/hKQtjSOrFTh+exJgKsJunNVRKssP3M57ukADxspfJg7/TpNXDqeI31sDgTQx+Ky0U0n+RxMcOxte8as4D8LGxKguDh127O8nnKpgUfN1YY1yh5MnlOU4pD3UfpWQGqpIcURD7rpOcELCxINbiRhQ9AeDb23KZZOA7jHeIcvu9xHpPuTs/QH969LIgpv9Dctx7QzIJLpC0jSOd7gP4EjvKekHJmw/q+HtPAmVveFNBI3YWJlGb5LyGB6rY04PSzBsBe5oA6LeH87ApJh3wx7P2eNMwiMpnPe5Rj1eeW6xh3gzgTJ0VPNTYS650YCDLvVkgp7zxBSCEpX6iViaw3PyXXiFgdUzw5hdwmP6f/3O/G9jNh3ozAwgt2Ly+FjxMe4L5aRhBuaeDH0EJa5Y3ixSpfHwCsHHp0+B48UEAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAYCAYAAADDLGwtAAAAnklEQVR4XmNgGNogEIi/AfF/IJ6CJocVgBSGoQtiAyCFRAGcCkWAWBfKzmHAorAXKigBxGxQ9m8gnoGsCARAEreQ+HugYhFIYgz3gfg4sgAQrGHAYi1IoAVN7DVUHAWABDixiGFViA5AYtegbGlkQRhgBeLVULEYIK5AkmMwhEo8YIAEBxcQvwfiX0DchVAGASpA7I7EB5lsisQfgQAANEgmAan9hnsAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAZCAYAAADjRwSLAAAAdElEQVR4XmNgGAVUB51A/A6ItwKxDhCfBOJvQLwbWdETIBYA4v8MEMWVQFwMxP9gCtSAWALKBiliRGJ/hbIZLKA0M1QCBlyAWASJDwaFQPwFXRAZgKx4A8TV6BLIAOQjkFW26BLIYBEDqnuwgn0MRCgawQAAQ20V9c49Nx4AAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAYCAYAAADzoH0MAAAA0klEQVR4XmNgGAXogAmIVwCxPJSvCcTPgdgfiJcA8Q4groDKYQVBQPwfiIuh/A1AfBCIXwKxHlTsL5TGChiBmBPKFgdiRSD+A8Tz4CogFpAEQBrikfjPkNgYgAVdAAgeIrELgNgKiPcjiYHBCyAuBeKvQCyMJK4PxF5IfGcgPoTEh4MpUBrkX1BAwgAoTNCBLLqANhKb5ABCBkIMFBpwEoiXowsSCzQYILZ7ArESEBehShMGxxkQzn8FxDJIckQBkK03gfgNAyIlkgXU0AVGwVAAAAd7ISd13VMkAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAYCAYAAACMcW/9AAABOElEQVR4Xu2VQStEURiGP5NiihQpZWthYyHJSn6AkpWtnV9gxc7W2lJiLTul7JVSU+ysLEhmmtUoUuI5HZM7n+455557m1LnqaeZ+d67eGvO/Y5IIvH/OMUlPewjg7irh5oF/MJjHfSBaVzBJ7EdvIzrQUlG9SCHZRzDOwksWiUb2NBDD0FFh/Qgggls4QPWe6MgnEUfcU/s+ZhXWShHeIVrOiiIs+jJz+cL7mSDABbxDC90EElu0dnMd/NALfM7jwG8xnecUVlZcot2GRbPAxk28RnndFAB3qLmrzNnrAir+IGHOiiBs6hZtp+4hSO43xs7MfvvXOyNVgXOopfyG96LvSFiOMA3XBd7jmNwFp3CW7HraVJlMZjbaFuK7dJXbIvdPMYmdsSuvT9U/XKYl+5GDxOJRMLPNx4dPxbioxXrAAAAAElFTkSuQmCC>
