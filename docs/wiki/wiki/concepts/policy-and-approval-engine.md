---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [security, policy, approvals]
---

# Policy And Approval Engine

## Definition

The policy and approval engine evaluates proposed actions and determines whether they are allowed, require approval, or are denied.

## Why It Matters

The source recommends simple allow/ask/deny semantics while making authorization depend on tool, path, command, working directory, network destination, credential scope, repository trust, user mode, agent profile, skill, external side effects, previous approval, and session state. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Safety must be enforced below the model.
- Reading and searching within a trusted repository can usually be allowed.
- Running tests can usually be allowed.
- Workspace writes may be ask or allow under an explicit edit mode.
- Deleting files, installing dependencies, network access, pushing commits, and creating external issues or pull requests should usually ask.
- Reading credential files and destructive cloud or production operations should be denied by default unless explicitly enabled.
- Approval caching should use normalized capabilities rather than exact command text, with scope and expiry.
- Enterprise deployments may delegate authorization decisions to an external policy engine while the harness remains responsible for enforcement, audit, explanation, approval flow, and tool execution.

## Related Concepts

- [[tool-system]]
- [[sandboxing]]
- [[agent-execution-loop]]

## Examples

- A user might approve running a specific test command in a repository for the current session, or writing files only under a specific directory.

## Contradictions Or Nuance

- Automatic action improves speed, but risk-based approval preserves safety, control, and trust.

## Open Questions

- What are the default permission modes?
- Which actions may be approved for the whole session?
- How should organizational policy override user preference?
