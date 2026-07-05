---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [architecture, synthesis]
---

# Recommended Architecture

## Current Thesis

The best current architecture is a modular, provider-neutral coding runtime with open standards at external boundaries and custom control over reliability-critical behavior. The harness should start as a dependable single-agent runtime and add durability, interoperability, and controlled delegation only after the core loop, tools, policy, context management, editing, and quality gates are reliable.

## Supporting Evidence

- The source explicitly states that the strongest design is a modular runtime with standards at boundaries and custom control over central behavior. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).
- The source lists custom-control areas including execution loop, context selection, context compaction, risk classification, approval policy, editing behavior, session state, quality gates, memory policy, subagent scheduling, cost controls, failure recovery, plugin trust, and human interaction model.
- The source recommends standards for repository instructions, skills, external tools/resources, editor integration, remote-agent federation, language intelligence, sandbox portability, observability, static-analysis findings, and structured schemas.
- The source states that no prompt, instruction file, hook, or system message should be treated as a security boundary.
- The source identifies context selection, edit reliability, side-effect control, failure recovery, verification, and truthful reporting as the main strategic differentiators.

## Component Model

- Client layer: CLI, TUI, editor, web, API, or remote runner surfaces that communicate with the runtime.
- Session supervisor: starts/resumes sessions, tracks limits, handles cancellation, checkpointing, configuration, and lifecycle events.
- Agent runtime: constructs model requests, receives model output, resolves tool calls, iterates, retries, invokes quality gates, and produces final results.
- Context manager: loads instructions, selects context, manages budgets, activates skills, compacts state, and tracks provenance.
- Tool registry and router: registers native and MCP tools, validates arguments, attaches risk metadata, executes tools, normalizes results, and controls concurrency.
- Policy and approval engine: decides allow, ask, or deny based on tool, path, command, network, credentials, trust, user mode, agent profile, skill, side effects, and session state.
- Sandbox layer: isolates filesystem, processes, network, resources, environment, snapshots, and execution backend.
- Quality gate: evaluates acceptance criteria, checks, unrelated changes, generated files, documentation, claims, evidence, and sensitive-file risks.
- Persistence and event store: records sessions, events, messages, tool calls, approvals, artifacts, checkpoints, memory, and replay data.
- Extension system: supports tools, hooks, providers, skills, policy modules, sandboxes, clients, and observability exporters without granting unrestricted trust.

## Counterpoints

- A workflow framework could provide durable state, checkpointing, graph execution, distributed tasks, and orchestration features, but the source recommends a custom loop until concrete requirements justify the added abstraction.
- Multi-agent orchestration can improve parallel investigation and specialized review, but the source recommends single-agent reliability first.
- Full context can be simpler in small repositories, but layered search, pinned state, and structured compaction are the recommended scalable path.

## Changes Over Time

- Initial synthesis created from a single design-context source. Future sources should refine implementation language, runtime deployment shape, event schemas, sandbox defaults, plugin model, and evaluation suite.

## Confidence

High for the architectural direction because the source is internally consistent and explicit. Medium for implementation sequence details because no implementation constraints have been selected yet.

## Open Questions

- Which implementation language and runtime deployment shape best fit the project?
- Which event schemas become stable public API?
- Which sandbox backend should ship first?
- How much of the plugin system should be available before interoperability phase work?
