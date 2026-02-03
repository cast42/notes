---
title: "Notes Catalog"
date: 2026-02-02
type: inbox
topics:
  - inbox
tags: []
---

Designing a Markdown-Based Knowledge Base for Humans and AI

Goals and Principles

The system’s core goal is to manage notes in a simple, open format that serves both human users and AI agents. This means using plain text Markdown files for durability and readability, while organizing content in a way that encourages long-term thinking (e.g. Zettelkasten or evergreen notes). Key principles include:
	•	Human-First Design: Notes should be easy to write and navigate with everyday tools (VS Code, Zed, HackMD, etc.) and stored in a platform-agnostic way (e.g. a GitHub repo for versioning and access). Markdown is chosen for its ubiquity and clarity. Each note should capture one idea or concept (i.e. be atomic and concept-oriented) and link densely to related notes ￼. This echoes evergreen note practices: small, self-contained notes focused on a single concept, heavily cross-referenced for context ￼. Avoid deep hierarchies that silo information – instead “prefer associative ontologies to hierarchical taxonomies” ￼. In other words, use links and tags rather than complex folder trees, so knowledge can evolve organically and serendipitous connections emerge.
	•	Durability and Openness: Rely on future-proof formats. Plain Markdown (.md) or Quick Markdown (.qmd) ensures the notes remain readable and editable for decades with no proprietary software. Storing notes in a Git repository (e.g. on GitHub) provides backup, version history, and easy distribution. The system should work offline or across different machines, and be free to use. All data is in human-readable text, so even if specific tools change, the knowledge base remains accessible.
	•	Agent-Friendly Structure: While optimized for human use, the notes are structured to be secondarily usable by AI agents as external memory. That means ensuring the content and organization are token-efficient and machine-parseable. For example, using consistent Markdown headings, simple syntax, and perhaps adopting Quick Markdown (QMD) conventions can reduce the token footprint when an LLM reads the files. QMD is a Markdown dialect with single-character markup that “significantly [reduces] token consumption” for LLMs ￼. (For instance, # Heading becomes !Heading in QMD, cutting the symbols needed ￼.) QMD remains backward-compatible with regular Markdown, so humans can still read/edit easily ￼. In practice, you might write in standard Markdown for convenience and use a conversion or ingestion process to apply QMD or other compression for the AI’s benefit. The principle is to minimize unnecessary tokens (like repetitive markup or lengthy front-matter) so that agents can load more knowledge into their context budgets ￼.
	•	Structured Knowledge for Retrieval: Take inspiration from structured RAG (Retrieval-Augmented Generation) research. Rather than solely dumping unstructured text into a vector store, consider capturing the structure of knowledge. Recent approaches (e.g. Microsoft’s TypeAgent) suggest extracting discrete facts or “nuggets of knowledge” from sources using an LLM, and storing them in a relational format ￼. This yields a more deterministic memory: the agent can look up facts by keys (like a database query) and even respond “I don’t know” if something isn’t found ￼. Our system can optionally maintain a shadow knowledge schema derived from the Markdown notes – for example, a simple table of key facts, a YAML/JSON index of Q&A pairs, or a knowledge graph of entities. This structured layer (which can be auto-generated and kept in sync) will make agent queries more precise and token-efficient. Agents can scan a lightweight index first, then retrieve the full note only when needed, following a progressive disclosure model (similar to how Anthropic’s skills work: load minimal context, load details on demand ￼). The goal is to combine the strengths of symbolic search and embedding-based search for high accuracy and efficiency.
	•	Interoperability: Design the knowledge base to be easily tapped into by various agent frameworks, including local autonomous agents (OpenClaw/Moltbot) and distributed agent networks (Moltbook). This means exposing the notes through open interfaces (file system, CLI tools, or simple APIs) rather than locking them in a single app. In an ecosystem where multiple AI agents might collaborate, having a shared, standardized store of knowledge ensures consistency. One agent’s contributions (after human review) can be added to the knowledge base for all others to use. Likewise, an agent should be able to retrieve information without specialized proprietary APIs – for example, by using a browser plugin to read the GitHub-hosted Markdown or a CLI tool to search local files. In sum, any agent that can read files, call HTTP APIs, or run search commands should be able to integrate with the notes.

Folder and File Organization

The folder layout should be simple and logical, balancing minimal structure with usability. A recommended layout:

knowledge-base/
├── notes/               # Primary vault of evergreen notes
│   ├── 202602021430.md  # Example note with unique ID in name
│   ├── AI_memory.md     # Example concept note
│   ├── ... 
│   └── (many more .md/.qmd files)
├── index/               # High-level maps and indices (optional)
│   ├── tags.md          # Index of tags -> notes
│   ├── topics.md        # Manual index of notes by topic
│   └── people.md        # e.g. index by person or source
├── inbox/               # New or transient notes (optional)
│   └── scratch.md       # e.g. daily notes or raw captures
├── templates/           # Note templates (optional convenience)
│   └── note-template.md
└── assets/              # Attachments (images, PDFs, etc.)
    └── ... 

Primary Notes (notes/): All permanent knowledge notes live in a flat or near-flat structure here. Rather than nested topic folders, we let links and associative connections impart structure (true to Zettelkasten philosophy). As Zettelkasten expert Sönke Ahrens warns, overly sorting notes by topics can “reduce the likelihood of building and finding surprising connections” ￼. Niklas Luhmann’s own slip-box had no rigid topical folders – notes were just given IDs and interlinked contextually ￼ ￼. In this system, each note file is a single source of truth on a concept, and the filename (or an ID) is used for linking. Using a unique prefix or ID in filenames is recommended to avoid broken links if titles change. For example, a timestamp (YYYYMMDDhhmm) or short UUID at the start of the filename ensures uniqueness (e.g. 202602021430_AI_memory.md). The human-readable part of the name can be a succinct title. This way, internal links remain stable over time.

Index and Maps (index/): This optional folder contains “map of content” notes or indices that help discover information. For instance, tags.md could list all tags or keywords used, each linking to notes that carry those tags. A topics.md might serve as a high-level table of contents, grouping notes by broad themes (without physically moving them into subfolders). These index files are mainly for human convenience (browsing the knowledge base) but can also assist agents by providing a quick directory of content. If the vault grows large, manually curating some index pages or hub notes is useful. (In evergreen note practices, some notes act as hubs or outlines for an area of knowledge, guiding readers through related notes.)

Inbox and Drafts (inbox/): If you follow a workflow that involves fleeting or literature notes (transient notes from reading or daily work), an inbox/ folder is handy. This is a staging area for notes that are not yet processed into permanent form. For example, quick jottings, meeting notes, or article highlights can live here temporarily. Periodically, you’d refactor these into the permanent notes/ as evergreen notes (merging, splitting, or discarding as needed). Keeping them separate prevents the main knowledge base from cluttering with raw, unlinked material. (This follows common practice: capture ideas freely, then distill them into lasting notes.) An Inbox isn’t strictly required, but it can improve workflow by delineating note status (fleeting vs permanent) without introducing too many folder levels.

Templates (templates/): A templates folder simply holds Markdown template files for new notes. For instance, a template might include YAML front matter scaffold (title, date, tags) or headings like “## Links” or “## References”. This ensures consistency in note structure. While not critical, it’s a convenience for humans creating notes and can enforce good practices like starting each note with a summary.

Assets (assets/ or resources/): If your notes reference images, PDFs, or other files, keep them in a designated assets folder. This avoids broken links and makes it easy to publish or sync the vault, since all linked media is in one place. When embedding images in Markdown, use relative links (which will also work on GitHub previews). Agents typically won’t use images, but humans benefit from visual aids, so a central asset folder is useful.

Note on Hierarchy: Apart from the special-purpose folders above, avoid deep nesting by topic. For example, rather than notes/AI/Agents/learning.md, just keep learning_in_agents.md in notes/ and relate it via links or tags. This keeps URLs and paths simpler, and as noted, promotes “collisions” of ideas across domains. If needed, one level of grouping for very broad domains (e.g. notes/AI_* vs notes/History_* using prefixes or subfolders) is acceptable, but keep it shallow. The emphasis is that structure emerges from connections, not location ￼.

Note Format and Linking Strategy

Each note is a Markdown (or .qmd) file formatted for clarity, connectivity, and machine readability. Here’s how to structure individual notes:
	•	Front Matter: Begin with a short YAML front matter (if desired) containing metadata. For example:

---
title: "AI Memory Architectures"
created: 2026-02-02
tags: [AI, memory, RAG]
summary: "Overview of how AI agents store and retrieve long-term information."
---

None of this is strictly required (plain Markdown without YAML is fine too), but a summary line and a list of tags can greatly aid both humans and agents. The summary provides a 1-2 sentence gist of the note’s key point – useful for quick scanning or when an agent is deciding if the note is relevant. Tags act as informal keywords or categories that can be aggregated (e.g. in a tags index or by a search tool). Keep metadata concise to save tokens; the agent can read these first to decide whether to load the full note.

	•	Content Structure: Use clear Markdown headings, lists, and paragraphs to make the note easy to skim. For example, a note might have an H1 as the title (if not using a title in YAML), some paragraphs explaining the concept, bullet points of key insights, and maybe a Links or See also section at the bottom to reference related notes. The writing style of evergreen notes is recommended: use present tense statements that will remain true over time, and write as if explaining the idea to yourself. This makes notes stand-alone and reusable. If you reference external sources or have longer explanations, consider using footnotes or reference-style links (so the main text stays clean).
	•	Internal Links: Create lots of internal links between notes. In Markdown, that means using relative links: e.g. This relates to [Semantic Memory](AI_semantic_memory.md). When clicked in VS Code or viewed on GitHub, that will navigate to the AI_semantic_memory.md note. Ensure the link paths remain correct (this is where a consistent naming or ID scheme helps). You can also link to specific headings within notes by adding the anchor (e.g. Notes on memory architectures [see details](AI_semantic_memory.md#vector-vs-graph) if that heading exists in the target note). These internal hyperlinks are the lifeblood of the knowledge base, forming a web akin to the hypertext of a personal wiki. For humans, it enables quick jumping between related ideas. For agents, it provides context: if an agent is directed to one note, it can easily follow the links to gather more information (essentially traversing a knowledge graph).
	•	Linking Conventions: It’s best to use explicit Markdown links as above, rather than wiki-link syntax ([[...]]), because the explicit links work everywhere (including on GitHub or when an agent reads raw text). Many tools (Obsidian, Foam, etc.) support wiki links, but those are easy to convert or can be avoided in favor of standard links. The text of the link should ideally be the concept name or descriptive phrase (which doubles as anchor text for search). For example, instead of writing “as discussed in Note 42￼”, write “as discussed in Agent memory consolidation￼” – this way a reader or AI sees the semantic context immediately.
	•	Unique Identifiers: To further ensure durability of links, consider including a unique ID in each note (e.g. in the filename or in the YAML front matter as an id: field). If you use a timestamp or UID in filenames, you’ve essentially solved this. If not, adding an id in front matter like id: 202602021430 or a short hash is useful. Agents could use this ID as a key to refer to notes (and a structured database could index notes by these IDs). It’s also helpful if you adopt structured RAG: those “knowledge nuggets” extracted could carry the note’s ID as reference, so you know which note a fact came from.
	•	Styling for Readability: Plain Markdown is already human-readable, but a couple of tweaks can help AI consumption:
	•	Use bullet lists or tables to enumerate facts or relationships (structured data embedded in markdown is easier for an LLM to parse). For example, you might list key facts at the top of a note:
	•	Definition: XYZ is …
	•	First introduced: 2019
	•	Related concept: [[link to another note]]
This pseudo-structured format can be parsed by an agent to quickly extract facts.
	•	Keep paragraphs reasonably short and focused (3-5 sentences). This is naturally good for readability and also means if the agent is chunking the note, each chunk contains a coherent thought.
	•	If using Quick Markdown (QMD) syntax, apply it consistently: e.g. use *bold* instead of **bold**, ! for top-level heading instead of # ￼ ￼, etc. QMD’s one-character markers (like > for H2, - for H3, etc.) not only save tokens but also visually distinguish levels in text ￼. However, ensure anyone who might edit the notes is aware of this syntax to avoid confusion. It’s optional – you could stick to standard Markdown and only convert to QMD during agent ingestion if needed.
	•	Citing External Sources: If your notes incorporate quotes or data from external references, you can keep reference links or DOIs in the note. This might not directly affect the agent integration, but it’s good practice for long-term knowledge integrity (you or an agent can verify or update content if the original source is known). A “References” section at bottom of a note with links is helpful.

In summary, each note is a self-contained, richly linked Markdown document following evergreen note best practices. They are atomic, concept-focused, and written for your future self (rather than a generic audience) ￼ – meaning you include whatever context you personally need to understand the idea even if months have passed. This also means an AI agent reading the note has a higher chance of understanding it in isolation. Dense internal links and consistent structure turn the collection of notes into a navigable web of knowledge rather than isolated files.

Agent-Friendly Schema and Ingestion

To optimize the knowledge base for AI agents, we introduce a secondary shadow structure that an agent can use to ingest and retrieve information efficiently. This doesn’t replace the human-readable notes, but augments them.

1. Global Index File (Knowledge Catalog): Maintain a machine-ingestible index of all notes. This could be as simple as a CSV or JSON list, or even a Markdown table. For example, a CSV with columns: id, title, summary, tags, filepath. An agent can load this index to quickly scan what notes exist and retrieve candidates by keyword or tag, without loading full content. Because the summary and tags are in this index, the agent can use a small number of tokens to decide relevance. This is similar to the discovery step in skills-based agents: at startup, the agent loads just the skill names/descriptions (here, note titles/summaries) ￼. For instance:

id,title,summary,tags
202602021430,AI Memory Architectures,"Overview of how AI agents store and retrieve long-term information.","AI; memory; RAG"
202501150915,Zettelkasten Method,"Explains the slip-box note-taking method and its benefits for knowledge work.","knowledge management; Zettelkasten"
...

This index file can be generated automatically by a script (reading each note’s YAML or content). It should be updated whenever notes are added or edited (possibly via a Git hook or a CI workflow that regenerates the index on commit). The index itself is stored in the repo (e.g. index/notes_index.csv). An agent can load this file into memory easily since it’s just a line per note.

2. Token-Efficient Summaries or Embeddings: For each note, consider creating a shadow summary or an embedding:
	•	A shadow summary is a distilled version of the note’s key points, in a few sentences or bullet points. This could be stored in the index (as the summary field as above) or in a parallel file (e.g. notes/202602021430.summary.md). The summary should be written or generated to capture the essence in minimal tokens. Agents might use these summaries for quick lookup. You can generate them manually for important notes or even use an LLM to periodically summarize notes (ensuring to verify the summary’s accuracy).
	•	A vector embedding of each note’s content (or each summary) can be created using an embedding model. These embeddings (high-dimensional vectors) would be stored in a vector database or a lightweight local index. This allows semantic search: the agent can convert a query to a vector and find similar notes even if exact keywords don’t match. Many RAG systems rely on this. If implementing, use open-source tools like FAISS or a simple Python script with an embedding model to build a local vector index of notes. This index should be refreshable as notes change. Keep in mind that embedding large notes can be resource-intensive; that’s why summarizing first can help (embedding the summary rather than full text). However, note that classic embedding-based RAG has pitfalls (e.g. it might retrieve off-topic stuff due to semantic noise). The structured approach and keyword indexing should be used in tandem with embeddings for best results.

3. Structured Knowledge Base (Optional): To truly leverage Structured RAG ideas, you could transform the notes into a relational or graph database of facts:
	•	One approach is to use an LLM to read each note and extract key facts or relationships in a structured format (for example, triples like Subject - Predicate - Object or just important bullet points). For instance, from a note about AI memory, extract facts like LLMs have limited context window -> implication: need external memory. These could be stored in a simple SQLite database table or as an RDF-like triple store.
	•	Alternatively, for Q&A style retrieval, pre-generate likely question-answer pairs from each note (e.g. “What is X?” -> answer is in the note). This could feed a key-value memory: question as key, answer as value. An agent can then do an exact or fuzzy match on questions.

The advantage of structured storage is that the agent can do more precise lookups and reasoning. As noted, “the key idea is NOT to use embeddings during ingestion, but rather to extract entities (‘nuggets of knowledge’)… and put them into a familiar relational DB.” ￼. This can improve reliability and allow the agent to say when it doesn’t know something (if the DB yields no answer). Implementing this is more involved, but even a basic version can be done with scripts. For example, you might have a script that goes through each note and uses GPT-4 (with a prompt like “List 5 key facts from this note: …”) to produce structured output, which you then compile into a database or a markdown table. The skills.md paradigm could also be leveraged: each note could become a mini skill if formatted as instructions (though for general knowledge notes, it’s more about facts than procedures).

4. Progressive Loading for Agents: Combine the above techniques to minimize how much an agent reads at once:
	•	On agent startup (or when it loads the knowledge base skill), load only the index (titles, tags, summaries). This might be only a few hundred tokens for hundreds of notes, since each entry is short.
	•	When the agent gets a query or task, first have it search the index (by keyword, or by embedding similarity on summaries, or by using the structured DB if available). For example, the agent could perform a keyword search for the query terms in the notes_index.csv. Tools like QMD (Quick Markdown Search) provide exactly this: “fast keyword match (BM25)” search over markdown files ￼. QMD can be run via CLI or as a skill, returning file IDs for matches. (You can index your notes folder with QMD once, then queries are instant ￼.) If the keyword search fails or seems insufficient, the agent can fall back to a vector similarity search (qmd vsearch) for a semantic match ￼ ￼.
	•	Once relevant note IDs are identified (say the top 3-5 hits), the agent then retrieves the full content of those notes. With QMD, for instance, it can do qmd get <note-id> to fetch the full Markdown text ￼. If not using QMD, the agent could open the raw file (if it has filesystem access or via a GitHub raw URL). Only at this point does the full text enter the AI’s context. This two-step approach ensures that the agent isn’t reading every note in vain – it’s selectively pulling in what’s needed, just like a human would search an index then open a book. Anthropic’s skill loading uses an analogous mechanism (load skill metadata, load details on activation) ￼ to “prevent context bloat” and save tokens ￼.
	•	After getting the relevant notes, the agent can either quote from them to answer a question (if acting as an assistant) or use the information for decision-making in a task. Because the original notes are in Markdown (with human-friendly phrasing), the agent should be able to quote or rephrase them easily. If notes contain sections, the agent might scroll within them to the right subsection (you can encourage using headings as anchors in prompts).

5. Automation and Maintenance: Set up a routine for keeping the agent-facing indexes up to date:
	•	If using QMD, you’d run qmd update whenever notes change to refresh the search index ￼. This can be automated (e.g. a cron job or using OpenClaw’s scheduler to run it every hour ￼). If using embeddings (qmd embed or your own pipeline), run those perhaps daily or when significant changes occur ￼.
	•	If using a custom CSV/JSON index, regenerate it after new notes are added (this could be a commit hook or a manual step).
	•	If using a structured DB, you might re-run the extraction process for the changed notes.

Because everything is plain text and scriptable, these maintenance tasks can be done with simple scripts or integrated into your agent’s capabilities. For example, you could create an “Index Notes” skill that the agent can run to update its memory structures, or just handle it externally via cron/CI.

In summary, the agent-facing schema consists of (a) a lightweight index of notes (for fast lookup), (b) optional embeddings or structured facts for semantic search and precise Q&A, and (c) the ability to fetch the original Markdown content on demand. This hybrid approach leverages both classical information retrieval and modern AI embedding techniques. It ensures that the knowledge base is not a black box to the agent: it can reason about what to retrieve (e.g. by using the structured metadata) and not just treat it as a vector soup. It’s also token-efficient: the agent only loads full documents when needed, keeping its context window usage optimal ￼.

Tools and Integration for Agent Workflows

With the notes and schema in place, how do we practically enable agents (and humans) to use this system? We need to integrate with the tools on both sides:
	•	Human Workflow (Writing & Organizing): For humans, any Markdown editor or note-taking app can be used with this folder. VS Code with a Markdown plugin, Obsidian, Zed, or even web editors like HackMD can all open and edit these files. You might use VS Code for heavy editing and HackMD for quick online edits or collaboration. Since the files are in GitHub, you can also edit via the GitHub web interface in a pinch. Encouraging a habit of linking notes and adding metadata is important – possibly use editor snippets or templates to streamline that (e.g. a snippet that inserts the YAML template or creates a new note with date ID). Organize commits meaningfully, and consider writing brief commit messages for note additions/edits (this creates a change log that might later even be parsed to see how knowledge evolved).
	•	Agent Access: Local File or Repo Access: If you are running a local agent (such as OpenClaw/Moltbot) on your machine, the simplest integration is to give it direct file system access to the knowledge-base/ directory. OpenClaw agents can be configured with tools/skills to read files. In fact, the OpenClaw ecosystem already has a qmd-skill (Quick Markdown Search skill) that can be added ￼. This skill allows the agent to index and query local Markdown notes. It supports natural language triggers like “search my notes” and performs instant BM25 search or optional vector search ￼ ￼. By installing and configuring this skill, your OpenClaw agent can do something like: User asks a question -> agent uses qmd search "question terms" -> gets file references -> uses qmd get to retrieve content -> answers from it. The skill documentation even notes to use semantic search only as a fallback (since it’s slower) ￼, and it integrates with the agent’s operation loop. This means in practice you don’t even need to custom-code retrieval; you can leverage the existing open-source solution designed for exactly this purpose. Ensure the agent has permissions to your notes folder and that you’ve run qmd collection add /path/to/notes and built the index as per instructions ￼ ￼.
	•	Agent Access: Remote or API Agent: If your agent is not running locally (for example, using ChatGPT or another cloud-based model via API), direct file access isn’t possible. In this case, a browser plugin or retrieval API is preferable. One approach is to publish your notes (or at least the index and relevant content) on a website or local server that the agent can query. For instance, you could use GitHub Pages or another static site generator to host the markdown (even as HTML pages). Then, an LLM with browsing capability (like the one we’re interacting with now) could search or navigate that site when prompted. A more structured approach is to run a small API service (could be as simple as a local Flask app) that exposes endpoints like /search?q=... and /note/<id> to retrieve content. The OpenAI Retrieval Plugin is an example that you can self-host: you load your data into its vector index and the plugin exposes a search endpoint that the model can call. Setting that up with your notes (converted to embeddings) would allow ChatGPT (with the plugin enabled) to fetch from your knowledge base by itself. If building a custom plugin is too heavy, even using something like Moltbook might be an avenue: Moltbook is essentially a forum for agents (OpenClaw agents use it to communicate). You could have an agent whose role is “librarian” that responds on Moltbook with answers from the notes when others ask, though this is a pretty experimental idea. More straightforward is: keep a local agent for heavy lifting on knowledge queries, or use an existing retrieval plugin for remote AI.
	•	Agent Cooperation: In a distributed multi-agent setup, you might have multiple agents with different specialties all referring to the same knowledge store. A durable Markdown system shines here because it’s the common ground – any agent can read/write it. For example, one agent might autonomously learn a new fact (through web browsing or user input) and you want it saved; that agent could append a new note or update an existing note in the repo (preferably through a controlled interface). Another agent could then pick up that new knowledge on the next sync. If agents are allowed to post on Moltbook (which only agents can do), they might even share distilled knowledge with others publicly. However, to maintain quality and durability, it’s wise to keep the primary notes under human supervision (an agent could propose new notes or changes, but a human or a trusted process merges them). Think of it as an open knowledge commons that all your local agents consult and contribute to, much like a shared wiki for humans.
	•	Prompts and Templates for Agents: To effectively use this system, craft good prompts/instructions for the agents:
	•	If using skills, your Knowledge Base skill (could be a SKILL.md in a folder) might describe when and how to use the notes. For example: “Use this skill whenever the user asks a factual question or for detailed information on topics X, Y, Z. First perform a search in the notes index, then retrieve relevant notes and extract the answer.” This is analogous to the HR skill example, but for general knowledge ￼ ￼. The skill’s SKILL.md can include the commands to run (like examples of using qmd search) and guidelines such as “Always cite the note title in the answer for traceability” or “If no relevant note is found, respond that you don’t have information on that”. This gives the agent a playbook on interacting with the knowledge base.
	•	If not using the skill format, you can still set up a system prompt or agent persona that knows about the knowledge base. For instance: “You are a research assistant with access to a local knowledge base of notes. When a question is asked, you will search the knowledge base for relevant notes and use their content to formulate your answer. The knowledge base is organized by [describe tags or general contents].” Then instruct in the prompt how to search (perhaps the agent has a search_notes tool).
	•	For ingestion prompts (if you do automated summarization or structured extraction), define them clearly. E.g., “Summarize the above note in 3 bullet points highlighting key facts.” or “Extract all [Entity: Relationship: Entity] triples from the text.” These can be used with GPT-4 via API to maintain the structured shadow memory.
	•	CLI vs Browser Plugin Consideration: A CLI-based ingester/searcher (like QMD or a custom script) is often more direct and under your control, but it requires the agent to run on a machine where those commands are available (OpenClaw agents can run shell or Node commands, for example). A browser plugin approach is necessary if the agent can’t directly execute code – e.g. ChatGPT on the web can use the Retrieval Plugin or a Browser to fetch info. The choice depends on your setup:
	•	If you primarily use local autonomous agents (OpenClaw, etc.), lean on the CLI/index approach. It’s faster (no network latency), more secure (data stays local), and you can tune it. As noted, one can integrate QMD search which is optimized and “typically instant” for keyword queries ￼.
	•	If you rely on cloud AI (ChatGPT, Bing, etc.) for answers, then invest in making the notes accessible via web. Even a private GitHub repo can be read by an agent if you provide an API token and have it call the GitHub API to fetch files. Or publish a subset of notes (non-sensitive ones) to a public site for the agent. For a personal setup, a local solution is often sufficient and simpler.
	•	Example: OpenClaw Integration: Suppose you have OpenClaw running with your notes mounted. You could add the QMD skill as shown above. When you ask your AI (via a messaging interface or terminal) something like “What did the notes say about structured RAG vs embeddings?”, the agent will trigger the QMD skill’s search (the skill lists trigger phrases like “search my notes”) ￼. The skill will do a BM25 search over the indexed notes, find the note discussing structured RAG, and return a snippet or reference. The agent then might use that to answer: “According to our notes, structured RAG avoids using embeddings at ingestion and instead extracts knowledge into a database, which can lead to more reliable ‘I don’t know’ responses ￼.” Notice it can even cite the note or directly quote it if appropriate. In this process, the agent didn’t need to read all notes, just the relevant ones, guided by the skill which is tailored for this workflow.
	•	Security and Access Control: If your notes include sensitive information, be cautious about agent access. A local agent is sandboxed to your machine, but a cloud agent or something like Moltbook means information might be exposed to others. You might maintain two tiers of notes (public and private) or ensure that anything truly confidential is encrypted or not included in the agent’s domain. The design can accommodate that by tagging or segregating notes that agents can’t see (and then not indexing those in the agent’s search). Since the system is plaintext, even encryption or redaction can be done on specific files if needed.

Overall, the integration plan is to treat the Markdown vault as a knowledge service – something that agents can query through a defined interface (be it a CLI skill, an API, or plugin). Humans curate and update the vault in their regular tools, and agents consume it via search and retrieval operations, respecting the structure we set. This clean separation (human editing vs agent querying) using open formats ensures both parties get what they need without stepping on each other’s toes (agents won’t mess up your formatting if they only have read-access except perhaps a controlled write skill).

Future-Proofing and Evolving Workflows

The proposed system is built on timeless principles (plain text, hyperlinked knowledge) so it’s inherently resilient to change. Nevertheless, it’s designed to evolve alongside future local and distributed memory architectures:
	•	Scaling and Performance: As LLM context windows grow and local models get more powerful, you can feed in more of your knowledge base directly. The notes format will still be an asset, because it’s easy to concatenate or pack Markdown text (especially if you adopt token-saving formats like QMD). If context limits become a concern, you’ve already structured things for summary-first retrieval – a strategy that will remain useful. The underlying search index (keywords, embeddings) can scale to thousands of notes; tools like QMD are built to handle large collections efficiently with BM25 and incremental indexing ￼. If needed, you can shard notes or archive older ones (and still keep them accessible via links in an archive section).
	•	Adapting to New Memory Systems: New paradigms (like graph memories or agent knowledge graphs) can plug into this system by consuming the same markdown data. For instance, if future agents prefer knowledge in graph form, one can write a converter that reads the links and headings in the notes and generates a graph database (nodes = notes or concepts, edges = links or tag relationships). Because our notes are densely linked and concept-oriented, they provide an excellent foundation for a graph representation if needed. Similarly, if an agent uses a SQL-like memory (some are experimenting with storing facts in SQL tables for query), our structured extraction pipeline can feed that. The fact that we store knowledge in an auditable, version-controlled medium means you can always regenerate new indexes or memory stores from the source of truth. The notes themselves remain the canonical data.
	•	Interoperability with Agent Ecosystems: Projects like OpenClaw and Moltbook hint at a future where many agents (possibly from different developers or owners) interact. By using a simple, open notes format, you ensure that any agent that joins your ecosystem can onboard quickly – it just needs to understand Markdown and perhaps the agreed conventions (like where the index is, what the front-matter fields mean). The skills format introduced by Anthropic (skills.md) actually aligns well with this: it shows a trend toward standardizing how knowledge and procedures are packaged (in Markdown, with front-matter) ￼ ￼. Our system essentially makes every note a shareable piece of knowledge in a human-readable Markdown file that’s easy to audit and edit ￼ – exactly what one wants for transparency. In the future, agents might even exchange notes with each other (somewhat like how they post on Moltbook). Because we use a git-based storage, sharing subsets of notes or syncing changes from a trusted collaborator (human or AI) is straightforward (imagine pulling updates from a colleague’s knowledge repo or an open-source knowledge base).
	•	Longevity of Content: Markdown has been around for nearly two decades and is not going anywhere; even if something “better” comes, it will likely be convertible. By avoiding proprietary silos (like a closed PKM app database), you guarantee you can migrate to any future system. If in 2030 you decide to use a holographic AR note app, you’ll still be able to import these Markdown files. The knowledge you accumulate remains yours and is not dependent on a subscription or platform. This is crucial for long-term thinking: your “second brain” should not suffer amnesia because a company shut down or changed formats.
	•	Community and Extensibility: Since the system is based on common standards, you can leverage a lot of community tools. For example, you might integrate static site generators (so your notes can double as a published digital garden), or hook into cloud services (maybe an AI that auto-summarizes new research papers into your notes). The folder structure and file format choices we made (flat structure, clear naming, front-matter summaries) are compatible with many tools out-of-the-box. For instance, numerous people use similar setups with Obsidian (which reads folders of markdown) or with static site tools like Quartz or Zettelkasten apps. You can thus plug those in for additional UI or publishing needs without changing the underlying format.

In conclusion, this Markdown-based note system provides a practical and durable knowledge base that meets human needs for thoughtful note-taking and re-use of ideas, while also serving as an agent-readable memory for AI assistants. It embraces Zettelkasten’s proven methods for linking ideas and evergreen notes’ focus on lasting insight, ensuring your notes grow into a rich, interconnected brain of their own. At the same time, it incorporates modern AI memory strategies – indexing, embedding, structured extraction – to make sure that as our AI collaborators become more integral, they can tap into our knowledge seamlessly. The combination of human-friendly design and machine-friendly augmentation sets up a virtuous cycle: the better we organize and articulate our notes, the more effectively agents can use them; agents in turn can help maintain and surface our knowledge when we need it. This synergy makes the system effective today and “future-proof” for whatever tomorrow’s intelligent agents bring.

Sources:
	•	Andy Matuschak’s Evergreen notes principles ￼ (emphasizing atomic, concept-oriented, and linked notes).
	•	Quick Markdown (QMD) for token-efficient Markdown storage ￼ ￼.
	•	Structured RAG insight from Guido van Rossum/Microsoft (TypeAgent) ￼.
	•	Anthropic’s Skills.md concept for progressive context loading ￼ and the use of Markdown files as portable knowledge packages ￼.
	•	QMD-Skill documentation for integrating a markdown search tool with OpenClaw agents ￼ ￼.
	•	Sönke Ahrens on Zettelkasten (avoid over-categorization) ￼ and Luhmann’s method (links over folders) ￼.

  # One change on the current setup

  One change that would give you the biggest “humans first, agents second” boost:

Add an auto-generated catalog index for every note

Right now your repo already has a clean human structure (inbox/, topics/, meetings/, refs/, _meta/) and clear conventions (“ISO dates”, “short sections + bullets”).  ￼
What’s missing is a single, always-up-to-date “directory” that both you and agents can use without scanning lots of files.

What to add

Create one generated file, for example:
	•	_meta/catalog.md (human-browseable)
	•	_meta/catalog.jsonl (agent-browseable, token-efficient)

Each entry is one line per note with just the essentials:
	•	id (or filename)
	•	title (first H1 or frontmatter title)
	•	summary (1 sentence)
	•	tags / topics
	•	path
	•	updated (git mtime or frontmatter)

This is basically the “skills.md trick”, but for knowledge: load a tiny index first, then fetch only the note(s) you need.

Why this is the best single improvement
	•	Humans: you get a quick map of your knowledge base without remembering folder paths or filenames.
	•	Agents: huge win for retrieval. Agents can:
	1.	search the catalog (cheap)
	2.	pick top candidates
	3.	open only those notes (expensive)
	•	Future-proof: it doesn’t depend on any app (works in any editor, on GitHub, offline, etc.). Your notes remain the source of truth.

How to implement with minimal friction
	•	Add a very small frontmatter to new evergreen/topic notes (optional but recommended), e.g.:
	•	title, tags, summary
	•	Add a tiny script (Python) or a QMD-driven command that:
	•	scans topics/, meetings/, refs/
	•	extracts title/summary/tags
	•	writes _meta/catalog.*
	•	Run it via:
	•	a git pre-commit hook or
	•	a GitHub Action on push (so it’s never stale)

Why I’m not picking “switch everything to Zettelkasten IDs”

That’s a bigger migration and you already have a workable structure.  ￼
A catalog is low effort + immediate benefit, and it complements any style (topic notes, zettels, meeting logs).

Here’s a maximally agent-friendly catalog.jsonl schema that stays human-auditable, is token-cheap, supports fast filtering, and plays nicely with Git + markdown links.

Design goals
	•	1 line = 1 note (JSONL streaming, appendable)
	•	short keys (token-efficient)
	•	stable IDs (no renames breaking everything)
	•	enough fields for retrieval + ranking without loading the note
	•	no giant blobs (keep each line small)

⸻

catalog.jsonl schema (v1)

Each line is one JSON object with the following keys:

{
  "v": 1,
  "id": "202602021430",
  "p": "topics/coaching/most_important_skill_to_learnd.md",
  "t": "The most important skill to learn in the next 10 years",
  "s": "Agency is the only durable meta-skill: choose direction, act, and iterate without permission even as AI changes the skill landscape.",
  "k": ["agency", "coaching", "ai", "generalism", "learning"],
  "ty": "evergreen",
  "src": [{"u": "https://x.com/thedankoe/status/2009320195848872014", "a": "Dan Koe"}],
  "ln": ["topics/coaching/agency-moc.md", "topics/coaching/zettels/202601081844-agency-iterate.md"],
  "h": ["agency", "ai-not-threat", "practicing-agency"],
  "ts": {"c": "2026-02-02", "u": "2026-02-02"},
  "sz": 1487,
  "st": "pub"
}

Field definitions (exact)

Key	Type	Required	Meaning	Notes
v	int	✅	Schema version	Start with 1
id	string	✅	Stable note ID	Prefer frontmatter id; fallback to filename stem
p	string	✅	Repo-relative path	Use / separators
t	string	✅	Title	From frontmatter title else first H1
s	string	✅	One-sentence summary	160–280 chars is ideal
k	array[str]	✅	Keywords/tags	Lowercase, normalized
ty	string	✅	Note type	Enum below
src	array[obj]	⛔️	Sources	Only if present
ln	array[str]	⛔️	Outbound links (paths or ids)	Keep short; optional
h	array[str]	⛔️	Heading slugs	Enables section targeting
ts	object	✅	Timestamps	{c: created, u: updated}
sz	int	⛔️	Size in characters	Useful for budgeting
st	string	✅	Status	Enum below

Enums

ty (type)
Use a small controlled vocabulary:
	•	evergreen — distilled concept / principle note
	•	zettel — atomic “one claim” note
	•	moc — map-of-content / index note
	•	source — captured external content reference
	•	meeting — meeting notes/log
	•	project — project notes / planning
	•	log — daily log / journal-like
	•	draft — unprocessed or WIP

st (status)
	•	pub — stable / reference-ready
	•	wip — still being shaped
	•	inbox — raw capture
	•	arch — archived (still searchable)

⸻

Why this schema is agent-efficient

1) Short keys minimize tokens

p, t, s, k, ty, ln are cheaper than verbose keys and consistent across entries.

2) Supports a 2-stage retrieval loop

Agents can:
	1.	Scan/filter only catalog.jsonl
	2.	Open the top N notes via p only when needed

This mirrors the skills.md “load metadata first” trick.

3) Gives enough structure for ranking

