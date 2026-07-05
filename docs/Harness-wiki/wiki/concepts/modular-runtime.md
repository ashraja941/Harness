---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [runtime, architecture]
---

# Modular Runtime

## Definition

A modular runtime is the central AI coding harness execution layer that operates independently of any specific terminal, editor, web client, or model provider.

## Why It Matters

The source argues that the runtime is the product: clients should start or resume sessions, submit tasks, receive streamed events, approve or reject actions, inspect diffs, cancel work, and review results, but should not directly manage model context or execute tools. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- The runtime should own model orchestration, tool routing, context construction, permission enforcement, quality gates, persistence, and event production.
- Clients should be thin adapters over runtime events and structured state.
- Provider-specific model behavior should be normalized into common concepts such as text, structured output, tool calls, streaming deltas, usage, refusals, context-limit failures, rate-limit failures, and provider errors.
- Capability negotiation is preferred over provider-name checks.

## Related Concepts

- [[standards-at-boundaries]]
- [[agent-execution-loop]]
- [[context-management]]
- [[policy-and-approval-engine]]

## Examples

- A CLI, editor extension, web UI, and automated API client can all communicate with the same runtime rather than each implementing their own tool execution and context policy.

## Contradictions Or Nuance

- The runtime should be custom enough to control reliability-critical behavior, but modular enough that clients, tools, providers, sandboxes, and policy modules can be replaced.

## Open Questions

- Should the runtime be a local process, daemon, service, or support all three?
- How should clients discover and connect to the runtime?
