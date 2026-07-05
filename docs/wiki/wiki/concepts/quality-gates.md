---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [quality, verification]
---

# Quality Gates

## Definition

Quality gates are deterministic and structured checks that evaluate whether the requested work is complete and supported by evidence.

## Why It Matters

The source says an agent should not declare success based only on narrative. Completion should be supported by acceptance criteria, checks, diffs, and explicit disclosure of unverified claims. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Significant tasks should have objective, acceptance criteria, constraints, non-goals, and verification expectations.
- Quality gates should check requested behavior, test results, formatting/linting, static-analysis findings, unrelated changes, generated-file handling, documentation updates, unverified claims, evidence for acceptance criteria, and added secrets or sensitive files.
- A quality gate may return structured feedback and request another agent turn.
- The final answer should honestly report changed files, reasons, checks run, check results, failures, assumptions, unverified items, risks, and next actions when incomplete.

## Related Concepts

- [[agent-execution-loop]]
- [[code-editing-reliability]]
- [[persistence-replay-observability]]

## Examples

- If tests were not run, the final answer must not imply that they passed.

## Contradictions Or Nuance

- Plans should remain lightweight and editable; quality gates should verify outcomes without turning every task into a rigid workflow.

## Open Questions

- Which checks are universal defaults?
- How should task-specific acceptance criteria be inferred and corrected?
