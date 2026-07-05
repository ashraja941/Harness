---
type: index
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [ai-coding-harness, architecture]
---

# Harness Wiki

This wiki captures the design knowledge for a next-generation AI coding harness: a controlled execution platform that lets language models inspect, modify, test, and explain software projects through explicit tools, policies, context management, and human oversight.

## Start Here

- [Overview](overview.md) - High-level summary of the desired harness architecture.
- [Recommended Architecture](synthesis/recommended-architecture.md) - Current thesis for the modular runtime design.
- [Implementation Roadmap](synthesis/implementation-roadmap.md) - Suggested capability phases from single-agent runtime to controlled delegation.
- [Open Design Questions](synthesis/open-design-questions.md) - Questions to resolve before or during implementation.

## Source Summaries

- [AI Coding Harness Design Context](sources/2026-07-04-ai-coding-harness-design-context.md) - Primary source defining the objective, principles, components, tradeoffs, roadmap, and open questions.

## Core Concepts

- [Modular Runtime](concepts/modular-runtime.md) - The harness as a provider-neutral runtime independent of clients and model vendors.
- [Standards At Boundaries](concepts/standards-at-boundaries.md) - Using open standards as adapters without letting them control internal architecture.
- [Agent Execution Loop](concepts/agent-execution-loop.md) - Controlled iterative model/tool/quality-gate loop.
- [Context Management](concepts/context-management.md) - Pinned, working, and evictable context with provenance and structured compaction.
- [Tool System](concepts/tool-system.md) - Native and MCP tools, metadata, selection, risk, and structured errors.
- [Policy And Approval Engine](concepts/policy-and-approval-engine.md) - Allow/ask/deny authorization enforced below the model.
- [Sandboxing](concepts/sandboxing.md) - Replaceable execution isolation for filesystem, process, network, and resources.
- [Code Editing Reliability](concepts/code-editing-reliability.md) - Targeted edits, preconditions, post-edit checks, and rollback.
- [Quality Gates](concepts/quality-gates.md) - Evidence-based completion checks against acceptance criteria.
- [Persistence Replay Observability](concepts/persistence-replay-observability.md) - Event storage, replay records, telemetry, and auditability.
- [Skills And Repository Instructions](concepts/skills-and-repository-instructions.md) - Separation of `AGENTS.md`, reusable skills, tools, hooks, plugins, and memory.
- [Subagents And A2A](concepts/subagents-and-a2a.md) - Controlled local delegation and reserved use of A2A for remote independent agents.

## Entities

No separate entity pages have been created yet. Standards and external systems are currently covered inside concept pages.

## Questions

No saved question-answer pages yet.

## Maintenance

- [Log](log.md) - Append-only record of wiki setup and changes.
