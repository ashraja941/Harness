# LLM Wiki Operating Manual

This folder is a portable kit for building and maintaining this LLM-maintained markdown wiki. Follow these rules whenever the user asks you to ingest sources, query this wiki, create pages, or maintain the knowledge base.

## Core Model

There are three layers:

- `raw/`: immutable source material supplied by the user.
- `wiki/`: LLM-generated markdown pages derived from raw sources and user questions.
- `AGENTS.md` plus `templates/`: shared conventions that make the wiki maintainable across sessions and tools.

Do not edit raw source files unless the user explicitly asks. Treat raw files as the source of truth.

## Workspace Layout

The wiki root is the folder containing this `AGENTS.md`, `wiki-kit.json`, `raw/`, `wiki/`, and `templates/`. This copy is intended to live at `docs/wiki/` inside the Harness project, but the folder can be moved as a unit.

Use this structure:

```text
docs/wiki/
  AGENTS.md
  wiki-kit.json
  templates/
  raw/
    assets/
  wiki/
    index.md
    log.md
    overview.md
    sources/
    entities/
    concepts/
    questions/
    synthesis/
    lint-reports/
```

Templates live in `templates/` under the wiki root.

## Naming Conventions

- Use lowercase kebab-case filenames: `retrieval-augmented-generation.md`.
- Prefer stable nouns for entity and concept pages.
- Source summary pages should include a short source identifier, for example `2026-07-04-smith-rag-survey.md`.
- Question pages should start with the date, for example `2026-07-04-how-does-rag-differ-from-wiki-ingestion.md`.
- Use Obsidian-compatible wiki links where useful: `[[retrieval-augmented-generation]]`.
- Use regular markdown links for cross-folder links when clarity matters: `[RAG](../concepts/retrieval-augmented-generation.md)`.

## Page Frontmatter

Use YAML frontmatter for generated wiki pages:

```yaml
---
type: concept
status: draft
created: 2026-07-04
updated: 2026-07-04
sources: []
tags: []
---
```

Use `status: draft` when the page is incomplete or weakly supported. Use `status: active` when it is useful and reasonably sourced. Use `status: needs-review` when there may be contradictions or uncertainty.

## Citation Rules

- Every factual claim that comes from a source should be traceable to a source summary or raw source.
- Prefer citing source summary pages from `wiki/sources/`.
- When needed, also cite raw files using paths relative to the wiki root.
- Do not invent citations.
- If a source is ambiguous, say so directly.

## Ingest Workflow

When the user asks you to ingest a source:

1. Identify the target wiki. If unclear, ask one short clarification question.
2. Read `wiki/index.md`, `wiki/log.md`, and relevant existing pages.
3. Read the raw source from `raw/`.
4. Create or update a source summary in `wiki/sources/` using `templates/source-summary.md`.
5. Extract important entities, concepts, claims, questions, contradictions, and open threads.
6. Create or update relevant pages in `wiki/entities/`, `wiki/concepts/`, and `wiki/synthesis/`.
7. Add cross-links between pages.
8. Update `wiki/index.md`.
9. Append an entry to `wiki/log.md` using the log format below.

Keep updates focused. Do not create many low-value pages for one-off mentions.

## Query Workflow

When the user asks a question about a wiki:

1. Read `wiki/index.md` first.
2. Read relevant pages from the wiki.
3. Read raw sources only when the wiki pages are insufficient or when verifying a precise claim.
4. Answer with citations to wiki pages and raw sources where appropriate.
5. If the answer is reusable, ask whether to save it or save it directly if the user requested a durable wiki update.
6. If saving, create a page in `wiki/questions/`, update `wiki/index.md`, and append to `wiki/log.md`.

## Lint Workflow

When the user asks you to lint or health-check a wiki:

1. Read `wiki/index.md` and recent entries in `wiki/log.md`.
2. Check for orphan pages, missing links, stale claims, contradictions, duplicate pages, missing source citations, and important uncreated concepts.
3. Write a lint report in `wiki/lint-reports/` using `templates/lint-report.md`.
4. Make small safe fixes directly when obvious.
5. List larger proposed fixes separately.
6. Update `wiki/index.md` and append to `wiki/log.md`.

## Log Format

Use append-only entries in `wiki/log.md`:

```markdown
## [YYYY-MM-DD] type | Title

- Wiki: `docs/wiki/`
- Changed: short description
- Pages: page links
- Notes: important decisions or uncertainties
```

Common types: `setup`, `ingest`, `query`, `lint`, `maintenance`, `synthesis`.

## Index Rules

`wiki/index.md` is the navigation hub. Update it whenever pages are added, renamed, or materially changed.

Each index entry should include:

- Link to the page.
- One-line description.
- Optional source count, status, or date.

## Maintenance Principles

- The wiki should compound over time.
- Prefer updating existing pages over creating duplicates.
- Preserve uncertainty and contradictions instead of smoothing them over.
- Keep page content concise but useful.
- Do not let chat-only insights disappear if they should become durable wiki knowledge.
- The best first implementation is markdown and search, not a database.
