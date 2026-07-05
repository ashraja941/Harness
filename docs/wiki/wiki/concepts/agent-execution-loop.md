---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [runtime, execution]
---

# Agent Execution Loop

## Definition

The agent execution loop is the controlled iterative process that builds context, invokes the model, validates and authorizes tool requests, executes permitted actions, records results, and finishes only when quality criteria are satisfied or a limit is reached.

## Why It Matters

The source says execution policy should remain visible in runtime logic rather than hidden inside prompts. The loop should support streaming, cancellation, time/token/cost/tool/turn limits, retries, resumability, structured errors, parallel read-only work, and serialized mutating operations. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- A normal turn checks limits, builds context, selects relevant permitted tools, calls the model, streams events, collects tool requests, validates and authorizes them, requests approval when needed, executes allowed actions, records results, and feeds results into the next turn.
- The loop should invoke a [[quality-gates]] step before final completion.
- Tool retries should be limited to idempotent operations.
- Mutating operations should be serialized unless isolation makes parallelism safe.

## Related Concepts

- [[modular-runtime]]
- [[tool-system]]
- [[policy-and-approval-engine]]
- [[quality-gates]]

## Examples

- Read-only search and file reads may run in parallel, while writes to the same working tree should be serialized.

## Contradictions Or Nuance

- The loop should be adaptive, but not so model-driven that safety, authorization, cancellation, and completion criteria become implicit.

## Open Questions

- What exact turn limits, retry limits, and cost budgets should be default?
- Which completion criteria should be generic versus task-specific?
