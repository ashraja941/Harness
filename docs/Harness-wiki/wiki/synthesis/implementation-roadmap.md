---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [roadmap, phases]
---

# Implementation Roadmap

## Current Thesis

The implementation should progress through five capability phases: dependable single-agent runtime, project-aware behavior, durability and isolation, interoperability, and controlled delegation.

## Supporting Evidence

- The source defines Phase 1 as a dependable single-agent runtime focused on provider-neutral model interface, controlled loop, event streaming, repository read/search, safe editing, shell/test execution, git diff, permission engine, basic client, session limits, and final reporting. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).
- The source defines Phase 2 as project-aware behavior with `AGENTS.md`, skill discovery/activation, context budgeting, artifact offloading, structured compaction, goals, acceptance criteria, and quality gates.
- The source defines Phase 3 as durability and isolation with persistent event store, resume, checkpoints, container or remote sandbox, approval caching, hooks, telemetry, and replay.
- The source defines Phase 4 as interoperability with MCP client, ACP server, plugin model, external policy integration, additional sandbox backends, and additional provider adapters.
- The source defines Phase 5 as controlled delegation with agent profiles, subagents, worktree isolation, concurrency controls, structured delegation results, and optional A2A.

## Phase 1: Dependable Single-Agent Runtime

Success condition: the system reliably completes small repository tasks without unsafe actions or unexplained changes.

Primary capabilities:

- Provider-neutral model interface.
- Controlled agent loop.
- Event streaming.
- Repository reading and search.
- Safe editing.
- Shell and test execution.
- Git diff.
- Permission engine.
- Basic client.
- Session limits.
- Clear final reporting.

## Phase 2: Project-Aware Behavior

Success condition: the system works effectively in nontrivial repositories while respecting project rules.

Primary capabilities:

- `AGENTS.md` support.
- Skill discovery and activation.
- Context budgeting.
- Artifact offloading.
- Structured compaction.
- Goals and acceptance criteria.
- Quality gates.

## Phase 3: Durability And Isolation

Success condition: the system survives interruption, supports debugging, and runs with meaningful isolation.

Primary capabilities:

- Persistent event store.
- Resume.
- Checkpoints.
- Container or remote sandbox.
- Approval caching.
- Hooks.
- Telemetry.
- Replay.

## Phase 4: Interoperability

Success condition: the system integrates with editors, services, and organization-specific tooling without core modification.

Primary capabilities:

- MCP client.
- ACP server.
- Plugin model.
- External policy integration.
- Additional sandbox backends.
- Additional provider adapters.

## Phase 5: Controlled Delegation

Success condition: delegation improves measurable task outcomes without uncontrolled cost, complexity, or merge conflicts.

Primary capabilities:

- Agent profiles.
- Subagents.
- Worktree isolation.
- Concurrency controls.
- Structured delegation results.
- Optional A2A support.

## Counterpoints

- Some phase 3 durability features may be easier to design early as interfaces, but the source discourages adding heavyweight frameworks before requirements justify them.
- Some interoperability work may be useful earlier if editor integration is a primary product goal, but ACP should still remain a client boundary rather than the runtime state model.

## Changes Over Time

- Initial roadmap copied from the design context and normalized into a reusable wiki page.

## Confidence

High for sequence direction; medium for exact phase boundaries because implementation constraints are unresolved.

## Open Questions

- Which phase 1 features define the first usable milestone?
- Which tasks form the acceptance suite for each phase?
- Which features should be designed as interfaces in phase 1 even if implemented later?
