---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-04
sources: []
tags: [architecture, tech-stack, implementation]
---

# Recommended Tech Stack

## Current Thesis

The first implementation should use a Python 3.12+ async runtime with native tools, SQLite persistence, official model-provider SDKs behind a custom provider interface, and standards-based integrations at system boundaries. This stack supports the current architecture goal: a reliable single-agent coding harness before adding heavier orchestration, subagents, remote agent integration, or performance-specific rewrites.

## Stack Choices

| Area | Choice |
| --- | --- |
| Primary language | Python 3.12+ |
| Package management | `uv` |
| Async runtime | `asyncio` with `TaskGroup`, queues, timeouts, and async subprocesses |
| HTTP and streaming | `httpx` |
| Schemas and validation | `pydantic`, `pydantic-settings` |
| CLI | `typer` |
| Terminal output | `rich` |
| Full TUI | `textual` |
| Persistence | SQLite with `aiosqlite` |
| Model providers | Official OpenAI and Anthropic Python SDKs behind a custom provider interface |
| External tools | Official Python MCP SDK |
| Code search | `ripgrep` |
| Code parsing | `tree-sitter` |
| Git operations | Native Git subprocesses; optionally `GitPython` for simple metadata |
| File watching | `watchfiles` |
| Path matching | `pathspec` |
| Retries | `tenacity` |
| Serialization | `orjson` |
| Testing | `pytest`, `pytest-asyncio`, `hypothesis`, `respx` |
| Observability | OpenTelemetry |
| Sandboxing | Docker or Podman behind an OCI-compatible sandbox interface |
| Static analysis output | SARIF |
| Editor integration later | ACP |
| Remote agent integration later | A2A |
| Optional workflow framework | LangGraph only if durable graph workflows become necessary |

## Core Architectural Choices

- Use a custom async agent loop.
- Keep the runtime independent from the TUI.
- Use `AGENTS.md` for repository instructions.
- Use Agent Skills for reusable workflows.
- Keep filesystem, Git, editing, shell, and testing tools native.
- Use MCP mainly for external services.
- Start with SQLite, not PostgreSQL or a vector database.
- Start with a reliable single agent before adding subagents.
- Use Zig later only for measured performance bottlenecks.

## Rationale

- Python 3.12+ fits the target ecosystem for model-provider SDKs, MCP integration, async orchestration, CLI/TUI tooling, testing, and rapid iteration.
- A custom `asyncio` loop preserves control over tool execution, policy checks, context selection, retries, cancellation, streaming, and quality gates.
- Native filesystem, Git, editing, shell, and testing tools keep reliability-critical behavior inside the harness rather than outsourcing it to external protocols.
- SQLite keeps persistence simple, inspectable, local-first, and sufficient for early event storage, replay, session state, and audit records.
- Docker or Podman behind an OCI-compatible interface keeps sandbox implementation replaceable.
- ACP, A2A, LangGraph, and Zig are deferred until concrete integration, durability, delegation, or performance requirements justify them.

## Relationship To Architecture

This page resolves the provisional implementation stack for [Recommended Architecture](recommended-architecture.md). It preserves the architecture principle that standards should be used at external boundaries while the core runtime remains custom and controlled.

## Changes Over Time

- Initial stack captured from user-provided project guidance on 2026-07-04.

## Confidence

High for initial implementation because the stack is coherent with the current architecture and roadmap. Medium for later phases because editor integration, remote agent integration, durable workflows, and performance-sensitive components may require revisions after measurement.

## Open Questions

- Should the first runtime ship only as a local CLI/TUI process, or should a daemon/service shape be designed from the beginning?
- Which exact event schemas should become stable public API?
- Which sandbox backend should be the default per operating system?
