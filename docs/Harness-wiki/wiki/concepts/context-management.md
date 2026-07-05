---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [context, memory]
---

# Context Management

## Definition

Context management is the harness responsibility for loading instructions, selecting relevant files and artifacts, managing token budgets, activating skills, preserving important state, compacting old information, avoiding redundancy, and tracking provenance.

## Why It Matters

The source identifies context management as a central differentiator. It recommends separating pinned, working, and evictable context; offloading large artifacts; using structured compaction; and tracking provenance so model summaries do not silently replace authoritative sources. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Pinned context includes system policy, user request, acceptance criteria, active repository instructions, active skills, current plan, safety constraints, and unresolved issues.
- Working context includes recently read files, current diff, recent tool results, current test failures, subagent findings, and implementation decisions.
- Evictable context includes old command output, large logs, repeated file contents, completed exploration, earlier failed approaches, and intermediate search results.
- Compacted state should preserve objective, acceptance criteria, instructions, skills, plan, inspected files, changed files, commands, checks, decisions, remaining problems, artifacts, risks, and open questions.
- Stored audit state should include plans, decisions, evidence, assumptions, alternatives at a high level, results, confidence, and unresolved questions, not private chain-of-thought.

## Related Concepts

- [[skills-and-repository-instructions]]
- [[persistence-replay-observability]]
- [[quality-gates]]

## Examples

- A full test log should be stored as an artifact while active context receives an exit code, duration, short summary, relevant excerpt, artifact reference, and truncation status.

## Contradictions Or Nuance

- Full context is simpler and may work for small repositories, but retrieval and compaction scale better when cost, latency, or distraction becomes material.

## Open Questions

- What token-budget policy should be used?
- How should file relevance be scored?
- When should semantic indexing be introduced?
- How should compaction quality be evaluated?
