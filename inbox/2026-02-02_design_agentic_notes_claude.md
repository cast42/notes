---
title: "Agentic Notes System: A Practical Proposal"
date: 2026-02-02
type: inbox
topics:
  - inbox
tags: []
---

# Agentic Notes System: A Practical Proposal

## Executive Summary

This proposal outlines a **dual-view** note-taking system that prioritizes human usability while enabling efficient agent interaction. The core insight: keep notes human-readable in your existing workflow, but add a thin semantic layer that agents can exploit without changing how you work.

**Key principles:**
1. Human-first: Notes remain simple markdown, editable anywhere
2. Agent-augmented: Structured metadata enables intelligent retrieval
3. Tool-minimal: qmd is sufficient with one small addition
4. Future-proof: Plain text + git = eternal accessibility

---

## Part 1: Research Findings

### 1.1 What TypeAgent-py/Structured RAG Teaches Us

TypeAgent-py's approach extracts **structured knowledge** from documents:
- Entities (people, concepts, tools)
- Relationships (uses, depends-on, relates-to)
- Temporal context (when discovered, last verified)

**Key insight**: The extraction happens at *ingest time*, not query time. This means humans write natural notes, and the system builds structure in the background.

### 1.2 What A-MEM/Zettelkasten Teaches Us

The A-MEM paper (NeurIPS 2025) implements Zettelkasten principles for agents:

| Zettelkasten Principle | A-MEM Implementation | Our System |
|------------------------|----------------------|------------|
| Atomic notes | Single-concept memories | One idea per file |
| Explicit links | Bi-directional `[[links]]` | Standard wiki-links |
| Tags/keywords | LLM-generated metadata | YAML frontmatter |
| Context descriptions | Generated summaries | Optional `_agent/` shadow |
| Evolution | Updates to old notes | Git history + backlinks |

**Key insight**: Agents benefit from *rich context* around notes (keywords, summaries, relationships), but humans shouldn't have to write this metadata manually.

### 1.3 What qmd Already Provides

Tobi's qmd is remarkably complete for your needs:
- **BM25 search**: Fast keyword matching
- **Vector search**: Semantic similarity via local embeddings
- **Hybrid search**: Best-of-both with reranking
- **MCP server**: Direct integration with Claude/OpenClaw
- **Collections**: Separate indexes for different knowledge bases

**What's missing**: qmd doesn't generate agent-optimized metadata during ingest. It searches what exists, but doesn't augment it.

### 1.4 What OpenClaw/Moltbook Shows About Distributed Knowledge

OpenClaw agents can share knowledge via:
- Skills (SKILL.md format) - instructions and procedures
- Moltbook posts - observations and experiences
- MCP tools - direct data access

**Key insight for distributed KB**: Knowledge can be partitioned:
- **Personal vault** → qmd index (your notes)
- **Shared skills** → OpenClaw skills folder
- **Public observations** → Moltbook (optional)

---

## Part 2: Proposed System Architecture

### 2.1 Directory Structure

```
notes/
├── inbox/                    # Capture first, organize later
│   └── 2026-02-02.md        # Daily scratchpad
├── topics/                   # Evergreen knowledge (Zettelkasten)
│   ├── rag.md
│   ├── embeddings.md
│   └── procurement/
│       └── drempelwaardes.md
├── refs/                     # External references
│   ├── papers/
│   └── links/
├── meetings/                 # Dated meeting notes
│   └── 2026-02-02-standup.md
├── _agent/                   # SHADOW: Agent-optimized metadata
│   ├── index.json           # Extracted entities & relationships
│   ├── summaries/           # LLM-generated note summaries
│   └── graph.json           # Relationship graph for traversal
├── _meta/
│   ├── tags.md              # Tag taxonomy
│   └── conventions.md       # Note-taking conventions
└── qmd.yaml                  # qmd configuration
```

### 2.2 The Dual-View Concept

**Human View** (what you see and edit):
```markdown
# RAG Implementation Patterns

Related: [[embeddings]], [[vector-databases]]
Tags: #ai #retrieval #implementation

## Key Concepts

Chunking strategy matters more than model choice for most use cases.
Overlap of 10-15% between chunks preserves context boundaries.

## Links
- TypeAgent-py: https://github.com/microsoft/typeagent-py
```

