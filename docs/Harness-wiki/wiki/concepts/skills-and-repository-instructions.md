---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [agents-md, skills, instructions]
---

# Skills And Repository Instructions

## Definition

Repository instructions and skills are separate customization mechanisms: `AGENTS.md` defines repository-specific rules, while Agent Skills define reusable procedures for classes of tasks.

## Why It Matters

The source warns that `AGENTS.md`, skills, tools, hooks, plugins, and memory should not be merged because they serve different purposes and have different trust boundaries. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- `AGENTS.md` should contain repository purpose, directory responsibilities, build/test commands, linting expectations, architecture constraints, generated-file warnings, dependency rules, sensitive areas, PR expectations, conventions, and protected areas.
- `AGENTS.md` should not become a general prompt dump, tutorial, API dump, temporary task log, secret store, credential store, or place for unverified model-generated knowledge.
- Instruction loading should support user-level global instructions, repository-root instructions, nested instructions, closest-scope precedence, user override, loaded-file reporting, and conflict detection.
- Skills should follow the Agent Skills specification and use progressive disclosure: discover metadata first, activate relevant skills only when needed, load instructions on activation, and load references only when required.
- Skills can contain powerful instructions and scripts, so trust should account for source, permissions, script approval, versions, hashes, compatibility, credentials, and network use.

## Related Concepts

- [[context-management]]
- [[policy-and-approval-engine]]
- [[standards-at-boundaries]]

## Examples

- A repository rule saying “run `npm test` before finalizing” belongs in `AGENTS.md`; a reusable procedure for diagnosing failing Python test suites belongs in a skill.

## Contradictions Or Nuance

- Instruction files can guide the model, but they are untrusted until the repository is trusted and must not become executable security policy.

## Open Questions

- Which skill locations are supported?
- How are skill versions resolved?
- How are skill scripts trusted?
- Should the harness maintain a skill registry?
