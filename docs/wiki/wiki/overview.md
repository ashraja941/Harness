---
type: overview
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [ai-coding-harness, architecture]
---

# Overview

The target system is an AI coding harness: a controlled execution platform that lets one or more language models inspect, reason about, modify, test, and explain software projects through explicit tools and policies. It should not be reduced to a chat UI connected to a shell; the source frames the runtime as responsible for orchestration, tool invocation, repository understanding, context selection, permissions, persistence, recovery, verification, oversight, interoperability, observability, and evaluation. See [AI Coding Harness Design Context](sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Direction

- Build a [[modular-runtime]] with standards at external boundaries and custom control over core behavior.
- Keep the central runtime independent of any one terminal, editor, web UI, or model vendor.
- Enforce safety below the model through tools, filesystem restrictions, process controls, network controls, sandboxing, credentials isolation, and policy.
- Prefer a dependable single-agent runtime before adding bounded [[subagents-and-a2a]].
- Make every significant action observable and replayable without depending on hidden chain-of-thought.

## Architectural Shape

The source separates the system into clients, session supervisor, agent runtime, context manager, tool registry/router, policy and approval engine, sandbox layer, quality gate, persistence/event store, and extension system. These responsibilities are expanded in [Recommended Architecture](synthesis/recommended-architecture.md).

## Initial Priorities

The first implementation phase should focus on a provider-neutral model interface, controlled agent loop, event streaming, repository reading/search, safe editing, shell and test execution, git diff, permission engine, basic client, session limits, and clear final reporting. See [Implementation Roadmap](synthesis/implementation-roadmap.md).

## Important Constraints

- Do not treat prompts, instruction files, hooks, or system messages as security boundaries.
- Do not let MCP, ACP, A2A, LSP, OCI, or any other protocol become the internal domain model.
- Do not add subagent swarms, automatic long-term memory, vector databases, complex graph runtimes, custom editor protocols, or proprietary skill/instruction formats as initial requirements.
- Do not declare task success without evidence from checks, diffs, or completion criteria.
