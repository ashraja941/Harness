---
type: synthesis
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [architecture, tech-stack, implementation]
---

# Recommended Tech Stack

## Current Thesis

The first implementation should stay close to Tau's lean Python stack: Python 3.12+, typed Pydantic models, async provider streaming, Typer/Rich for terminal surfaces, optional Textual for a TUI, and durable local sessions before heavier infrastructure. The stack page should distinguish what is installed today from what is planned. See [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Stack Choices

| Area | Current / Target Choice |
| --- | --- |
| Primary language | Python 3.12+ |
| Package management | `uv` |
| Async runtime | Current: standard async protocols; target: `asyncio` or `anyio` patterns as needed |
| HTTP and streaming | Current: `httpx`; Tau reference: `httpx[socks]` |
| Schemas and validation | `pydantic`, `pydantic-settings` |
| CLI | `typer` |
| Terminal output | `rich` |
| Full TUI | Planned: `textual` when interactive TUI work begins |
| Persistence | Target first: append-only JSONL sessions; defer SQLite until requirements justify it |
| Model providers | Current: `openai`; target: provider-neutral adapters, potentially Anthropic, Hugging Face, OpenRouter, and OpenAI-compatible endpoints |
| External tools | Defer MCP until the built-in coding tool layer works |
| Code search | Native tools can use `ripgrep` subprocesses when added |
| Git operations | Native Git subprocesses when coding tools need Git awareness |
| File watching | Defer until TUI/session requirements need it |
| Path matching | Add only when project-resource discovery needs it |
| Retries | Add only when provider/tool failure policy needs it |
| Serialization | Standard JSON is sufficient until performance or schema requirements justify alternatives |
| Testing | Current: `pytest`, `pytest-asyncio`; target: fake providers and fake tools for deterministic loop tests |
| Observability | Event stream first; defer OpenTelemetry |
| Sandboxing | Defer Docker/Podman until the basic coding agent works |
| Editor integration later | ACP remains later |
| Remote agent integration later | A2A remains later |
| Optional workflow framework | Avoid until durable graph workflows become necessary |

## Core Architectural Choices

- Use a custom async agent loop inspired by Tau.
- Keep the runtime independent from the TUI.
- Use `AGENTS.md` for repository instructions.
- Use Agent Skills for reusable workflows.
- Keep filesystem, Git, editing, shell, and testing tools native.
- Use MCP mainly for external services.
- Start with append-only JSONL sessions, not SQLite, PostgreSQL, or a vector database.
- Start with a reliable single agent before adding subagents.
- Add performance-specific dependencies only after measurement.

## Rationale

- Python 3.12+ fits both the current project and Tau's implementation baseline.
- A custom `asyncio` loop preserves control over tool execution, policy checks, context selection, retries, cancellation, streaming, and quality gates.
- Native filesystem, Git, editing, shell, and testing tools keep reliability-critical behavior inside the harness rather than outsourcing it to external protocols.
- Append-only JSONL sessions match Tau's emphasis on durable, inspectable history and are simpler than a database for the first implementation.
- SQLite, Docker/Podman, OpenTelemetry, MCP, ACP, A2A, LangGraph, and performance-specific dependencies are deferred until concrete requirements justify them.

## Relationship To Architecture

This page resolves the provisional implementation stack for [Recommended Architecture](recommended-architecture.md). It preserves the architecture principle that standards should be used at external boundaries while the core runtime remains custom and controlled.

## Changes Over Time

- Initial stack captured from user-provided project guidance on 2026-07-04.
- 2026-07-26: Reconciled the stack with Tau and the current `pyproject.toml`; moved SQLite, MCP, sandboxing, and observability to later phases.

## Confidence

High for initial implementation because the stack is coherent with the current architecture and roadmap. Medium for later phases because editor integration, remote agent integration, durable workflows, and performance-sensitive components may require revisions after measurement.

## Open Questions

- Should the first runtime ship only as a local CLI/TUI process, or should a daemon/service shape be designed from the beginning?
- Which exact event schemas should become stable public API?
- Which sandbox backend should be the default per operating system?