**Agent View** (generated in `_agent/summaries/rag.json`):
```json
{
  "source": "topics/rag.md",
  "title": "RAG Implementation Patterns",
  "summary": "Practical patterns for implementing RAG systems with focus on chunking strategies",
  "entities": ["RAG", "chunking", "embeddings", "TypeAgent-py"],
  "relationships": [
    {"type": "relates_to", "target": "embeddings.md"},
    {"type": "relates_to", "target": "vector-databases.md"},
    {"type": "references", "target": "https://github.com/microsoft/typeagent-py"}
  ],
  "keywords": ["chunking", "overlap", "retrieval", "implementation"],
  "updated": "2026-02-02T10:30:00Z",
  "token_estimate": 450
}
```

### 2.3 Why This Works

| Human Concern | Solution |
|---------------|----------|
| "I want to edit in VS Code" | Plain markdown, no special syntax required |
| "I want to sync with git" | All files are text, git-friendly |
| "I don't want lock-in" | Standard formats, no database |
| "I want it to work offline" | qmd runs locally |

| Agent Concern | Solution |
|---------------|----------|
| "I need semantic search" | qmd vsearch + embeddings |
| "I need relationship traversal" | `_agent/graph.json` |
| "I need summaries for context" | `_agent/summaries/*.json` |
| "I need efficient retrieval" | Pre-computed metadata |

---

## Part 3: Implementation Details

### 3.1 Note Format Conventions

**Minimal frontmatter** (for humans who want it):
```yaml
---
tags: [ai, rag, implementation]
created: 2026-02-02
---
```

**Wiki-links** for relationships:
```markdown
This relates to [[embeddings]] and [[vector-databases]].
```

**Sections** for structure:
```markdown
## Key Concepts
## Examples  
## Links
## Open Questions
```

### 3.2 The Agent Metadata Generator

A small CLI tool that runs periodically (via cron or git hook):

```python
#!/usr/bin/env python3
"""notes-agent-index: Generate agent-optimized metadata for notes."""

import json
from pathlib import Path
from datetime import datetime

def extract_links(content: str) -> list[str]:
    """Extract [[wiki-links]] from markdown."""
    import re
    return re.findall(r'\[\[([^\]]+)\]\]', content)

def extract_tags(content: str) -> list[str]:
    """Extract #tags from markdown."""
    import re
    return re.findall(r'#(\w+)', content)

def generate_summary(filepath: Path, content: str) -> dict:
    """Generate agent metadata for a note.
    
    For production: call LLM to generate summary + entities.
    For MVP: extract what we can statically.
    """
    links = extract_links(content)
    tags = extract_tags(content)
    title = content.split('\n')[0].lstrip('# ').strip()
    
    return {
        "source": str(filepath),
        "title": title,
        "links": links,
        "tags": tags,
        "updated": datetime.now().isoformat(),
        "char_count": len(content),
    }

def build_graph(summaries: list[dict]) -> dict:
    """Build relationship graph from summaries."""
    nodes = {}
    edges = []
    
    for s in summaries:
        nodes[s["source"]] = {"title": s["title"], "tags": s["tags"]}
        for link in s.get("links", []):
            edges.append({"from": s["source"], "to": link, "type": "links_to"})
    
    return {"nodes": nodes, "edges": edges}
```

**Usage**: 
```bash
# Run after note changes (git post-commit hook)
notes-agent-index ~/notes

# Or via qmd update hook (proposed enhancement)
qmd update --post-hook "notes-agent-index ."
```

### 3.3 Enhanced qmd Configuration

```yaml
# ~/notes/qmd.yaml
collections:
  - name: notes
    path: ~/notes
    glob: "**/*.md"
    exclude: ["_agent/**", "_meta/**"]
    
  - name: agent-meta
    path: ~/notes/_agent
    glob: "**/*.json"

contexts:
  - path: "topics/"
    description: "Evergreen knowledge notes on various topics"
  - path: "inbox/"
    description: "Daily capture and scratchpad notes"
  - path: "meetings/"
    description: "Meeting notes with dates"
  - path: "_agent/"
    description: "Agent-optimized metadata (auto-generated)"
```

### 3.4 Agent Retrieval Flow

When an agent (Claude/OpenClaw) needs information:

```
1. User query: "How should I implement chunking for RAG?"
          │
          ▼
2. qmd query "chunking RAG implementation"
          │
          ▼
3. Results: [topics/rag.md, refs/papers/typeagent.md]
          │
          ▼
4. Load _agent/summaries/rag.json for context
          │
          ▼
5. Follow graph edges: rag → embeddings → vector-databases
          │
          ▼
6. Agent has: original note + summary + related notes
```

