---
type: synthesis
status: active
created: 2026-07-26
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [implementation, status, tau]
---

# Current Implementation Status

## Current Thesis

Harness is in the earliest Tau-aligned implementation slice. The code currently defines provider, message, tool, event, and wire-model primitives, but it does not yet implement a complete coding agent loop, CLI, provider adapter, built-in coding tools, sessions, or tests.

## Implemented

- `src/harness/agent/base.py` defines `WireModel`, a strict Pydantic base model with camel-case wire aliases.
- `src/harness/agent/types.py` defines JSON-like type aliases for tool arguments, tool data, and structured event payloads.
- `src/harness/agent/messages.py` defines `HumanMessage`, `AssistantMessage`, `ToolResultMessage`, and the `AgentMessage` union.
- `src/harness/agent/tools.py` defines `ToolCall`, `AgentToolResult`, `AgentTool`, `ToolExecutor`, and `ToolCancellationToken`.
- `src/harness/agent/events.py` defines initial portable agent events for agent start/end, turn start/end, message lifecycle, and tool execution lifecycle.
- `src/harness/ai/events.py` defines provider-neutral response start/end, text delta, and tool-call events.
- `src/harness/ai/provider.py` defines a `ModelProvider` protocol with `stream_response` returning provider events.

## Not Yet Implemented

- `AgentHarness` or equivalent reusable loop.
- Concrete provider adapters.
- CLI beyond the placeholder `harness` script that prints `Hello from harness!`.
- TUI, print mode, slash commands, or renderers.
- Built-in coding tools such as `read`, `write`, `edit`, and `bash`.
- Durable session storage, resume, branching, export, or compaction.
- Project instruction loading from `AGENTS.md`, `.tau/`, or equivalent project resources.
- Tests under `tests/`.
- A Tau-like package split between provider, agent, and coding-app layers.

## Supporting Evidence

- Tau identifies provider streaming, portable agent core behavior, coding-app wrapping, typed events, ordinary typed tools, and durable sessions as the important architectural pieces. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).
- The current source tree contains only `src/harness/ai` and `src/harness/agent` primitives plus an empty root README and placeholder CLI entry point.

## Counterpoints

- The existing single `harness` package can still follow Tau's dependency boundary internally before committing to separate installable packages.
- Some originally planned platform features remain useful later, but documenting them as current implementation would mislead future work.

## Changes Over Time

- 2026-07-26: Added current implementation status after comparing the committed Python scaffolding with Tau's architecture.

## Confidence

High for current implementation status based on the repository files. Medium for next-step ordering because package naming and command naming remain unresolved.

## Open Questions

- Should tests be added before the first concrete provider adapter?
- Should `AgentHarness` live under `harness.agent` first, or should the package split happen before implementing the loop?
- Should event schemas add IDs, timestamps, and session metadata before persistence work begins?
