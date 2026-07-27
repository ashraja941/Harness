---
type: overview
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [ai-coding-harness, architecture]
---

# Overview

The target system is now a Tau-inspired Python coding agent: a small, readable terminal-first harness that lets a language model inspect, modify, test, and explain software projects through typed tools and provider-neutral events. The original design context remains useful for long-term platform concerns, but Tau is now the primary near-term implementation reference. See [AI Coding Harness Design Context](sources/2026-07-04-ai-coding-harness-design-context.md) and [Tau Coding Agent](sources/2026-07-26-tau-coding-agent.md).

## Current Direction

- Follow [[tau-alignment]]: provider streaming, portable agent core, and coding-app concerns should remain separated.
- Build the Tau-style core first: provider-neutral events, messages, tools, agent loop, harness, and session primitives.
- Keep the reusable core independent of CLI, Rich, Textual, local config paths, slash commands, and rendering.
- Treat events as the contract consumed by print mode, TUI, custom frontends, and future extensions.
- Keep broader policy, sandboxing, MCP, ACP/A2A, and subagent work as later-stage concerns unless a concrete milestone requires them.

## Architectural Shape

The current architectural shape follows Tau's three-layer dependency direction: provider/model streaming, portable agent brain, and coding application wrapper. These responsibilities are expanded in [Recommended Architecture](synthesis/recommended-architecture.md), [Tau Alignment](synthesis/tau-alignment.md), and [Current Implementation Status](synthesis/current-implementation-status.md).

## Initial Priorities

The first implementation phase should finish the minimal provider-neutral agent loop and test it with fake providers and fake tools. The next usable milestone should add a simple CLI or print mode, built-in coding tools, and append-only local sessions. See [Implementation Roadmap](synthesis/implementation-roadmap.md).

## Important Constraints

- Do not treat prompts, instruction files, hooks, or system messages as security boundaries.
- Do not let MCP, ACP, A2A, LSP, OCI, or any other protocol become the internal domain model.
- Do not add subagent swarms, automatic long-term memory, vector databases, complex graph runtimes, custom editor protocols, or proprietary skill/instruction formats as initial requirements.
- Do not declare task success without evidence from checks, diffs, or completion criteria.
