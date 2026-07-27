---
type: synthesis
status: active
created: 2026-07-26
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [tau, architecture, implementation]
---

# Tau Alignment

## Current Thesis

Tau is now the primary implementation reference for Harness. Harness should follow Tau's small layered architecture and event-first design while keeping its own package names until a deliberate rename or package split is chosen.

The near-term target is not the full broad platform described in the original design context. It is a readable terminal coding agent with a portable core, provider-neutral streaming, typed tools, a minimal agent loop, a CLI or print mode, coding tools, and durable local sessions. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Supporting Evidence

- Tau separates `tau_ai`, `tau_agent`, and `tau_coding`, giving each layer one job and keeping dependencies flowing toward the provider layer. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).
- Tau treats typed events as the contract between providers, the harness, renderers, the TUI, print mode, and custom frontends.
- The current Harness code already started in the Tau-compatible direction: provider events, agent events, messages, tool abstractions, and a provider streaming protocol exist under `src/harness`.
- Tau's documentation says public docs should follow implementation while phase notes preserve the build journal. That fits this wiki's role as durable project memory.

## Implications For Harness

- Preserve the core/application boundary: agent messages, tools, events, loop, and harness logic should remain independent of CLI, Rich, Textual, local config, and rendering.
- Prefer a minimal `AgentHarness` loop before adding policy engines, sandbox backends, MCP integrations, subagents, or database persistence.
- Treat events as a stable design surface early, even if the exact schema remains provisional.
- Implement tools as typed async callables with explicit schemas and structured results.
- Prefer append-only JSONL session history before adding SQLite or heavier replay infrastructure.

## Counterpoints

- The original design context still captures useful long-term concerns: policy, sandboxing, quality gates, observability, and controlled delegation. These should remain in the wiki as later-stage constraints rather than the first build target.
- Tau is an external project, not a requirements document. Harness can diverge when local goals require it, but deviations should be explicit.

## Changes Over Time

- 2026-07-26: Added Tau as the primary implementation reference after the project direction changed toward following the Hugging Face Tau coding agent.

## Confidence

High that Tau should reshape the near-term roadmap; medium on exact package naming because the user has not yet decided whether to keep a single `harness` package or split into Tau-like package layers.

## Open Questions

- Should Harness adopt Tau-like package names such as `harness_ai`, `harness_agent`, and `harness_coding`?
- Should the root command remain `harness`, become Tau-like, or use a new product name?
- Which Tau behaviors should be implemented first: harness loop, print mode, coding tools, or sessions?
