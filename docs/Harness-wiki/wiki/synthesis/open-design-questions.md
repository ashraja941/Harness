---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [open-questions, design]
---

# Open Design Questions

## Current Thesis

Several decisions should remain open until implementation constraints are clearer. The source explicitly leaves runtime, event model, context, editing, sandbox, permissions, skills, plugins, subagents, memory, and evaluation questions unresolved.

## Runtime

- Resolved provisionally: use Python 3.12+ with the stack captured in [Recommended Tech Stack](recommended-tech-stack.md).
- Should the runtime be a local process, daemon, service, or support all three?
- How should clients discover and connect to the runtime?

## Event Model

- Which events are stable public API?
- How should event schemas be versioned?
- How much model-provider detail should be preserved?

## Context

- What token-budget policy should be used?
- How should file relevance be scored?
- When should semantic indexing be introduced?
- How should compaction quality be evaluated?

## Editing

- Which edit primitives should be first-class?
- When should syntax-aware edits be required?
- How should merge conflicts be exposed?

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

## Counterpoints

- Some questions may need provisional answers before coding starts, especially runtime shape, default permission modes, and phase 1 acceptance tasks.

## Changes Over Time

- Initial tracker created from the source document. Future entries should add decisions, evidence, and links to resulting concept or decision pages.
- 2026-07-04: Marked the primary implementation language and initial technology stack as provisionally resolved by [Recommended Tech Stack](recommended-tech-stack.md).

## Confidence

High that the remaining items are current open questions; medium for the provisional stack answer because it is user-provided project guidance rather than source-derived analysis.

## Open Questions

- Which of these should be promoted into formal architecture decision records first?