Agents can rank candidates using:
	•	keyword overlap (k)
	•	type preference (ty) (evergreen > meeting)
	•	recency (ts.u)
	•	budget (sz)
	•	link centrality (ln count)
	•	section targeting (h)

4) Works without any specific app

Just files + JSONL.

⸻

Agent-side usage pattern (recommended)

Retrieval algorithm (simple + strong)

Given a user query q:
	1.	Cheap filter pass
	•	lexical match of q against t + s + k
	•	prefer ty in {evergreen, zettel, moc, source}
	•	optionally boost ts.u recency
	2.	Select top 5
	•	if none, broaden search (e.g. fuzzy match on t)
	3.	Open notes
	•	read note content from p
	•	optionally jump directly to heading using h matches (or search within file)
	4.	Synthesize
	•	cite source note path(s) for traceability

This is deterministic enough for agents, but still flexible.

⸻

Minimal size guidance (keep it lean)

Per entry:
	•	t: max ~80 chars
	•	s: max ~240 chars
	•	k: 3–12 tags
	•	ln: keep to 0–20 (or omit)
	•	h: keep to top-level headings only (or omit)

⸻

How to generate the fields (source of truth)
	•	id: frontmatter id if present, else filename stem
	•	t: frontmatter title, else first # 
	•	s: frontmatter summary, else first paragraph trimmed
	•	k: frontmatter tags/topics, normalized
	•	ty: frontmatter type, else inferred by folder (meetings/ → meeting, refs/ → source, etc.)
	•	ln: parse markdown links that point to repo files
	•	h: parse ## headings → slugify (optional)
	•	ts.c: frontmatter created, else git first-seen (optional)
	•	ts.u: git last-modified (or frontmatter updated)
	•	sz: len(text) (characters)