---

## Part 4: SKILL.md for Notes Interaction

Create this as a skill for OpenClaw/Claude:

```markdown
---
name: personal-notes
description: Search and interact with personal knowledge base using qmd. 
  Use when user asks about their notes, past learnings, or wants to 
  find/create documentation. Triggers on: "my notes", "what do I know about",
  "find my notes on", "add to my notes", "search my knowledge base".
---

# Personal Notes Skill

## Search Notes

Use qmd MCP tools:
- `qmd:search` for keyword search
- `qmd:vsearch` for semantic search  
- `qmd:query` for best quality (hybrid + rerank)
- `qmd:get` to retrieve full note content

## Create Notes

When user wants to capture knowledge:

1. Determine appropriate location:
   - New learning → `inbox/YYYY-MM-DD.md` 
   - Evergreen concept → `topics/{concept}.md`
   - Meeting notes → `meetings/YYYY-MM-DD-{title}.md`
   - External reference → `refs/{type}/{name}.md`

2. Use this template:
   ```markdown
   # {Title}

   Related: [[link1]], [[link2]]
   Tags: #tag1 #tag2

   ## Summary
   {One paragraph overview}

   ## Details
   {Main content}

   ## Links
   - {External references}
   ```

3. After creating, run: `notes-agent-index ~/notes`

## Agent Metadata

Check `_agent/summaries/{note}.json` for pre-computed:
- Keywords and entities
- Relationship graph
- Token estimates

## Conventions

- One concept per note (atomic)
- Use [[wiki-links]] for connections
- Prefer linking over duplicating
- Capture first in inbox, organize later
```

---

## Part 5: Ingestion Flows

### 5.1 Browser Capture (via extension)

**Option A: Existing tools (recommended)**

Use a simple bookmarklet or extension that:
1. Captures URL + title + selected text
2. Appends to `inbox/YYYY-MM-DD.md`
3. Triggers sync (if using git auto-commit)

Example bookmarklet:
```javascript
javascript:(function(){
  const text = window.getSelection().toString();
  const url = window.location.href;
  const title = document.title;
  const note = `\n## ${title}\n${text}\n- Source: ${url}\n`;
  navigator.clipboard.writeText(note);
  alert('Copied to clipboard - paste into inbox');
})();
```

**Option B: Custom extension (future)**

A browser extension could:
1. Detect when you're reading something interesting
2. Generate a structured note via API call
3. Create file directly in notes repo
4. Trigger `notes-agent-index`

### 5.2 Command Line Capture

```bash
# Quick capture to inbox
alias note='echo "## $(date +%H:%M) - " >> ~/notes/inbox/$(date +%Y-%m-%d).md && $EDITOR +999 ~/notes/inbox/$(date +%Y-%m-%d).md'

# Create topic note
notes-new() {
  local topic="$1"
  local file=~/notes/topics/${topic}.md
  cat > "$file" << EOF
# ${topic}

Related: 
Tags: 

## Summary

## Details

## Links
EOF
  $EDITOR "$file"
  notes-agent-index ~/notes
}
```

### 5.3 Agent-Initiated Capture

When Claude/OpenClaw learns something useful:

```markdown
User: "Remember that the procurement threshold for EU tenders is €140,000"

Agent action:
1. Search existing notes: qmd:search "procurement threshold"
2. If exists: append to existing note
3. If not: create topics/procurement/thresholds.md
4. Update _agent/ metadata
```

---

## Part 6: Distributed Knowledge via OpenClaw

### 6.1 Personal vs Shared Knowledge

```
┌─────────────────────────────────────────────────────┐
│                   Your Knowledge                     │
├─────────────────────────────────────────────────────┤
│  ~/notes/              │  ~/.openclaw/skills/       │
│  ├── topics/           │  ├── personal-notes/       │
│  ├── inbox/            │  │   └── SKILL.md          │
│  └── _agent/           │  └── dataroots-patterns/   │
│                        │      └── SKILL.md          │
│  [Private, local]      │  [Shareable procedures]    │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│              Moltbook (Optional, Public)             │
├─────────────────────────────────────────────────────┤
│  - Observations from your agent                     │
│  - Learnings worth sharing                          │
│  - NOT private notes                                │
└─────────────────────────────────────────────────────┘
```

### 6.2 Moltbook Integration (Optional)

If you want your agent to share learnings publicly:

```python
# In OpenClaw skill
def share_to_moltbook(learning: str, is_public: bool = False):
    """Share a learning to Moltbook if appropriate."""
    if not is_public:
        return  # Keep private by default
    
    # Only share:
    # - General technical learnings
    # - Tool tips and tricks
    # - NOT personal or work-specific info
    
    moltbook.post(content=learning, tags=["technical", "tip"])
