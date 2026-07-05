---
type: log
status: active
created: 2026-07-04
updated: 2026-07-04
sources: []
tags: [maintenance]
---

# Harness Wiki Log

## [2026-07-04] setup | Initialize Harness wiki

- Wiki: `wikis/Harness/`
- Changed: Created standard raw/wiki structure, copied the design context into `raw/`, and generated starter source, overview, concept, and synthesis pages.
- Pages: [index](index.md), [overview](overview.md), [source summary](sources/2026-07-04-ai-coding-harness-design-context.md), [recommended architecture](synthesis/recommended-architecture.md), [implementation roadmap](synthesis/implementation-roadmap.md), [open design questions](synthesis/open-design-questions.md)
- Notes: Source file was copied to `raw/ai-coding-harness-design-context.md`; the original root-level file was left untouched.

## [2026-07-04] maintenance | Relocate Harness wiki

- Wiki: `docs/wiki/`
- Changed: Copied the Harness wiki into the Harness project workspace under `docs/wiki/` and added local operating files for standalone use.
- Pages: [index](index.md), [log](log.md), [local README](../README.md)
- Notes: This copy includes `AGENTS.md`, `templates/`, and `wiki-kit.json` so it can be moved or recreated without depending on the original `LLM-KB` repository path.