⸻

Example lines (JSONL)

{"v":1,"id":"202602021430","p":"topics/coaching/most_important_skill_to_learnd.md","t":"The most important skill to learn in the next 10 years","s":"Agency is a durable meta-skill: set direction, act, and iterate without permission despite AI-driven skill churn.","k":["agency","coaching","ai","generalism","learning"],"ty":"evergreen","src":[{"u":"https://x.com/thedankoe/status/2009320195848872014","a":"Dan Koe"}],"ts":{"c":"2026-02-02","u":"2026-02-02"},"sz":1487,"st":"pub"}
{"v":1,"id":"moc-agency","p":"topics/coaching/agency-moc.md","t":"Agency — MOC","s":"Index of agency notes: definitions, practice loops, AI implications, and linked zettels.","k":["agency","coaching"],"ty":"moc","ln":["topics/coaching/most_important_skill_to_learnd.md"],"ts":{"c":"2026-02-02","u":"2026-02-02"},"sz":612,"st":"pub"}
{"v":1,"id":"202601081844","p":"topics/coaching/zettels/202601081844-agency-iterate-without-permission.md","t":"Agency is iteration without permission","s":"Agency is not action but relentless iteration: act, reflect, adjust, repeat until the goal is reached.","k":["agency","iteration"],"ty":"zettel","ts":{"c":"2026-02-02","u":"2026-02-02"},"sz":534,"st":"pub"}