```

**Warning**: Moltbook is public and has security concerns. Use only for general knowledge you'd share on a blog.

### 6.3 Multi-Agent Knowledge Sharing

For sharing between your devices/agents:

```yaml
# ~/notes/qmd.yaml - multi-device setup
collections:
  - name: personal
    path: ~/notes
    sync: git  # git push/pull for sync
    
  - name: shared-team
    path: ~/team-notes  
    sync: git  # shared repo with colleagues
    read_only: true  # don't modify team notes
```

---

## Part 7: Comparison with Alternatives

| Approach | Human-Friendly | Agent-Efficient | Durability | Complexity |
|----------|---------------|-----------------|------------|------------|
| **This proposal** | ✅ Plain markdown | ✅ Via `_agent/` | ✅ Plain text | Low |
| Obsidian + plugins | ✅ Great UI | ⚠️ Plugin-dependent | ⚠️ Plugin ecosystem | Medium |
| Full knowledge graph | ⚠️ Graph UI learning | ✅ Native | ⚠️ Database | High |
| mem0/Graphiti | ❌ API-only | ✅ Optimized | ⚠️ Service dependency | Medium |
| Claude memory | ✅ Automatic | ✅ Built-in | ❌ Platform-locked | Low |

---

## Part 8: Implementation Roadmap

### Phase 1: MVP (Now)
- [x] Use existing notes structure
- [x] Configure qmd with collections
- [ ] Create basic `notes-agent-index` script
- [ ] Write SKILL.md for OpenClaw/Claude

### Phase 2: Enhancement (Week 2)
- [ ] Add LLM-powered summary generation to indexer
- [ ] Build relationship graph visualization
- [ ] Create browser bookmarklet for capture

### Phase 3: Integration (Month 1)
- [ ] OpenClaw skill for full notes interaction
- [ ] Git hooks for automatic indexing
- [ ] Optional Moltbook sharing for public learnings

### Phase 4: Polish (Month 2+)
- [ ] Mobile capture workflow
- [ ] Team sharing via git repos
- [ ] Metrics on note usage and retrieval quality

---

## Part 9: Answers to Your Questions

### Is qmd sufficient?

**Yes, with one addition.** qmd handles search/retrieval excellently. The missing piece is the `_agent/` metadata layer that provides:
- Pre-computed summaries (token-efficient context)
- Relationship graph (multi-hop traversal)
- Entity extraction (structured queries)

This can be a simple Python script that runs post-commit.

### Is a browser plugin needed?

**Not required, but helpful.** Options:
1. **Minimal**: Bookmarklet → clipboard → paste to inbox
2. **Better**: Obsidian web clipper or similar
3. **Best**: Custom extension that creates notes directly

### Can this work with OpenClaw?

**Yes.** Create a SKILL.md that:
1. Uses qmd MCP tools for search
2. Reads `_agent/` metadata for context
3. Creates notes following conventions

### Can this interoperate with Moltbook?

**Partially.** Keep separation:
- Personal notes → local qmd
- Shareable procedures → OpenClaw skills
- Public observations → Moltbook (carefully)

Moltbook is essentially a public scratchpad. Don't put private or work notes there.

### What prompts are needed for ingestion?

For the metadata generator, use this prompt:

```
Given this markdown note, extract:
1. A one-sentence summary (max 100 chars)
2. Key entities (people, tools, concepts)
3. Keywords for retrieval (5-10)
4. Relationships to other notes (if [[links]] present)

Note content:
{note_content}

Respond in JSON format only.
```

---

## Conclusion

The optimal system is **simple by design**:

1. **Write notes normally** in markdown with wiki-links
2. **Let qmd search** with hybrid BM25 + vector
3. **Generate `_agent/` metadata** periodically for agent efficiency
4. **Share procedures via SKILL.md**, not raw notes

This approach:
- ✅ Works with your existing setup
- ✅ Requires minimal new tooling
- ✅ Remains human-readable and editable
- ✅ Enables sophisticated agent retrieval
- ✅ Survives tool/platform changes (plain text forever)

The complexity ceiling is low, the durability ceiling is high, and you can evolve it incrementally.
