---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [runtime, execution]
---

# Agent Execution Loop

## Definition

The agent execution loop is the controlled iterative process that sends the current system prompt, transcript, tools, and model choice to a provider; streams a response; emits events; executes requested tools; appends tool results; and repeats until the assistant produces no more tool calls or a limit is reached.

## Why It Matters

The original design context says execution policy should remain visible in runtime logic rather than hidden inside prompts. Tau provides the immediate implementation reference: the loop is the small reusable engine that turns messages, tools, and provider streams into progress events. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md) and [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Current Understanding

- A minimal Tau-style turn takes the current system prompt, transcript, tools, and model selection, asks the provider to stream a response, emits message events, collects the assistant message, executes requested tools, appends tool results, and repeats.
- The final `AssistantMessage` should be authoritative for persisted text, thinking, and tool calls; streaming update events are for responsive rendering.
- Frontends should render from provider-neutral agent events rather than raw provider chunks.
- Advanced approval, quality-gate, retry, and parallelism policy can be added after the minimal loop is reliable.

## Implementation Status

- Current code defines initial provider events, agent events, message types, tool types, and a provider protocol.
- Current code does not yet define an `AgentHarness` loop or deterministic loop tests.

## Related Concepts

- [[modular-runtime]]
- [[tool-system]]
- [[policy-and-approval-engine]]
- [[quality-gates]]
- [[tau-alignment]]

## Examples

- Read-only search and file reads may run in parallel, while writes to the same working tree should be serialized.

## Contradictions Or Nuance

- The loop should be adaptive, but not so model-driven that safety, authorization, cancellation, and completion criteria become implicit.

## Open Questions

- Which event fields are needed before the first loop implementation: IDs, timestamps, turn indexes, session IDs, usage, or cost?
- Should approval and quality-gate hooks exist in the first loop, or be added after the basic Tau-style loop works?
