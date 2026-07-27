---
type: source-summary
status: active
created: 2026-07-26
updated: 2026-07-26
source_path: https://github.com/huggingface/tau
source_type: repository|documentation
authors: [Hugging Face]
published: null
tags: [tau, coding-agent, architecture, events]
---

# Tau Coding Agent

## Citation

- Source: `https://github.com/huggingface/tau`
- Supporting docs: `https://twotimespi.dev/internals/architecture/`, `https://twotimespi.dev/internals/agent-loop/`, `https://twotimespi.dev/concepts/`
- Author(s): Hugging Face contributors
- Published: Active project; exact publication date not captured

## One-Line Summary

Tau provides a small, readable Python coding-agent architecture that separates provider streaming, portable agent core behavior, and coding-app concerns behind typed event streams.

## Key Takeaways

- Tau is organized as `tau_coding -> tau_agent -> tau_ai`, where provider integration is below the portable agent core and the coding application wraps that core.
- Tau treats events as the contract between providers, the reusable harness, renderers, the TUI, print mode, and custom frontends.
- Tau's portable core is deliberately kept free of CLI, Textual, Rich, local config paths, slash commands, and app-specific rendering.
- Tau defines tools as ordinary typed functions: a schema plus an async executor returning a structured result.
- Tau uses durable, inspectable sessions, with append-only JSONL history and compaction that does not rewrite the record.

## Important Claims

- Claim: The core coding-agent brain should not depend on terminal UI, local file-layout, or rendering concerns.
  Evidence: Tau's architecture documentation states that `tau_agent` must not import CLI, Rich, Textual, or resource-loading code, and that frontends consume events.
  Confidence: high
- Claim: A minimal coding-agent loop repeatedly streams a model response, emits events, executes requested tools, appends tool results, and continues until no tool calls remain.
  Evidence: Tau's agent-loop documentation lists that turn cycle explicitly.
  Confidence: high
- Claim: Events are the stable contract for frontend rendering and extension points.
  Evidence: Tau's README and internals documentation both say providers, renderers, the TUI, and custom frontends meet at a typed event stream.
  Confidence: high
- Claim: Tau's public implementation favors a readable teaching codebase over a large production framework.
  Evidence: Tau's README describes it as a small, readable terminal coding agent and a teaching project.
  Confidence: high

## Entities Mentioned

- Tau
- Hugging Face
- Pi
- OpenAI
- Anthropic
- OpenRouter
- Textual
- Rich

## Concepts Mentioned

- [[agent-execution-loop]]
- [[tool-system]]
- [[persistence-replay-observability]]
- [[context-management]]
- [[skills-and-repository-instructions]]
- [[modular-runtime]]

## Contradictions Or Tensions

- Earlier Harness wiki pages describe a broad platform with policy, sandboxing, MCP, ACP, A2A, quality gates, and subagents as prominent architectural concerns. Tau supports extensibility but demonstrates a smaller first target centered on provider streams, a portable agent harness, a coding session wrapper, typed tools, events, CLI/TUI, and durable local sessions.
- Earlier stack guidance mentions SQLite, OpenTelemetry, Docker/Podman, MCP SDKs, and other later infrastructure. Tau's public package uses a leaner dependency set and append-only JSONL sessions.

## Open Questions

- Should Harness keep a single `harness` Python package for now, or split into Tau-like layers such as `harness_ai`, `harness_agent`, and `harness_coding`?
- Which Tau features should be copied directly, and which should remain only conceptual inspiration?
- Should the project keep the Harness name while describing itself as Tau-inspired, or eventually rename product/package surfaces?

## Pages To Update

- `wiki/overview.md`
- `wiki/synthesis/recommended-architecture.md`
- `wiki/synthesis/implementation-roadmap.md`
- `wiki/synthesis/recommended-tech-stack.md`
- `wiki/concepts/agent-execution-loop.md`
- `wiki/concepts/tool-system.md`
- `wiki/concepts/persistence-replay-observability.md`
