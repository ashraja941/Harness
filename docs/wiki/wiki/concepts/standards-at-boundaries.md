---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [standards, interoperability]
---

# Standards At Boundaries

## Definition

Standards at boundaries means adopting open standards where interoperability is valuable while preventing those standards from becoming the harness's internal architecture.

## Why It Matters

The source recommends using `AGENTS.md`, Agent Skills, MCP, ACP, A2A, LSP, OCI concepts, OpenTelemetry, SARIF, and JSON Schema, but frames them as boundary protocols or artifact formats rather than central domain models. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- MCP is an external tool/resource boundary, not the internal tool architecture.
- ACP is a client/editor boundary, not the internal event model.
- A2A is a federation boundary for independent remote agents, not the local subagent scheduler.
- LSP is a language-intelligence boundary, not the repository representation.
- OCI is a sandbox portability concept, not a requirement to hard-code one container engine.
- OpenTelemetry, SARIF, and JSON Schema should normalize observability, analysis findings, tool schemas, structured outputs, plugin manifests, and configuration validation.

## Related Concepts

- [[modular-runtime]]
- [[tool-system]]
- [[skills-and-repository-instructions]]
- [[subagents-and-a2a]]

## Examples

- An editor can speak ACP to the harness while the runtime maintains its own richer event store.
- External issue trackers can be accessed through MCP without bypassing the central permission engine.

## Contradictions Or Nuance

- Standards increase ecosystem compatibility, but premature protocol coupling can reduce control over reliability, safety, and internal evolution.

## Open Questions

- Which protocol-facing event schemas should be stable public API?
- How much provider- or protocol-specific detail should be preserved internally?
