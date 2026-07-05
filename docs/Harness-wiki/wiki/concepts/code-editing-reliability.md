---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [editing, reliability]
---

# Code Editing Reliability

## Definition

Code editing reliability is the harness's ability to apply targeted, verifiable, reversible code changes while avoiding accidental or unrelated modifications.

## Why It Matters

The source says edit quality is a core reliability feature and recommends targeted edits over arbitrary full-file regeneration. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Preferred edit modes include anchored replacement, structured patch application, syntax-aware replacement, justified full-file replacement, and generated-file updates through project generators.
- Before editing, the harness should verify that the file still matches what the model inspected, the target exists, the target is unambiguous, the path is allowed, the file is not generated or protected, and the edit does not cross workspace boundaries.
- After editing, the harness should produce a diff, validate syntax where practical, track inverse changes, detect unexpected modifications, make rollback possible, and run relevant formatting or tests based on policy.
- Two writing agents should not modify the same working tree without explicit coordination.

## Related Concepts

- [[quality-gates]]
- [[tool-system]]
- [[sandboxing]]

## Examples

- Safer multi-agent editing options include isolated worktrees, isolated branches, file ownership, serialized writes, and patch-only subagent output.

## Contradictions Or Nuance

- Full-file replacement may be valid, but only when justified by the task and protected by verification.

## Open Questions

- Which edit primitives should be first-class?
- When should syntax-aware edits be required?
- How should merge conflicts be exposed?
