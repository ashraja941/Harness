---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [persistence, replay, observability]
---

# Persistence Replay Observability

## Definition

Persistence, replay, and observability are the harness capabilities that make sessions resumable, actions inspectable, behavior debuggable, and frontend rendering independent from raw provider APIs.

## Why It Matters

The original design context recommends append-oriented event storage, replay records, OpenTelemetry, and enough structured information to explain model inputs, active tools, actions, checks, and completion claims. Tau provides a smaller first target: append-only JSONL sessions, event-driven rendering, resume, branching, export, and compaction without rewriting history. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md) and [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Current Understanding

- The first persistence format should be append-only JSONL, not SQLite.
- The event stream should be the first observability surface for CLI, print mode, TUI, custom frontends, and tests.
- Saved sessions should preserve finalized messages and tool results; streaming update events can be transient unless needed for transcripts.
- Compaction should add summary entries rather than rewriting original history.
- OpenTelemetry, replay modes, and database-backed event stores should wait until the basic session model works.

## Implementation Status

- Current code defines event schemas but does not yet persist events or sessions.
- Current event schemas do not yet include session IDs, turn indexes, timestamps, usage, cost, or schema versions.

## Related Concepts

- [[context-management]]
- [[quality-gates]]
- [[sandboxing]]
- [[tau-alignment]]

## Examples

- A first session file can append user messages, finalized assistant messages, tool results, compaction summaries, and session metadata as JSONL records.

## Contradictions Or Nuance

- Replay and observability should not require storing private chain-of-thought. Tau-style thinking support should be modeled explicitly only when the active provider exposes it safely.

## Open Questions

- Which records belong in durable JSONL sessions versus transient frontend streams?
- Should event schema versions be added before the first persisted session format?
- What source-code and secret redaction defaults are acceptable?
