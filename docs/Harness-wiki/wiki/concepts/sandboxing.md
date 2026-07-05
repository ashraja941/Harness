---
type: concept
status: active
created: 2026-07-04
updated: 2026-07-04
sources:
  - wiki/sources/2026-07-04-ai-coding-harness-design-context.md
tags: [sandbox, security]
---

# Sandboxing

## Definition

Sandboxing is the execution boundary that protects the host from model-generated actions and protects tasks from inconsistent or unsafe environments.

## Why It Matters

The source says the sandbox layer should handle filesystem isolation, process execution, network isolation, resource limits, environment management, snapshot/reset behavior, and local or remote execution abstraction. See [AI Coding Harness Design Context](../sources/2026-07-04-ai-coding-harness-design-context.md).

## Current Understanding

- Desired properties include non-root execution, ephemeral environments, restricted mounts, workspace-specific write access, network disabled by default, CPU/memory/process/disk/time limits, environment sanitization, no host container socket, no privileged mode, reproducible environments, and cleanup.
- The runtime should support more than one backend: local restricted execution, local container, remote container, VM, managed remote development environment, or organization-specific sandbox.
- Agent process and code-execution environment should be separable to support remote execution, stronger isolation, multiple language environments, reproducibility, horizontal scaling, worktree isolation, and enterprise deployment.
- The runtime should depend on sandbox capabilities rather than a specific vendor or container engine.

## Related Concepts

- [[policy-and-approval-engine]]
- [[tool-system]]
- [[persistence-replay-observability]]

## Examples

- A phase 3 implementation may add container or remote sandbox support after the single-agent runtime and project-aware behavior are reliable.

## Contradictions Or Nuance

- Local execution offers low latency and easy development, while remote sandboxing offers stronger isolation, reproducibility, scalability, and enterprise control.

## Open Questions

- What should the default local sandbox be?
- How should Windows, macOS, and Linux differ?
- Is remote execution required for the first release?
