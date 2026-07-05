---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [persistence, replay, observability]
---

# Persistence Replay Observability

## Definition

Persistence, replay, and observability are the harness capabilities that make sessions resumable, actions auditable, behavior debuggable, and evaluations repeatable.

## Why It Matters

The source recommends append-oriented event storage, replay records, OpenTelemetry, and enough structured information to answer what the model received, which instructions and tools were active, what actions were attempted, why policy decisions were made, what changed, which checks ran, and why completion was claimed. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Session persistence should survive client disconnects, runtime restarts, tool failures, model failures, user pauses, and approval delays.
- Events may include user messages, model events, tool calls/results, policy decisions, approvals, compaction, skill activation, file changes, checkpoints, quality results, and final outcome.
- Replay records should preserve normalized model requests, model response events, tool schemas, tool calls/results, instruction and skill hashes, policy and approval decisions, environment fingerprint, sandbox identity, repository state, artifacts, timing, and cost.
- OpenTelemetry is the preferred standard for traces, metrics, and logs.
- Observability should redact secrets, full credentials, and unnecessary source code by default.

## Related Concepts

- [[context-management]]
- [[quality-gates]]
- [[sandboxing]]

## Examples

- Replay modes may reuse recorded model output while rerunning tools, reuse both model and tool output, replay context construction, replay authorization decisions, or compare two models on the same recorded environment.

## Contradictions Or Nuance

- Replay and observability should not require storing private chain-of-thought.

## Open Questions

- Which events are stable public API?
- How should event schemas be versioned?
- What source-code and secret redaction defaults are acceptable?
