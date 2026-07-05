---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [tools, mcp]
---

# Tool System

## Definition

The tool system registers native and MCP tools, filters tool exposure, validates arguments, attaches risk metadata, executes tools, normalizes results and errors, and enforces concurrency rules.

## Why It Matters

The source says coding-critical operations should normally remain native because they need precise control, while MCP should be used for external or organizational integrations. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Native tools likely include file reading/writing, anchored edits, patch application, text and file search, git inspection, git diff, test execution, shell execution, repository metadata, language-service access, and artifact storage.
- MCP tools are appropriate for git hosting, issue trackers, documentation systems, databases, cloud services, browsers, communication systems, and enterprise APIs.
- Tool metadata should describe purpose, schemas, risk category, read-only status, idempotency, parallel safety, timeout, required capabilities, network behavior, credential requirements, and side effects.
- Tool exposure should be filtered by task, agent profile, permission mode, active skills, repository type, relevance, trust level, and sandbox capabilities.
- Tool errors should distinguish invalid arguments, permission denied, approval rejected, timeout, process failure, resource exhaustion, conflict, unsupported capability, transient external errors, permanent external errors, and partial success.

## Related Concepts

- [[policy-and-approval-engine]]
- [[sandboxing]]
- [[standards-at-boundaries]]

## Examples

- `git diff` and anchored edits should be native; opening an issue in a tracker can be provided through MCP but still routed through central policy.

## Contradictions Or Nuance

- MCP improves interoperability, but should not replace the core permission model, filesystem layer, or sandbox.

## Open Questions

- Which tools are mandatory for phase 1?
- How should tool relevance be scored per turn?