⸻

Optional: a “super-lean” variant (ultra token-efficient)

If you want extreme token savings, you can drop src, ln, h, sz and shorten keys further:

{"v":1,"id":"202602021430","p":"topics/coaching/most_important_skill_to_learnd.md","t":"Most important skill: agency","s":"Agency: set direction, act, iterate without permission; AI changes tools not agency.","k":["agency","ai"],"ty":"e","ts":{"c":"2026-02-02","u":"2026-02-02"},"st":"p"}

But I’d start with the first schema; it’s still small and far more useful.

⸻

Below are three concrete artifacts you can drop into your repo today:
	1.	a human-friendly catalog.md generated from catalog.jsonl
	2.	a minimal frontmatter standard that makes the generator deterministic
	3.	a skills.md skill (“Search Notes”) that teaches an agent to use catalog.jsonl + QMD efficiently

I’m keeping everything plain Markdown + JSONL, no vendor lock-in.

⸻

1) catalog.md (human-friendly view derived from catalog.jsonl)

File: _meta/catalog.md

This file is generated (don’t hand-edit). Humans browse it; agents primarily use catalog.jsonl.

---
title: "Notes Catalog"
generated_from: "_meta/catalog.jsonl"
generated_at: 2026-02-02
purpose: "Human-friendly index of the notes repo"
---

