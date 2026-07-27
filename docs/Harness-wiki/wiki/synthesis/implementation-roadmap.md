---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [roadmap, phases]
---

# Implementation Roadmap

## Current Thesis

The implementation should now progress through a Tau-aligned sequence: typed primitives, minimal agent harness loop, deterministic tests, concrete provider adapter, CLI or print mode, built-in coding tools, append-only sessions, then project instructions, skills, context management, and optional TUI/extension work.

## Supporting Evidence

- The source defines Phase 1 as a dependable single-agent runtime focused on provider-neutral model interface, controlled loop, event streaming, repository read/search, safe editing, shell/test execution, git diff, permission engine, basic client, session limits, and final reporting. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).
- Tau provides a concrete smaller build target: provider-neutral event stream, portable agent core, typed tools, agent loop, coding-session wrapper, CLI/TUI, built-in coding tools, project instructions, skills, context accounting, and append-only sessions. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).
- Current Harness implementation has started the typed primitive layer but not the loop, CLI, tools, sessions, or tests. See [Current Implementation Status](current-implementation-status.md).
- The source defines Phase 2 as project-aware behavior with `AGENTS.md`, skill discovery/activation, context budgeting, artifact offloading, structured compaction, goals, acceptance criteria, and quality gates.
- The source defines Phase 3 as durability and isolation with persistent event store, resume, checkpoints, container or remote sandbox, approval caching, hooks, telemetry, and replay.
- The source defines Phase 4 as interoperability with MCP client, ACP server, plugin model, external policy integration, additional sandbox backends, and additional provider adapters.
- The source defines Phase 5 as controlled delegation with agent profiles, subagents, worktree isolation, concurrency controls, structured delegation results, and optional A2A.

## Phase 0: Typed Primitive Foundation

Success condition: provider, message, tool, and event schemas are small, typed, serializable, and tested.

Current status: started.

Primary capabilities:

- Strict wire model base.
- JSON-like value types.
- Human, assistant, and tool-result messages.
- Tool calls, structured tool results, tool executor protocol, and cancellation token protocol.
- Provider-neutral response events.
- Portable agent lifecycle, turn, message, and tool-execution events.

## Phase 1: Minimal Agent Harness Loop

Success condition: a reusable harness can accept a prompt, stream provider events, emit agent events, execute requested fake tools, append results, and continue until the assistant returns no tool calls.

Primary capabilities:

- Provider-neutral model interface.
- Controlled agent loop.
- Event streaming.
- Fake provider and fake tools for deterministic loop tests.
- Final assistant message as authoritative saved output.
- Turn and tool limits.
- Structured errors for provider and tool failures.

## Phase 2: First Usable Coding App

Success condition: the project can be run from a terminal for one-shot prompts against a real model and simple coding tools.

Primary capabilities:

- Concrete provider adapter.
- Minimal CLI or print mode.
- Built-in `read`, `write`, `edit`, and `bash` tools.
- Basic provider/model configuration.
- Plain text or Rich event renderer.
- Tests around serialization, loop behavior, and tool execution.

## Phase 3: Durable Sessions

Success condition: sessions are inspectable, append-only, resumable, and exportable without introducing a database.

Primary capabilities:

- JSONL session history.
- Resume.
- Branching from earlier session points.
- Session metadata.
- Event transcript export.
- Manual compaction entry support.

## Phase 4: Project-Aware Behavior

Success condition: the system works effectively in nontrivial repositories while respecting project rules.

Primary capabilities:

- `AGENTS.md` and project resource support.
- Tau-style skills and prompt templates.
- Context accounting.
- Manual and optional automatic compaction.
- Provider/model catalog.
- TUI or richer interactive session.

## Phase 5: Later Platform Features

Success condition: heavier platform features are added only after the Tau-style coding agent is useful and tested.

Primary capabilities:

- Permission policy and approvals.
- Sandboxing.
- Quality gates.
- MCP and extension interfaces.
- ACP/editor integration.
- Subagents and optional A2A.
- OpenTelemetry or richer observability.

## Counterpoints

- Some phase 3 durability features may be easier to design early as interfaces, but the source discourages adding heavyweight frameworks before requirements justify them.
- Some interoperability work may be useful earlier if editor integration is a primary product goal, but ACP should still remain a client boundary rather than the runtime state model.
- Tau already includes a TUI and durable sessions, but Harness should still build them incrementally because the current code only has typed primitives.

## Changes Over Time

- Initial roadmap copied from the design context and normalized into a reusable wiki page.
- 2026-07-26: Replaced the broad five-phase roadmap with a Tau-aligned implementation sequence and added current status.

## Confidence

High for sequence direction; medium for exact phase boundaries because implementation constraints are unresolved.

## Open Questions

- Which phase 1 features define the first usable milestone?
- Which tasks form the acceptance suite for each phase?
- Which features should be designed as interfaces in phase 1 even if implemented later?
