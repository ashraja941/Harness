---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [architecture, synthesis]
---

# Recommended Architecture

## Current Thesis

The best current architecture is a Tau-inspired, provider-neutral coding agent with three small layers: provider/model streaming, a portable agent core, and a coding-application wrapper. The harness should first build the reusable event-driven agent brain and only later add larger platform features such as advanced policy, sandboxing, MCP, ACP/A2A, and subagents.

## Supporting Evidence

- The source explicitly states that the strongest design is a modular runtime with standards at boundaries and custom control over central behavior. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).
- Tau provides the current implementation reference: `tau_ai` translates providers into provider-neutral streams, `tau_agent` owns messages, tools, events, loop, harness, and session primitives, and `tau_coding` owns CLI/TUI, coding tools, config, instructions, skills, and on-disk sessions. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).
- The current Harness source tree already follows part of this shape with `harness.ai` provider/event primitives and `harness.agent` message/tool/event primitives. See [Current Implementation Status](current-implementation-status.md).
- The source lists custom-control areas including execution loop, context selection, context compaction, risk classification, approval policy, editing behavior, session state, quality gates, memory policy, subagent scheduling, cost controls, failure recovery, plugin trust, and human interaction model.
- The source recommends standards for repository instructions, skills, external tools/resources, editor integration, remote-agent federation, language intelligence, sandbox portability, observability, static-analysis findings, and structured schemas.
- The source states that no prompt, instruction file, hook, or system message should be treated as a security boundary.
- The source identifies context selection, edit reliability, side-effect control, failure recovery, verification, and truthful reporting as the main strategic differentiators.

## Tau-Aligned Component Model

- Provider layer: provider-specific adapters translate OpenAI, Anthropic, Hugging Face, OpenRouter, or compatible endpoints into provider-neutral stream events.
- Agent core: messages, tools, events, the agent loop, harness configuration, and portable session primitives live below UI and coding-app concerns.
- Coding application: CLI, print mode, optional TUI, built-in `read`/`write`/`edit`/`bash` tools, project instructions, skills, provider config, and on-disk sessions wrap the portable core.
- Frontends and renderers: consume events rather than raw provider chunks or internal state.

## Longer-Term Platform Components

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

## Implementation Stack

The current implementation stack is captured in [Recommended Tech Stack](recommended-tech-stack.md). It should now distinguish dependencies already present in `pyproject.toml` from Tau-inspired target dependencies and later platform infrastructure.

## Counterpoints

- A workflow framework could provide durable state, checkpointing, graph execution, distributed tasks, and orchestration features, but the source recommends a custom loop until concrete requirements justify the added abstraction.
- Multi-agent orchestration can improve parallel investigation and specialized review, but the source recommends single-agent reliability first.
- Full context can be simpler in small repositories, but layered search, pinned state, and structured compaction are the recommended scalable path.
- Tau's architecture is intentionally smaller than the original Harness platform vision; the wiki should preserve long-term concerns without letting them obscure the first usable coding agent.

## Changes Over Time

- Initial synthesis created from a single design-context source. Future sources should refine implementation language, runtime deployment shape, event schemas, sandbox defaults, plugin model, and evaluation suite.
- 2026-07-04: Added a provisional implementation stack in [Recommended Tech Stack](recommended-tech-stack.md), resolving the primary language and initial technology choices while leaving runtime deployment shape and stable event schemas open.
- 2026-07-26: Reoriented the recommended architecture around Tau's three-layer coding-agent design and added current implementation status.

## Confidence

High for the architectural direction because the source is internally consistent and explicit. Medium for implementation sequence details because no implementation constraints have been selected yet.

## Open Questions

- Which runtime deployment shape best fits the project: local process, daemon, service, or multiple modes?
- Which event schemas become stable public API?
- Which sandbox backend should ship first?
- How much of the plugin system should be available before interoperability phase work?
