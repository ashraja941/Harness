---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-26
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
  - wiki/sources/2026-07-26-tau-coding-agent.md
tags: [tools, mcp]
---

# Tool System

## Definition

The near-term tool system should follow Tau's smaller model: a tool is an ordinary typed async function with a JSON-like input schema and a structured result. Larger registry, routing, risk, MCP, policy, and concurrency concerns remain later-stage extensions.

## Why It Matters

The original design context says coding-critical operations should normally remain native because they need precise control, while MCP should be used for external or organizational integrations. Tau narrows the first implementation target to typed tools such as `read`, `write`, `edit`, and `bash`. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md) and [Tau Coding Agent](../sources/2026-07-26-tau-coding-agent.md).

## Current Understanding

- Current code defines `ToolCall`, `AgentToolResult`, `AgentTool`, `ToolExecutor`, and `ToolCancellationToken`.
- The first built-in coding tools should be Tau-like: `read`, `write`, `edit`, and `bash`.
- A tool should expose a name, description, input schema, async executor, and structured result.
- The result should preserve both human-readable content and machine-readable data/details where useful.
- MCP, risk metadata, approval integration, and advanced concurrency rules should be deferred until native tools and the loop work.

## Related Concepts

- [[policy-and-approval-engine]]
- [[sandboxing]]
- [[standards-at-boundaries]]
- [[tau-alignment]]

## Examples

- A `read` tool can take a path and return file contents; an `edit` tool can apply a targeted change; a `bash` tool can execute a command and return stdout, stderr, and exit code.

## Contradictions Or Nuance

- MCP improves interoperability, but adding it before the native Tau-style tools would distract from the first usable coding agent.

## Open Questions

- Should the first `edit` tool support patch application, string replacement, or both?
- What approval behavior should `bash` have before a full policy engine exists?
