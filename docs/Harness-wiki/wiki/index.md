---
type: index
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [ai-coding-harness, architecture, tau]
---

# Harness Wiki

This wiki captures the design knowledge for Harness, now a Tau-inspired Python coding-agent harness. The near-term direction is a small, readable, terminal-first coding agent with provider-neutral streams, a portable agent core, typed tools, event-driven frontends, and durable local sessions.

## Start Here

- [Overview](overview.md) - High-level summary of the Tau-aligned Harness direction.
- [Tau Alignment](synthesis/tau-alignment.md) - Decision synthesis naming Tau as the primary implementation reference.
- [Current Implementation Status](synthesis/current-implementation-status.md) - What exists in the Python codebase today and what is missing.
- [Recommended Architecture](synthesis/recommended-architecture.md) - Current thesis for the Tau-inspired layered design.
- [Recommended Tech Stack](synthesis/recommended-tech-stack.md) - Current implementation stack and core architectural choices.
- [Implementation Roadmap](synthesis/implementation-roadmap.md) - Tau-aligned phases from typed primitives to a usable coding app.
- [Open Design Questions](synthesis/open-design-questions.md) - Questions to resolve before or during implementation.

## Source Summaries

- [AI Coding Harness Design Context](sources/2026-07-04-ai-coding-harness-design-context.md) - Primary source defining the objective, principles, components, tradeoffs, roadmap, and open questions.
- [Tau Coding Agent](sources/2026-07-26-tau-coding-agent.md) - External implementation reference for a small layered Python terminal coding agent.

## Core Concepts

- [Modular Runtime](concepts/modular-runtime.md) - The harness as a provider-neutral runtime independent of clients and model vendors.
- [Standards At Boundaries](concepts/standards-at-boundaries.md) - Using open standards as adapters without letting them control internal architecture.
- [Agent Execution Loop](concepts/agent-execution-loop.md) - Tau-style iterative model/tool/event loop.
- [Context Management](concepts/context-management.md) - Pinned, working, and evictable context with provenance and structured compaction.
- [Tool System](concepts/tool-system.md) - Typed async tools with schemas and structured results, with larger registry/policy work deferred.
- [Policy And Approval Engine](concepts/policy-and-approval-engine.md) - Allow/ask/deny authorization enforced below the model.
- [Sandboxing](concepts/sandboxing.md) - Replaceable execution isolation for filesystem, process, network, and resources.
- [Code Editing Reliability](concepts/code-editing-reliability.md) - Targeted edits, preconditions, post-edit checks, and rollback.
- [Quality Gates](concepts/quality-gates.md) - Evidence-based completion checks against acceptance criteria.
- [Persistence Replay Observability](concepts/persistence-replay-observability.md) - Event streams and append-only session history before heavier observability.
- [Skills And Repository Instructions](concepts/skills-and-repository-instructions.md) - Separation of `AGENTS.md`, reusable skills, tools, hooks, plugins, and memory.
- [Subagents And A2A](concepts/subagents-and-a2a.md) - Controlled local delegation and reserved use of A2A for remote independent agents.

## Entities

No separate entity pages have been created yet. Standards and external systems are currently covered inside concept pages.

## Questions

No saved question-answer pages yet.

## Maintenance

- [Log](log.md) - Append-only record of wiki setup and changes.
