---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [open-questions, design]
---

# Open Design Questions

## Current Thesis

Several decisions remain open, but Tau now resolves the near-term shape: a small layered coding agent with provider streaming, a portable agent core, typed tools, events as the contract, and a coding-app wrapper. Remaining questions should focus first on package naming, loop schema, CLI milestone, built-in tools, sessions, and tests.

## Runtime

- Resolved provisionally: use Python 3.12+ with the stack captured in [Recommended Tech Stack](recommended-tech-stack.md).
- Resolved directionally: follow Tau's local terminal-first coding-agent shape before daemon/service work.
- Should the current single `harness` package stay in place, or should it split into Tau-like layers such as `harness_ai`, `harness_agent`, and `harness_coding`?
- Should the root command remain `harness`, or should product naming change?

## Event Model

- Which events are stable public API?
- How should event schemas be versioned?
- How much model-provider detail should be preserved?
- Should IDs, timestamps, turn indexes, session IDs, usage, and cost be added before the first `AgentHarness` loop?

## Agent Loop

- What is the minimal `AgentHarness` API?
- Should approval and quality-gate hooks be present from the start, or added after the Tau-style loop works?
- Which fake provider and fake tool behaviors are needed for deterministic tests?

## Context

- What token-budget policy should be used?
- How should file relevance be scored?
- When should semantic indexing be introduced?
- How should compaction quality be evaluated?

## Editing

- Which edit primitives should be first-class?
- When should syntax-aware edits be required?
- How should merge conflicts be exposed?
- Should the first Tau-like `edit` tool implement string replacement, patch application, or both?

## CLI And Sessions

- Should the first usable interface be print mode, interactive CLI, or Textual TUI?
- What JSONL record schema should be used for append-only sessions?
- Which session features are first: save, resume, branch, export, or compaction?

## Sandbox

- What is the default local sandbox?
- How should Windows, macOS, and Linux differ?
- Is remote execution a first-release requirement?

## Permissions

- What are the default permission modes?
- Which actions may be approved for the whole session?
- How should organizational policy override user preference?

## Skills

- Which skill locations are supported?
- How are skill versions resolved?
- How are skill scripts trusted?
- Should the harness maintain a skill registry?

## Plugins

- Are plugins loaded in-process or out-of-process?
- How is plugin compatibility managed?
- Is signature verification required?

## Subagents

- When is delegation allowed automatically?
- How are budgets divided?
- How are conflicting findings resolved?
- How are patches merged?

## Memory

- What may be stored automatically?
- What requires approval?
- How is memory deleted or expired?
- How is memory scoped by user, repository, and organization?

## Evaluation

- Which tasks represent the target workload?
- Which metrics determine whether a feature should be retained?
- What is the acceptable cost and latency envelope?

## Supporting Evidence

- The full question set is sourced from the open design questions section of [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).
- Tau contributes the new near-term implementation constraints around layers, events, tools, sessions, and documentation following implementation. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Counterpoints

- Some questions may need provisional answers before coding starts, especially runtime shape, default permission modes, and phase 1 acceptance tasks.

## Changes Over Time

- Initial tracker created from the source document. Future entries should add decisions, evidence, and links to resulting concept or decision pages.
- 2026-07-04: Marked the primary implementation language and initial technology stack as provisionally resolved by [Recommended Tech Stack](recommended-tech-stack.md).
- 2026-07-26: Added Tau-driven questions about package boundaries, loop API, event schema, CLI milestone, coding tools, sessions, and tests.

## Confidence

High that the remaining items are current open questions; medium for the provisional stack answer because it is user-provided project guidance rather than source-derived analysis.

## Open Questions

- Which of these should be promoted into formal architecture decision records first?
