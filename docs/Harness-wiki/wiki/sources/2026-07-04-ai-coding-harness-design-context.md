---
type: source-summary
status: active
created: 2026-07-04
updated: 2026-07-04
source_path: raw/ai-coding-harness-design-context.md
source_type: note
authors: []
published: null
tags: [ai-coding-harness, architecture, runtime]
---

# AI Coding Harness Design Context

## Citation

- Source: `raw/ai-coding-harness-design-context.md`
- Author(s): Unknown
- Published: Unknown

## One-Line Summary

This source defines the design direction for a next-generation AI coding harness as a modular, provider-neutral, policy-controlled, observable, and extensible execution runtime.

## Key Takeaways

- The harness should be an execution platform, not just a chat interface connected to a shell.
- Open standards should be used at interoperability boundaries, while central behavior such as the execution loop, context selection, compaction, risk classification, approvals, editing, quality gates, memory, subagent scheduling, cost controls, and recovery should remain custom-controlled.
- Safety must be enforced below the model through authorization, filesystem/process/network restrictions, sandboxing, credential isolation, and policy.
- A reliable single-agent runtime should come before multi-agent orchestration.
- Context management, edit mechanics, failure recovery, verification, replay, and truthful reporting are the key differentiators.
- Initial capability phases should progress from dependable single-agent work, to project-aware behavior, durability/isolation, interoperability, and then controlled delegation.

## Important Claims

- Claim: The strongest architecture is a modular runtime with standards at system boundaries and custom control over central behavior.
  Evidence: The source explicitly recommends standards for `AGENTS.md`, Agent Skills, MCP, ACP, A2A, LSP, OCI, OpenTelemetry, SARIF, and JSON Schema while listing core runtime areas that should remain custom.
  Confidence: high
- Claim: Security decisions must not be delegated to prompts or instruction files.
  Evidence: The source states that no prompt, instruction file, hook, or system message should be treated as a security boundary and lists enforcement mechanisms below the model.
  Confidence: high
- Claim: Single-agent reliability is the prerequisite for multi-agent design.
  Evidence: The source recommends a dependable single-agent runtime first and says subagents should not compensate for weak context selection, search, editing, testing, planning, or verification.
  Confidence: high
- Claim: Context management should use pinned, working, and evictable categories with provenance and structured compaction.
  Evidence: The source defines those context categories and lists required fields for compacted state and provenance.
  Confidence: high
- Claim: The initial design should avoid unnecessary platform complexity such as marketplaces, vector databases, proprietary formats, custom editor protocols, complex graph runtimes, and unlimited subagent swarms.
  Evidence: The source lists these as non-goals for the initial design.
  Confidence: high

## Entities Mentioned

- OpenAI Codex
- Claude Code
- OpenCode
- Deep Agents
- Pi
- Aider
- Cline
- Roo Code
- Gemini CLI
- MCP
- ACP
- A2A
- LSP
- OCI
- OpenTelemetry
- SARIF
- JSON Schema

## Concepts Mentioned

- [[modular-runtime]]
- [[standards-at-boundaries]]
- [[agent-execution-loop]]
- [[context-management]]
- [[tool-system]]
- [[policy-and-approval-engine]]
- [[sandboxing]]
- [[quality-gates]]
- [[code-editing-reliability]]
- [[persistence-replay-observability]]
- [[skills-and-repository-instructions]]
- [[subagents-and-a2a]]

## Contradictions Or Tensions

- The source favors standards and interoperability, but warns against letting standards become the internal architecture.
- The source values autonomy and speed, but recommends explicit human approval for risky or side-effecting actions.
- The source leaves several implementation choices open, including implementation language, runtime deployment shape, event schemas, sandbox defaults, and plugin isolation.

## Open Questions

- Which implementation language best fits portability, performance, and ecosystem needs?
- Which runtime events should be stable public API?
- What token-budget and relevance-scoring policies should govern context selection?
- What default sandbox should be used on Windows, macOS, and Linux?
- Which permission modes and session-scoped approvals should exist?
- Should plugins run in-process or out-of-process?

## Pages To Update

- `wiki/overview.md`
- `wiki/synthesis/recommended-architecture.md`
- `wiki/synthesis/implementation-roadmap.md`
- `wiki/synthesis/open-design-questions.md`
- `wiki/concepts/*.md`
