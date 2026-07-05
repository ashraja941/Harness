---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [subagents, a2a, delegation]
---

# Subagents And A2A

## Definition

Subagents are bounded delegated workers inside the harness, while A2A should be reserved for remote, independently operated agents with their own identity, lifecycle, authentication, task state, streaming, failure behavior, and trust domain.

## Why It Matters

The source recommends reliable single-agent behavior before multi-agent orchestration and warns against using subagents to compensate for weak context selection, search, editing, testing, planning, or verification. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Subagents are useful for repository exploration, independent review, test failure analysis, documentation research, security review, comparing options, and isolated module work.
- Subagents should reuse the same runtime, receive limited context and tools, have explicit budgets, limited recursion depth, structured results, preserved evidence, and visible activity.
- Writing subagents should avoid shared-state editing unless isolated.
- Reasonable defaults include no automatic delegation unless justified, low maximum depth, small concurrency limits, separate worktrees for writing tasks, serialized merge or patch review, and parent responsibility for final quality.
- A subagent result should include summary, evidence, files inspected, files changed, tests run, artifacts, unresolved issues, confidence, and suggested next action.

## Related Concepts

- [[modular-runtime]]
- [[context-management]]
- [[quality-gates]]

## Examples

- Local repository exploration can use internal subagents; a cloud-hosted organization-specific analysis service may justify A2A.

## Contradictions Or Nuance

- Multi-agent work can improve parallel investigation and review, but adds cost, latency, merge conflicts, debugging complexity, and context-management complexity.

## Open Questions

- When is delegation allowed automatically?
- How are budgets divided?
- How are conflicting findings resolved?
- How are patches merged?