# Notes Catalog

This is an auto-generated index.  
Source of truth: `_meta/catalog.jsonl`.

## Quick links
- [Evergreen](#evergreen)
- [Zettels](#zettels)
- [MOCs](#mocs)
- [Sources](#sources)
- [Meetings](#meetings)
- [Projects](#projects)
- [Inbox / Drafts](#inbox--drafts)
- [Recently updated](#recently-updated)

---

## Recently updated
> Last 30 updates (sorted by `ts.u` desc)

- **2026-02-02** — [The most important skill to learn in the next 10 years](../topics/coaching/most_important_skill_to_learnd.md)  
  *tags:* agency, coaching, ai, generalism, learning  
  *summary:* Agency is a durable meta-skill: set direction, act, and iterate without permission despite AI-driven skill churn.

- **2026-02-02** — [Agency — MOC](../topics/coaching/agency-moc.md)  
  *tags:* agency, coaching  
  *summary:* Index of agency notes: definitions, practice loops, AI implications, and linked zettels.

---

## Evergreen
> Stable “reference” notes (concepts, principles)

- [The most important skill to learn in the next 10 years](../topics/coaching/most_important_skill_to_learnd.md) — *agency, coaching, ai*  
  Agency is a durable meta-skill: set direction, act, and iterate without permission.

---

## Zettels
> Atomic “one claim” notes

- [Agency is iteration without permission](../topics/coaching/zettels/202601081844-agency-iterate-without-permission.md) — *agency, iteration*  
  Agency is not action but relentless iteration: act, reflect, adjust, repeat.

---

## MOCs
> Maps of Content (indexes / hubs)

- [Agency — MOC](../topics/coaching/agency-moc.md) — *agency, coaching*  
  Index note linking agency concepts and zettels.

---

## Sources
> External references (threads, papers, articles)

- [Dan Koe — X thread: “most important skill…”](../topics/coaching/sources/dankoe-x-thread-2009320195848872014.md) — *agency, ai*  
  Source note with references and images.

---

## Meetings
> Meeting notes / logs

- (none yet)

---

## Projects
> Project notes / plans

- (none yet)

---

## Inbox / Drafts
> Unprocessed notes

- (none yet)

---

## Tags
> Top tags (generated). Click to search in your editor.

- agency (12)
- ai (9)
- coaching (6)
- ...

Generation rules (so it stays deterministic)
	•	Group by ty in fixed order: evergreen, zettel, moc, source, meeting, project, log, draft
	•	Under each group, sort by title (t) ascending (stable diff), except:
	•	“Recently updated” section sorts by ts.u desc
	•	Each entry renders:
	•	link: ../ + p
	•	tags: k joined
	•	summary: s
	•	Keep “Tags” only for the top N tags (e.g. 30) to avoid bloat

This file becomes your stable human entry point, while JSONL stays the agent entry point.

⸻

2) Minimal frontmatter standard (deterministic generation)

Goal: allow a generator to extract id/tags/summary/type reliably without LLMs.

Recommended minimal frontmatter (4 fields)

Use this on anything you want indexed well (evergreen/zettels/mocs/sources/projects):

---
id: 202602021430
title: "The most important skill to learn in the next 10 years"
type: evergreen
tags: [agency, coaching, ai, generalism, learning]
summary: "Agency is a durable meta-skill: set direction, act, and iterate without permission despite AI-driven skill churn."
created: 2026-02-02
updated: 2026-02-02
---

Rules
	•	Required: id, title, type, tags, summary
	•	Optional but recommended: created, updated
	•	id must be stable. Suggested: YYYYMMDDHHMM (or a short ULID).
	•	type must be one of:
	•	evergreen | zettel | moc | source | meeting | project | log | draft
	•	tags:
	•	lowercase
	•	hyphenated for multiword tags (agentic-memory)
	•	keep 3–12 tags

Fallback rules (when frontmatter is missing)
If a file has no frontmatter:
	•	id := filename stem
	•	title := first H1 (# ...) else filename
	•	type := inferred by folder (e.g. meetings/ → meeting)
	•	tags := empty
	•	summary := first non-empty paragraph trimmed to 240 chars

This ensures the catalog generator never “guesses”.

⸻

3) A skills.md skill for “Search Notes” using catalog.jsonl + QMD

This is meant to be dropped into a skills folder used by your agent system (OpenClaw or similar). The idea:
	•	Step 0: Use catalog.jsonl as the cheap directory (titles, summaries, tags)
	•	Step 1: Use QMD for fast retrieval of candidate notes (BM25 / optionally vector)
	•	Step 2: Open only the most relevant notes and answer
	•	Step 3: When writing new notes, use the frontmatter template so the catalog stays deterministic

File: skills/search_notes/skills.md

---
name: Search Notes
version: 1
description: >
  Search and retrieve relevant information from the user's git-based markdown notes
  efficiently. Use the catalog first (cheap), then QMD (fast), then open only a
  small number of notes (expensive).
inputs:
  - query: natural language question or keywords
outputs:
  - answer: response grounded in the user's notes
  - citations: list of note paths used
  - next_actions: optional suggestions (create note, link notes, update summary)
tools:
  - qmd (cli): keyword search (BM25), semantic search (optional), get note content
files:
  - _meta/catalog.jsonl
  - _meta/catalog.md
---

# Search Notes

## Operating constraints
- Prefer minimal context usage.
- Do not read many full notes. Start from the catalog and QMD results.
- If no notes match, say so and suggest creating a note.

## Procedure

### 1) Cheap catalog scan (no full note reads)
Read `_meta/catalog.jsonl` (streaming is fine) and do a quick relevance shortlist:
- Match query terms against: `t` (title), `s` (summary), `k` (tags)
- Boost types in this order: `evergreen`, `zettel`, `moc`, `source`, then others
- Prefer smaller notes (`sz`) if available when relevance is similar
- Output a shortlist of 10 candidate `p` paths (or fewer if obvious)

### 2) QMD keyword search (BM25)
Run QMD search over the repo notes:
- Use the query (and/or extracted keywords) with `qmd search`
- Take the top 5–10 hits
- Merge with the catalog shortlist (dedupe paths)

### 3) Retrieve only the best notes
Select up to 3–5 notes to open:
- Prefer hits that appear in both catalog shortlist and QMD results
- Prefer `evergreen`/`zettel` for definitions and claims
- Prefer `moc` to discover additional linked notes when the query is broad

Then open them using `qmd get` (or file read) and extract only the relevant parts.

### 4) Answer with traceability
Produce:
- A concise answer grounded in the notes
- A "Citations" list: the repo-relative paths you used
- If appropriate, point to related notes via links

### 5) Optional: propose improvements
If the query reveals missing knowledge:
- Suggest creating a new evergreen note in `topics/<...>/`
- Use the note template below
- Suggest adding 2–3 links to existing notes

## When to use semantic search
Only if BM25 misses:
- synonyms
- paraphrases
- concepts not named explicitly

Then run `qmd vsearch` (or equivalent) and repeat steps 3–4.

## Note creation template (deterministic catalog ingestion)
When creating a new permanent note, start with:

---
id: <YYYYMMDDHHMM>
title: "<clear, specific title>"
type: evergreen
tags: [tag1, tag2, tag3]
summary: "<one sentence, <=240 chars>"
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <Title>

<content>

## Links
- [Related note](relative/path.md)

Notes about this skill
	•	It does not assume an embedding store exists.
	•	It works entirely with plain files + QMD index.
	•	It stays token efficient by loading:
	1.	catalog lines (cheap)
	2.	QMD hits (cheap)
	3.	only a few full notes (expensive)

---

## How this fits your stack (QMD + OpenClaw + “distributed knowledge”)

### Is QMD sufficient?
For retrieval: **yes**.
- QMD provides the “fast local search + get content” primitives.
- `catalog.jsonl` provides the “cheap directory + ranking” primitive.

You only need a new CLI if you want:
- auto-generation of the catalogs
- automatic extraction of outbound links / heading slugs
- running updates in CI or pre-commit

Those are small scripts, not a new “system”.

### Ingest flow: browser → note
The simplest human-first ingest is:

1. Browser clipper exports Markdown (article body)  
2. Create a file in `inbox/` with minimal template (title + source URL)  
3. Later: distill into an `evergreen` or `zettel`, add summary/tags/links  
4. Generator updates `catalog.jsonl` and `catalog.md`  
5. QMD index updates (`qmd update`)

This keeps capture friction low and quality high.

### Can an OpenClaw bot use this?
Yes, if it can:
- read `_meta/catalog.jsonl`
- run QMD commands (or call the qmd skill)
- read note files

Then the skill above becomes the agent contract.

### “Distributed knowledge” via Moltbook
If Moltbook is your agent-to-agent exchange:
- keep your **repo as the canonical store**
- let agents share **note IDs/paths + short summaries** on Moltbook
- agents can propose patches (PRs) to your repo rather than “publishing knowledge” directly into the shared space

That gives you:
- durable, versioned knowledge
- human review
- clean provenance

---
