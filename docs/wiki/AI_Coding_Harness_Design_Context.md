# AI Coding Harness — Design Context

## Purpose of this document

This document captures the current design direction for a next-generation AI coding harness. It is intended to be given to a coding agent, engineering team, or future design process as durable project context.

The purpose is not to prescribe a specific implementation, framework, programming language, repository layout, or class hierarchy. The purpose is to define:

- What the system is expected to do.
- Which architectural concerns must be handled explicitly.
- Which open standards should be followed.
- Which design patterns appear strongest across existing coding harnesses.
- Which tradeoffs should remain deliberate rather than accidental.
- Which implementation areas should remain proprietary and under direct control.
- Which optional packages or frameworks may be evaluated later.

Any implementation examples, package references, or organizational suggestions in this document are advisory only. They should not be treated as fixed technical requirements unless they are promoted into explicit project decisions later.

---

## 1. Project objective

The project is an AI coding harness: a system that allows one or more language models to inspect, reason about, modify, test, and explain software projects through a controlled set of tools and policies.

The harness should not be reduced to a chat interface connected to a shell. It should be treated as an execution platform with the following responsibilities:

- Model orchestration.
- Tool discovery and invocation.
- Repository understanding.
- Context selection and compression.
- Project-specific instruction handling.
- Reusable skill handling.
- Safe filesystem and process access.
- Permission and approval enforcement.
- Session persistence.
- Failure recovery.
- Testing and quality verification.
- Human oversight.
- Editor and external-tool interoperability.
- Observability and evaluation.

The long-term goal is to build a reliable engineering agent, not merely an impressive coding demo.

---

## 2. Core design position

The strongest design is a modular runtime with standards at its boundaries and custom control over its central behavior.

The harness should adopt standards where interoperability is valuable:

- `AGENTS.md` for repository-specific instructions.
- Agent Skills for reusable procedures.
- Model Context Protocol, or MCP, for external tools and resources.
- Agent Client Protocol, or ACP, for editor-to-agent communication.
- Agent-to-Agent, or A2A, only when interacting with independent remote agents.
- Language Server Protocol, or LSP, for language intelligence.
- Open Container Initiative, or OCI, concepts for portable sandbox execution.
- OpenTelemetry for traces, metrics, and logs.
- SARIF for normalized static-analysis and security findings.
- JSON Schema for tool and structured-output definitions.

The harness should retain custom control over the following areas:

- Agent execution loop.
- Context selection and budgeting.
- Context compaction.
- Risk classification.
- Approval policy.
- Code-editing behavior.
- Session state and event model.
- Quality gates.
- Memory policy.
- Subagent scheduling.
- Cost controls.
- Failure recovery.
- Plugin trust.
- Human interaction model.

These custom areas are where the harness can differentiate itself. Outsourcing them to a general orchestration framework too early would reduce control over reliability and behavior.

---

## 3. Influences from existing harnesses

The design should synthesize ideas from multiple systems rather than clone one project.

### 3.1 OpenAI Codex influence

Useful ideas to retain:

- Clear separation between the coding runtime, user interface, tools, and sandbox behavior.
- Strong repository-local operation.
- Explicit approval boundaries.
- Support for project instructions.
- A runtime that can be used through more than one client surface.
- A bias toward constrained tool use rather than unconstrained shell automation.
- Agent profiles or specialized execution roles where appropriate.

The lesson is that the agent runtime should be independent from the terminal or editor experience.

### 3.2 Claude Code influence

Useful ideas to retain:

- Hierarchical project instructions.
- Reusable skills.
- Lifecycle hooks.
- Specialized agent profiles.
- Human-readable configuration.
- Explicit permission modes.
- Progressive disclosure of capabilities.
- Strong integration between reasoning, repository context, and execution.

The major lesson is that customization should be possible without modifying the core runtime.

### 3.3 OpenCode influence

Useful ideas to retain:

- Simple allow, ask, and deny permission semantics.
- Extensible provider and plugin support.
- Terminal-first ergonomics.
- Clear exposure of tool activity.
- Configurable agent behavior.
- Practical integration with multiple model providers.
- Strong user control over approval behavior.

The major lesson is that safety policy must be visible and understandable to the user.

### 3.4 Deep Agents influence

Useful ideas to retain:

- Explicit goals and acceptance criteria.
- Rubric-based quality checks.
- Persistent execution state.
- Support for long-running tasks.
- Separation between the agent and the execution sandbox.
- Controlled subagent delegation.
- Structured task completion rather than arbitrary model stopping.
- Durable workflow concepts where they provide concrete value.

The major lesson is that an agent should stop because evidence shows the task is complete, not because the model decided to stop generating tool calls.

### 3.5 Pi influence

Useful ideas to retain:

- A minimal and composable core.
- Extension-first thinking.
- Avoiding unnecessary framework complexity.
- Treating the harness as a programmable substrate.
- Making it possible to replace individual behaviors without rewriting the system.

The major lesson is to keep the kernel small and make policies, tools, interfaces, and integrations replaceable.

### 3.6 Aider and related patch-oriented tools

Useful ideas to retain:

- Git-aware workflows.
- Diff-first user interaction.
- Repository maps and targeted context gathering.
- Tight feedback between edits and tests.
- Emphasis on reversible changes.
- Practical handling of model-generated patches.

The major lesson is that coding quality depends heavily on edit mechanics and feedback loops, not only model quality.

### 3.7 IDE-centered agents such as Cline and Roo Code

Useful ideas to retain:

- Explicit visibility into every action.
- Strong human approval workflows.
- Tight editor integration.
- Checkpoint and restore capabilities.
- Tool-by-tool interaction history.
- User-facing planning and task tracking.

The major lesson is that transparency and reversibility are central product features, not debugging conveniences.

### 3.8 Gemini CLI and other provider-backed harnesses

Useful ideas to retain:

- Standardized tool declarations.
- Broad model and multimodal support.
- Integration with external services.
- Project-level context files.
- Extensible command systems.
- Provider-specific capabilities hidden behind a stable user experience.

The major lesson is to normalize provider differences without forcing the lowest common denominator.

---

## 4. Architectural principles

### 4.1 The runtime is the product

The central runtime should function without depending on a particular terminal interface, editor, web application, or model vendor.

Any client should be able to:

- Start or resume a session.
- Submit a task.
- Receive streamed events.
- Approve or reject actions.
- Inspect diffs.
- Cancel work.
- Review results.

The runtime should expose events and structured state rather than assume direct terminal rendering.

### 4.2 Standards belong at system boundaries

External protocols should be treated as adapters.

For example:

- MCP is an external tool boundary, not the internal tool architecture.
- ACP is a client boundary, not the internal event model.
- A2A is a federation boundary, not the local subagent scheduler.
- LSP is a language-intelligence boundary, not the repository representation.
- OCI is a sandbox portability concept, not a requirement to hard-code Docker-specific behavior.

This prevents a protocol from controlling the internal architecture.

### 4.3 Safety is enforced below the model

No prompt, instruction file, hook, or system message should be treated as a security boundary.

Security decisions must be enforced by:

- Tool authorization.
- Filesystem restrictions.
- Process restrictions.
- Network controls.
- Credential isolation.
- Sandbox boundaries.
- External policy where necessary.

The model may explain a restriction, but it must not be responsible for enforcing it.

### 4.4 A single agent must be reliable before multi-agent orchestration

The initial goal should be a dependable single-agent runtime.

Subagents should not be added to compensate for weaknesses in:

- Context selection.
- Code search.
- Edit reliability.
- Testing.
- Planning.
- Quality verification.

Multi-agent features should be added only when they create measurable benefits.

### 4.5 Every significant action should be observable and replayable

The harness should produce enough structured information to answer:

- What did the model receive?
- Which instructions were active?
- Which tools were available?
- Which action was attempted?
- Why was it allowed, denied, or sent for approval?
- What changed?
- Which checks were run?
- Why did the agent consider the task complete?
- How much time and cost were consumed?

This should be possible without exposing private chain-of-thought.

### 4.6 Human control should be explicit

The user should always be able to:

- See what the agent plans to do.
- Inspect pending risky actions.
- Change permission modes.
- Cancel execution.
- Review diffs.
- Revert changes.
- Resume a prior session.
- Understand what was verified and what was not.

---

## 5. Conceptual component model

The system should be divided conceptually into the following responsibilities.

### 5.1 Client layer

Possible clients include:

- Command-line interface.
- Terminal user interface.
- Editor extension.
- Web interface.
- Automated API client.
- Remote task runner.

Clients should not directly execute tools or manage model context. They communicate with the runtime.

### 5.2 Session supervisor

The session supervisor is responsible for:

- Starting and resuming sessions.
- Tracking limits.
- Cancellation.
- Session-level configuration.
- Checkpointing.
- Coordination between the client and runtime.
- Managing session lifecycle events.

### 5.3 Agent runtime

The agent runtime is responsible for:

- Constructing model requests.
- Receiving model output.
- Resolving tool calls.
- Managing iteration.
- Handling retries.
- Feeding results back to the model.
- Invoking quality gates.
- Deciding whether another turn is required.
- Producing a final result.

### 5.4 Context manager

The context manager is responsible for:

- Loading applicable instructions.
- Selecting relevant files and artifacts.
- Managing token budgets.
- Activating skills.
- Preserving important state.
- Compacting old information.
- Avoiding redundant context.
- Tracking provenance for included information.

### 5.5 Tool registry and router

The tool system is responsible for:

- Registering native tools.
- Registering MCP tools.
- Presenting only relevant tools to the model.
- Validating arguments.
- Attaching risk metadata.
- Executing tools.
- Normalizing results and errors.
- Enforcing concurrency rules.

### 5.6 Policy and approval engine

The policy engine is responsible for:

- Evaluating proposed actions.
- Determining allow, ask, or deny.
- Applying workspace and path restrictions.
- Evaluating process, network, and credential risk.
- Caching approved capabilities.
- Recording policy decisions.
- Integrating external policy systems where needed.

### 5.7 Sandbox layer

The sandbox layer is responsible for:

- Filesystem isolation.
- Process execution.
- Network isolation.
- Resource limits.
- Environment management.
- Snapshot or reset behavior.
- Local or remote execution abstraction.

### 5.8 Quality gate

The quality gate is responsible for:

- Comparing results with acceptance criteria.
- Running deterministic checks.
- Detecting unverified claims.
- Checking for unrelated changes.
- Evaluating tests, linting, formatting, and static analysis.
- Returning structured feedback to the agent when work is incomplete.

### 5.9 Persistence and event store

Persistence is responsible for:

- Sessions.
- Events.
- Messages.
- Tool calls.
- Approvals.
- Artifacts.
- Checkpoints.
- Memory.
- Replay data.

### 5.10 Extension system

The extension system may support:

- Additional tools.
- Hooks.
- Provider adapters.
- Skills.
- Policy modules.
- Sandbox backends.
- Client integrations.
- Observability exporters.

Extensions should not receive unrestricted trust merely because they are installed.

---

## 6. Agent execution loop

The harness should use a controlled iterative execution model.

A normal turn should conceptually include:

1. Check session limits.
2. Build the current context.
3. Select tools that are relevant and permitted.
4. Call the selected model.
5. Stream model events to the client.
6. Collect valid tool requests.
7. Validate and authorize each request.
8. Ask for approval when required.
9. Execute allowed actions.
10. Record results.
11. Feed results back into the next model turn.
12. When no further tool call is requested, invoke the quality gate.
13. Finish only when completion criteria are satisfied or a limit is reached.

The execution model should support:

- Streaming.
- Cancellation.
- Time limits.
- Token limits.
- Cost limits.
- Tool-call limits.
- Turn limits.
- Model retries.
- Tool retries for idempotent operations.
- Parallel execution for independent read-only work.
- Serialized execution for mutating operations.
- Structured errors.
- Resumability.

The system should avoid hiding important control flow inside a model prompt. Execution policy should remain visible in runtime logic.

---

## 7. Repository instructions with `AGENTS.md`

### 7.1 Purpose

`AGENTS.md` should hold durable instructions about how an agent should work within a repository.

Appropriate content includes:

- Repository purpose.
- Important directory responsibilities.
- Build commands.
- Test commands.
- Linting and formatting expectations.
- Architectural constraints.
- Generated-file warnings.
- Dependency-management rules.
- Security-sensitive areas.
- Pull request expectations.
- Project-specific conventions.
- Areas that must not be modified.

### 7.2 What should not go into `AGENTS.md`

It should not become a general prompt dump.

Avoid placing the following there:

- Large tutorials.
- Complete API documentation.
- Long code examples.
- Temporary task instructions.
- Frequently changing operational status.
- Full reusable workflows better represented as skills.
- Secrets.
- Tool credentials.
- Unverified model-generated knowledge.

### 7.3 Hierarchical behavior

The harness should support:

- User-level global instructions.
- Repository-root instructions.
- Nested instructions for subdirectories.
- Closest-scope precedence.
- Explicit user instructions overriding project defaults.
- Clear reporting of which instruction files were loaded.
- Conflict detection.

### 7.4 Trust and safety

Instruction files should be treated as untrusted content until the repository is trusted.

The harness should:

- Avoid executing commands merely because an instruction file mentions them.
- Record instruction file origin and hash.
- Apply size limits.
- Resolve symbolic links safely.
- Warn when instructions attempt to access credentials or paths outside the workspace.
- Distinguish project guidance from system-enforced policy.

---

## 8. Skills

### 8.1 Purpose

A skill is a reusable procedure that teaches the agent how to perform a class of tasks.

Examples include:

- Reviewing a pull request.
- Diagnosing a failing Python test suite.
- Migrating an API.
- Performing a security review.
- Updating documentation.
- Preparing a release.
- Running a project-specific validation process.

Skills should be portable and discoverable.

### 8.2 Recommended standard

The harness should follow the Agent Skills specification rather than inventing a proprietary format.

A skill may include:

- A human-readable name.
- A description used for discovery.
- Main instructions.
- Optional compatibility constraints.
- Optional tool restrictions.
- References.
- Supporting assets.
- Deterministic scripts.

### 8.3 Progressive disclosure

The system should not load every skill into every prompt.

Recommended behavior:

1. Discover skills.
2. Load only concise metadata.
3. Present relevant skill names and descriptions to the model.
4. Activate a skill only when needed.
5. Load the main instructions on activation.
6. Load referenced material only when required.
7. Preserve active skill state during context compaction.
8. Avoid activating the same skill repeatedly.

### 8.4 Skill trust

Skills can contain powerful instructions and scripts. They should be governed by:

- Source trust.
- Tool permissions.
- Script approval.
- Version tracking.
- Integrity hashes.
- Compatibility checks.
- Explicit restrictions on credentials and network use.

### 8.5 Relationship to other concepts

- `AGENTS.md` defines repository rules.
- Skills define reusable procedures.
- Tools perform actions.
- Hooks perform deterministic lifecycle automation.
- Plugins distribute capabilities.
- Memory stores approved learned facts.

These concepts should not be merged.

---

## 9. Tool system

### 9.1 Native tools

Core operations should normally remain native because they require precise control.

Likely native capabilities include:

- File reading.
- File writing.
- Anchored edits.
- Patch application.
- Text search.
- File search.
- Git inspection.
- Git diff.
- Test execution.
- Shell execution.
- Repository metadata.
- Language-service access.
- Artifact storage.

### 9.2 MCP tools

MCP should be used for external or organizational integrations such as:

- Git hosting.
- Issue trackers.
- Documentation systems.
- Databases.
- Cloud services.
- Browsers.
- Team communication systems.
- Internal enterprise APIs.

MCP should not replace the core permission model, filesystem layer, or sandbox.

### 9.3 Tool metadata

Every tool should have metadata describing:

- Name.
- Purpose.
- Input schema.
- Output schema where useful.
- Risk category.
- Whether it is read-only.
- Whether it is idempotent.
- Whether it is safe to execute in parallel.
- Timeout.
- Required capabilities.
- Network behavior.
- Credential requirements.
- Expected side effects.

### 9.4 Tool selection

The harness should avoid exposing every installed tool on every turn.

Tool availability should be filtered using:

- Current task.
- Agent profile.
- Permission mode.
- Active skills.
- Repository type.
- Tool relevance.
- Trust level.
- Sandbox capabilities.

This reduces context size, tool confusion, and accidental side effects.

### 9.5 Tool errors

Tool results should distinguish:

- Invalid arguments.
- Permission denied.
- Approval rejected.
- Timeout.
- Process failure.
- Resource exhaustion.
- Conflict.
- Unsupported capability.
- Transient external error.
- Permanent external error.
- Partial success.

The model should receive structured errors rather than raw stack traces alone.

---

## 10. Model provider abstraction

The runtime should not be coupled to any provider-specific response object.

Provider differences should be normalized into common concepts such as:

- Text output.
- Structured output.
- Tool calls.
- Streaming deltas.
- Usage.
- Reasoning summaries when available.
- Safety refusal.
- Rate-limit failure.
- Context-limit failure.
- Provider error.

The abstraction should allow provider-specific features without forcing every provider into the lowest common denominator.

Examples:

- A model that supports native patch tools may use them.
- A model that supports prompt caching may expose that capability.
- A model that supports long context may receive different context policy.
- A model that supports computer use may expose additional tools.

The core runtime should use capability negotiation rather than provider name checks wherever possible.

A general provider router may be used as an optional adapter, but the harness should retain its own internal request, event, and error models.

---

## 11. Context management

Context management is a central differentiator and should remain under direct control.

### 11.1 Context categories

Context should be separated into at least three categories.

#### Pinned context

Pinned context should remain available unless explicitly replaced.

Examples:

- System policy.
- User request.
- Acceptance criteria.
- Active repository instructions.
- Active skills.
- Current plan.
- Safety constraints.
- Important unresolved issues.

#### Working context

Working context is actively relevant but may change during execution.

Examples:

- Recently read files.
- Current diff.
- Recent tool results.
- Current test failures.
- Active subagent findings.
- Current implementation decisions.

#### Evictable context

Evictable context can be summarized or moved to artifacts.

Examples:

- Old command output.
- Large logs.
- Repeated file contents.
- Completed exploration.
- Earlier failed approaches.
- Intermediate search results.

### 11.2 Artifact offloading

Large content should be stored outside the active prompt and represented by references.

Examples:

- Full test logs.
- Build logs.
- Large diffs.
- Generated reports.
- Dependency graphs.
- Static-analysis results.

The active context should contain:

- A concise summary.
- Relevant excerpts.
- A durable artifact reference.
- Provenance.

### 11.3 Structured compaction

Compaction should preserve task state rather than produce an informal narrative.

A compacted state should preserve:

- User objective.
- Acceptance criteria.
- Active instructions.
- Active skills.
- Current plan.
- Files inspected.
- Files changed.
- Commands run.
- Tests and checks.
- Important decisions.
- Remaining problems.
- Artifacts.
- Risks.
- Open questions.

### 11.4 Context provenance

The harness should track where every major context element came from:

- User message.
- System policy.
- Instruction file.
- Skill.
- Tool output.
- External service.
- Model summary.
- Subagent result.
- Memory.

This helps prevent model summaries from silently replacing authoritative sources.

### 11.5 Chain-of-thought policy

The harness should not depend on storing private chain-of-thought.

It should store:

- Plans.
- Decisions.
- Evidence.
- Assumptions.
- Alternatives considered at a high level.
- Results.
- Confidence.
- Unresolved questions.

That is sufficient for reproducibility and auditing.

---

## 12. Repository understanding

The harness should use layered repository intelligence.

### 12.1 Text and metadata search

The first layer should be fast and inexpensive:

- Text search.
- File-name search.
- Manifest inspection.
- Git status.
- Git history.
- Dependency files.
- Build configuration.
- Existing documentation.

### 12.2 Syntax-aware analysis

Syntax parsing can provide:

- Function and class boundaries.
- Imports.
- Definitions.
- Call-site approximations.
- Symbol extraction.
- Basic dependency maps.
- Safer edit boundaries.

### 12.3 Language-server integration

LSP can provide:

- Definitions.
- References.
- Diagnostics.
- Workspace symbols.
- Rename support.
- Language-specific semantic understanding.

Language servers should be started lazily and only for relevant languages.

### 12.4 Optional semantic indexing

Semantic indexing may be useful for very large repositories, but it should not be mandatory for the first version.

Before adding vector retrieval, measure whether it improves:

- File discovery.
- Symbol discovery.
- Cross-module understanding.
- Latency.
- Cost.
- Task success.

Text search, syntax information, and repository metadata may outperform an immature semantic index.

---

## 13. Code editing

Edit quality is a core reliability feature.

### 13.1 Preferred behavior

The harness should favor targeted, verifiable edits rather than arbitrary full-file regeneration.

Useful edit modes include:

- Anchored replacement.
- Structured patch application.
- Syntax-aware replacement.
- Full-file replacement only when justified.
- Generated-file updates through the project’s generator rather than direct editing.

### 13.2 Precondition checks

Before applying an edit, the system should verify:

- The file still matches the version the model inspected.
- The intended target exists.
- The target is unambiguous.
- The path is allowed.
- The file is not generated or protected.
- The edit does not cross workspace boundaries.

### 13.3 Post-edit checks

After applying an edit, the system should:

- Produce a diff.
- Validate syntax where practical.
- Track inverse changes.
- Detect unexpected file modifications.
- Make rollback possible.
- Run relevant formatting or tests based on policy.

### 13.4 Concurrency

Two writing agents should not modify the same working tree without explicit coordination.

Safer options include:

- Isolated worktrees.
- Isolated branches.
- File ownership.
- Serialized writes.
- Patch-only subagent output.

---

## 14. Shell and process execution

Shell access is necessary but high risk.

### 14.1 Execution principles

The harness should:

- Prefer argument-based process execution over raw shell strings.
- Restrict the working directory.
- Limit environment variables.
- Remove credentials by default.
- Enforce timeouts.
- Enforce output limits.
- Kill complete process groups.
- Record exit status and resource usage.
- Distinguish process execution from network permission.
- Treat package installation as a higher-risk action.
- Detect shell escapes and nested shell invocation where practical.

### 14.2 Risk categories

Process requests should be classified based on:

- Read-only inspection.
- Build or test execution.
- Workspace mutation.
- Dependency installation.
- Network access.
- Credential use.
- External side effects.
- Destructive behavior.
- Privilege escalation.
- Host access.

### 14.3 Output handling

Large command output should be written to artifacts.

The model should receive:

- Exit code.
- Duration.
- Short summary.
- Relevant excerpt.
- Artifact reference.
- Truncation status.

---

## 15. Permission and approval model

### 15.1 Core decisions

The simplest useful permission model is:

- Allow.
- Ask.
- Deny.

### 15.2 Policy dimensions

Authorization may depend on:

- Tool.
- Path.
- Command.
- Working directory.
- Network destination.
- Credential scope.
- Repository trust.
- User mode.
- Agent profile.
- Skill.
- External side effects.
- Previous approval.
- Session state.

### 15.3 Suggested defaults

Reasonable starting defaults include:

- Reading within a trusted repository: allow.
- Searching within a trusted repository: allow.
- Running tests: allow.
- Writing within the workspace: ask or allow under an explicit edit mode.
- Deleting files: ask.
- Installing dependencies: ask.
- Network access: ask.
- Reading credential files: deny.
- Accessing the user’s home directory: deny by default.
- Pushing commits: ask.
- Creating external issues or pull requests: ask.
- Destructive cloud or production operations: deny unless explicitly enabled.

### 15.4 Approval caching

Approval should be cached by normalized capability rather than by exact text.

A user may approve a category such as:

- Running a specific test command in the repository.
- Writing files within a specific directory.
- Accessing a specific network host.
- Using a named credential scope.
- Performing a repeated safe action for the current session.

Approvals should have scope and expiry.

### 15.5 Enterprise policy

For enterprise deployments, the runtime may integrate with an external policy engine.

External policy should decide authorization, while the harness remains responsible for:

- Enforcing the decision.
- Auditing.
- User explanation.
- Approval flow.
- Tool execution.

---

## 16. Hooks

Hooks provide deterministic lifecycle automation.

Potential hook points include:

- Session start.
- Session resume.
- Before context construction.
- Before model invocation.
- After model invocation.
- Before authorization.
- Before tool execution.
- After tool execution.
- Tool failure.
- Before compaction.
- After compaction.
- Before quality evaluation.
- Before final response.
- Session end.

Hooks may be used for:

- Logging.
- Formatting.
- Adding project context.
- Running lightweight checks.
- Notifications.
- Policy enrichment.
- Artifact capture.
- Organization-specific automation.

Hooks should not be the sole security boundary.

Hook behavior should be:

- Time-limited.
- Isolated from the core runtime.
- Ordered deterministically.
- Auditable.
- Unable to silently change actions without reauthorization.
- Fail-safe.

---

## 17. Sandboxing

### 17.1 Purpose

The sandbox protects the host from model-generated actions and protects the task from environmental inconsistency.

### 17.2 Desired properties

A strong sandbox should support:

- Non-root execution.
- Ephemeral environments.
- Restricted filesystem mounts.
- Workspace-specific write access.
- Network disabled by default.
- CPU limits.
- Memory limits.
- Process limits.
- Disk limits.
- Time limits.
- Environment sanitization.
- No host container socket.
- No privileged mode.
- Reproducible images or environments.
- Cleanup after completion.

### 17.3 Abstraction

The harness should support more than one sandbox backend.

Potential forms include:

- Local restricted execution.
- Local container.
- Remote container.
- Virtual machine.
- Managed remote development environment.
- Organization-specific sandbox.

The rest of the runtime should depend on capabilities rather than a specific vendor or container engine.

### 17.4 Sandbox as a separate execution boundary

The agent process and the code-execution environment should be separable.

This enables:

- Remote execution.
- Stronger isolation.
- Multiple language environments.
- Reproducibility.
- Horizontal scaling.
- Worktree isolation.
- Enterprise deployment.

---

## 18. Goals, plans, and quality gates

### 18.1 Goals

Each significant task should have:

- Objective.
- Acceptance criteria.
- Constraints.
- Non-goals.
- Verification expectations.

The harness may infer these from the user request but should expose them for correction when uncertainty is material.

### 18.2 Plans

Plans should remain lightweight and editable.

A plan may track:

- Investigation.
- Proposed changes.
- Verification.
- Documentation.
- Completion.

The plan should not become a rigid workflow that prevents the agent from adapting.

### 18.3 Quality gates

The agent should not declare success based only on its own narrative.

A quality gate should check:

- Whether the requested behavior exists.
- Whether relevant tests passed.
- Whether formatting and linting passed.
- Whether static-analysis findings were introduced.
- Whether unrelated files changed.
- Whether generated files were handled correctly.
- Whether documentation was updated when required.
- Whether unverified claims are clearly labeled.
- Whether acceptance criteria are supported by evidence.
- Whether secrets or sensitive files were added.

The quality gate may return structured feedback and request another agent turn.

---

## 19. Subagents

### 19.1 Purpose

Subagents are useful for bounded, separable work such as:

- Repository exploration.
- Independent review.
- Test failure analysis.
- Documentation research.
- Security review.
- Comparing implementation options.
- Working on isolated modules.

### 19.2 Design principles

Subagents should:

- Reuse the same runtime.
- Receive limited context.
- Receive only necessary tools.
- Have explicit budgets.
- Have limited recursion depth.
- Return structured results.
- Preserve evidence.
- Avoid editing shared state unless isolated.
- Remain visible to the user.

### 19.3 Suggested limits

Reasonable defaults include:

- No automatic delegation unless justified.
- Low maximum depth.
- Small concurrency limit.
- Separate worktrees for writing tasks.
- Serialized merge or patch review.
- Explicit parent responsibility for final quality.

### 19.4 Structured result

A subagent result should include:

- Summary.
- Evidence.
- Files inspected.
- Files changed.
- Tests run.
- Artifacts.
- Unresolved issues.
- Confidence.
- Suggested next action.

### 19.5 A2A usage

A2A should be reserved for remote, independently operated agents with their own:

- Identity.
- Lifecycle.
- Authentication.
- Task state.
- Streaming.
- Failure behavior.
- Trust domain.

Local subagents should use a simpler internal protocol.

---

## 20. Memory and persistence

### 20.1 Separate concepts

The design should distinguish:

- Project instructions.
- Skills.
- Session state.
- Artifacts.
- Checkpoints.
- Long-term memory.
- External knowledge.

### 20.2 Session persistence

A session should be resumable after:

- Client disconnect.
- Runtime restart.
- Tool failure.
- Model failure.
- User pause.
- Approval delay.

### 20.3 Event-oriented storage

The most robust model is an append-oriented event history from which current state can be reconstructed.

Events may include:

- User messages.
- Model events.
- Tool calls.
- Tool results.
- Policy decisions.
- Approvals.
- Context compaction.
- Skill activation.
- File changes.
- Checkpoints.
- Quality results.
- Final outcome.

### 20.4 Long-term memory

Long-term memory should be conservative.

A memory item should include:

- Content.
- Type.
- Source.
- Evidence.
- Confidence.
- Timestamp.
- Expiry where appropriate.
- User or policy approval.
- Scope.

The model should not silently convert temporary observations into permanent memory.

### 20.5 Initial storage strategy

A relational embedded database is sufficient for an initial implementation.

A vector database should be added only when measured retrieval requirements justify it.

---

## 21. Editor integration with ACP

The harness should avoid being tied to one editor.

ACP is an appropriate boundary for communication between an editor and an agent runtime.

Editor integration may support:

- Starting sessions.
- Streaming messages.
- Showing diffs.
- Approval prompts.
- Context selection.
- File references.
- Cancellation.
- Resume.
- Status display.

The internal runtime should not use ACP as its own state model. ACP should translate between client-facing concepts and internal events.

---

## 22. Remote agents with A2A

A2A may be useful for:

- Delegating work to a specialized remote service.
- Interacting with organizational agents.
- Long-running independent tasks.
- Cross-team agent federation.
- Cloud-hosted analysis agents.

A2A should not be used merely because the system contains more than one agent.

For local subagents, an internal protocol is simpler, faster, and easier to secure.

---

## 23. Plugin and extension model

### 23.1 Plugin responsibilities

A plugin may provide:

- Tools.
- Hooks.
- Skills.
- Provider adapters.
- Policy modules.
- Sandbox adapters.
- Observability exporters.
- Client integrations.

### 23.2 Plugin requirements

Plugins should declare:

- Name and version.
- Compatible harness API.
- Capabilities.
- Required permissions.
- Filesystem scope.
- Network scope.
- Credential scope.
- Dependencies.
- Trust requirements.

### 23.3 Trust model

Installation should not imply unrestricted trust.

The system should consider:

- Metadata-only discovery.
- Explicit enablement.
- Capability approval.
- Process isolation.
- Signature or integrity verification.
- Version pinning.
- Audit logs.
- Out-of-process execution for untrusted plugins.

### 23.4 Relationship to skills

Plugins distribute executable or integrated capabilities.

Skills distribute reusable procedures.

A plugin may contain skills, but a skill should remain portable and usable without requiring a proprietary plugin when possible.

---

## 24. Observability

OpenTelemetry is the preferred standard for traces, metrics, and logs.

Useful observability dimensions include:

- Session.
- Turn.
- Model.
- Provider.
- Tool.
- Tool risk.
- Approval requirement.
- Tool duration.
- Input tokens.
- Output tokens.
- Cost.
- Cache behavior.
- Context size.
- Compaction count.
- Subagent depth.
- Sandbox backend.
- Test results.
- Errors.
- Retry count.
- Cancellation.
- Completion status.

Observability should not capture secrets, full credentials, or unnecessary source code by default.

The system should support configurable redaction.

---

## 25. Replay

Replay is required for debugging and evaluation.

A replay record should preserve:

- Normalized model request.
- Model response events.
- Tool schemas.
- Tool calls.
- Tool results.
- Instruction hashes.
- Skill hashes.
- Policy decisions.
- Approval decisions.
- Environment fingerprint.
- Sandbox identity.
- Repository state.
- Artifacts.
- Timing.
- Cost.

Useful replay modes include:

- Reusing recorded model output while rerunning tools.
- Reusing recorded model output and tool output.
- Replaying only context construction.
- Replaying only authorization decisions.
- Comparing two models on the same recorded environment.

Replay should avoid depending on hidden reasoning traces.

---

## 26. Evaluation strategy

### 26.1 Unit evaluation

Test isolated behaviors such as:

- Instruction precedence.
- Skill discovery.
- Skill activation.
- Tool validation.
- Permission decisions.
- Approval caching.
- Path restrictions.
- Patch conflicts.
- Context compaction.
- Event reconstruction.
- Cancellation.
- Timeout behavior.

### 26.2 Integration evaluation

Use controlled repositories and environments to test:

- Repository exploration.
- Editing.
- Testing.
- Git behavior.
- Sandbox behavior.
- MCP integration.
- ACP integration.
- Session resume.
- Subagent isolation.
- Plugin loading.

### 26.3 Behavioral task suites

Representative tasks should include:

- Fixing a failing test.
- Adding a small feature.
- Refactoring without behavior change.
- Diagnosing without editing.
- Updating documentation.
- Handling conflicting instructions.
- Refusing unsafe actions.
- Recovering after a failed tool.
- Resuming an interrupted task.
- Working within a cost budget.

### 26.4 Metrics

Useful metrics include:

- Task success.
- Test pass rate.
- Correct-file change rate.
- Unrelated-file change rate.
- Number of approvals.
- Tool-call count.
- Token use.
- Cost.
- Wall-clock latency.
- Recovery rate.
- Resume success.
- Policy violation rate.
- Revert rate.
- User intervention rate.
- Final-answer factual accuracy.
- Unverified-claim rate.

### 26.5 Security evaluation

The system should be tested against:

- Malicious repository instructions.
- Prompt injection in source files.
- Path traversal.
- Symlink escape.
- Credential exfiltration.
- Dependency confusion.
- Shell injection.
- Network misuse.
- Untrusted MCP servers.
- Malicious plugins.
- Conflicting nested instructions.
- Sandbox escape attempts.
- Large-output denial of service.
- Recursive subagent explosions.

---

## 27. Standards to follow

### 27.1 `AGENTS.md`

Use for repository-specific instructions.

Important principles:

- Markdown format.
- Hierarchical scope.
- Closest-file precedence.
- Explicit user instructions take priority.
- Human-readable and version-controlled.
- No assumption that instructions are trusted executable policy.

### 27.2 Agent Skills

Use for reusable procedural knowledge.

Important principles:

- Metadata-first discovery.
- Main instructions loaded on activation.
- Optional references, assets, and scripts.
- Progressive disclosure.
- Tool restrictions where supported.
- Portable skill representation.

### 27.3 MCP

Use for external tools, prompts, and resources.

Important principles:

- Capability negotiation.
- Typed tool interfaces.
- Clear trust boundaries.
- Server isolation.
- Authorization outside the model.
- External integrations should not bypass central policy.

### 27.4 ACP

Use for client and editor integration.

Important principles:

- Runtime independent of editor.
- Streamed events.
- Diff-aware interaction.
- Approval and cancellation support.
- Client-specific rendering outside the core runtime.

### 27.5 A2A

Use only for independent remote agents.

Important principles:

- Remote identity.
- Task lifecycle.
- Authentication.
- Streaming.
- Failure isolation.
- Cross-trust-domain operation.

### 27.6 LSP

Use for language intelligence.

Important principles:

- Lazy startup.
- Capability detection.
- Language-specific semantics.
- Avoid relying on LSP for all repository understanding.

### 27.7 OCI

Use as the conceptual standard for portable sandbox execution.

Important principles:

- Runtime portability.
- Image reproducibility.
- Resource isolation.
- Avoid hard-coding one container engine.

### 27.8 OpenTelemetry

Use for observability.

Important principles:

- Standard traces, metrics, and logs.
- Context propagation.
- Pluggable exporters.
- Redaction.

### 27.9 SARIF

Use for static-analysis and security findings.

Important principles:

- Normalized machine-readable findings.
- Integration with code-hosting and analysis systems.
- Stable artifact representation.

### 27.10 JSON Schema

Use for:

- Tool inputs.
- Structured outputs.
- Plugin manifests where appropriate.
- Configuration validation.
- Protocol translation.

---

## 28. Optional implementation candidates

The following are possible implementation aids. They are not binding architectural decisions.

### 28.1 Data validation and schemas

Potential options:

- Pydantic.
- Dataclasses with JSON Schema tooling.
- TypeScript schema libraries.
- Protocol Buffer or equivalent for service boundaries.

Desired capability:

- Runtime validation.
- Serialization.
- Schema generation.
- Versioning.
- Good error messages.

### 28.2 Asynchronous runtime and networking

Potential options:

- Native asynchronous language runtime.
- AnyIO.
- HTTPX.
- Equivalent async libraries in another implementation language.

Desired capability:

- Cancellation propagation.
- Timeouts.
- Streaming.
- Backpressure.
- Structured concurrency.

### 28.3 CLI and TUI

Potential options:

- Typer.
- Rich.
- Textual.
- Equivalent tools in Rust, TypeScript, or Go.

Desired capability:

- Thin client.
- Event streaming.
- Diff rendering.
- Approval prompts.
- Session resume.

### 28.4 Persistence

Potential options:

- SQLite.
- PostgreSQL for multi-user deployment.
- Embedded event stores.
- Object storage for artifacts.

Desired capability:

- Transactions.
- Append-oriented events.
- Resumability.
- Migration support.
- Artifact references.

### 28.5 Code intelligence

Potential options:

- Ripgrep.
- Tree-sitter.
- Language servers.
- Git command-line tools.
- Native parser libraries.

Desired capability:

- Fast search.
- Syntax awareness.
- Semantic references.
- Incremental operation.

### 28.6 Sandboxing

Potential options:

- Docker.
- Podman.
- OCI runtimes.
- Remote container services.
- Virtual machines.
- MicroVMs.
- Organization-specific sandbox systems.

Desired capability:

- Isolation.
- Limits.
- Reproducibility.
- Network control.
- Workspace mounting.
- Cleanup.

### 28.7 Policy

Potential options:

- Internal rule engine.
- Open Policy Agent.
- Organization-specific authorization service.

Desired capability:

- Allow, ask, deny.
- Explainable decisions.
- Context-aware authorization.
- External policy integration.

### 28.8 Workflow frameworks

Potential options:

- Plain custom asynchronous loop.
- LangGraph.
- Temporal.
- Durable task frameworks.
- State-machine libraries.

Recommendation:

Start with a custom runtime loop. Add a workflow framework only when concrete requirements justify it, such as distributed durability, complex branching, or external task orchestration.

### 28.9 Provider routing

Potential options:

- Direct provider adapters.
- LiteLLM or equivalent as an optional compatibility layer.
- Self-hosted inference gateways.

Recommendation:

Keep an internal provider-neutral event model. Third-party routers should remain adapters, not become the domain model.

---

## 29. Major architectural tradeoffs

### 29.1 Custom loop versus workflow framework

Custom loop advantages:

- Maximum control.
- Easier debugging.
- Clear cancellation.
- Lower abstraction overhead.
- Easier policy integration.

Workflow framework advantages:

- Durable state.
- Checkpointing.
- Graph execution.
- Distributed tasks.
- Existing orchestration features.

Recommended direction:

Start custom. Add a durable framework only when a measured requirement appears.

### 29.2 Native tools versus MCP tools

Native tool advantages:

- Better performance.
- Stronger security control.
- Better error semantics.
- Tight filesystem and sandbox integration.

MCP advantages:

- Interoperability.
- External ecosystem.
- Easier integration with services.
- Independent server development.

Recommended direction:

Keep coding-critical tools native and use MCP for external integrations.

### 29.3 Single agent versus multi-agent

Single-agent advantages:

- Lower cost.
- Lower latency.
- Easier debugging.
- Fewer merge conflicts.
- Simpler context model.

Multi-agent advantages:

- Parallel investigation.
- Specialized review.
- Independent verification.
- Better handling of separable tasks.

Recommended direction:

Default to single agent. Add bounded delegation.

### 29.4 Local execution versus remote sandbox

Local advantages:

- Low latency.
- Easy development.
- User control.
- Offline support.

Remote advantages:

- Stronger isolation.
- Reproducibility.
- Scalable resources.
- Enterprise control.
- Persistent long-running tasks.

Recommended direction:

Design an abstraction that supports both.

### 29.5 Automatic memory versus conservative memory

Automatic memory advantages:

- Convenience.
- Personalization.
- Lower repeated explanation.

Risks:

- Incorrect facts.
- Stale facts.
- Privacy concerns.
- Hidden behavioral drift.
- Prompt injection persistence.

Recommended direction:

Conservative, approved, scoped memory.

### 29.6 Full context versus retrieval and compaction

Full context advantages:

- Simplicity.
- Fewer retrieval failures.
- Better global awareness in small repositories.

Retrieval and compaction advantages:

- Lower cost.
- Better scalability.
- Less distraction.
- Faster inference.

Recommended direction:

Use full context only when affordable. Otherwise use layered search, pinned state, and structured compaction.

### 29.7 Automatic action versus human approval

Automatic action advantages:

- Speed.
- Better autonomous workflows.
- Lower user friction.

Approval advantages:

- Safety.
- User control.
- Better handling of side effects.
- Trust.

Recommended direction:

Use risk-based permissions with user-selectable modes.

---

## 30. Non-goals for the initial design

The initial system should not require:

- A marketplace.
- Unlimited subagent swarms.
- Automatic long-term memory.
- A vector database.
- A proprietary skill format.
- A proprietary repository instruction format.
- A custom editor protocol.
- A complex graph runtime.
- Production cloud deployment.
- Multi-user collaboration.
- Automatic deployment to production.
- Unrestricted browser control.
- Full computer-use automation.
- Support for every model provider.
- Support for every programming language.
- Self-modifying core runtime behavior.

These may be evaluated later.

---

## 31. Recommended capability phases

### Phase 1: dependable single-agent runtime

Focus on:

- Provider-neutral model interface.
- Controlled agent loop.
- Event streaming.
- Repository reading and search.
- Safe editing.
- Shell and test execution.
- Git diff.
- Permission engine.
- Basic client.
- Session limits.
- Clear final reporting.

Success condition:

The system can reliably complete small repository tasks without unsafe actions or unexplained changes.

### Phase 2: project-aware behavior

Add:

- `AGENTS.md`.
- Skill discovery.
- Skill activation.
- Context budgeting.
- Artifact offloading.
- Structured compaction.
- Goals.
- Acceptance criteria.
- Quality gates.

Success condition:

The system can work effectively in nontrivial repositories while respecting project rules.

### Phase 3: durability and isolation

Add:

- Persistent event store.
- Resume.
- Checkpoints.
- Container or remote sandbox.
- Approval caching.
- Hooks.
- Telemetry.
- Replay.

Success condition:

The system can survive interruption, support debugging, and run with meaningful isolation.

### Phase 4: interoperability

Add:

- MCP client.
- ACP server.
- Plugin model.
- External policy integration.
- Additional sandbox backends.
- Additional provider adapters.

Success condition:

The system can integrate with editors, services, and organization-specific tooling without core modification.

### Phase 5: controlled delegation

Add:

- Agent profiles.
- Subagents.
- Worktree isolation.
- Concurrency controls.
- Structured delegation results.
- Optional A2A support.

Success condition:

Delegation improves measurable task outcomes without causing uncontrolled cost, complexity, or merge conflicts.

---

## 32. Product behavior expectations

The user experience should make the following visible:

- Current task.
- Current plan.
- Active instructions.
- Active skills.
- Model being used.
- Tools available.
- Tool currently running.
- Approval requests.
- Files changed.
- Current diff.
- Tests run.
- Cost and token use where available.
- Errors.
- Completion evidence.
- Unverified items.

The system should avoid:

- Pretending untested changes are correct.
- Hiding failed commands.
- Hiding denied actions.
- Claiming completion when limits were reached.
- Overwriting user work.
- Silently changing permission modes.
- Silently activating powerful plugins.
- Silently storing long-term memory.

---

## 33. Final answer contract

At task completion, the harness should produce a structured and honest report covering:

- What was changed.
- Why it was changed.
- Which files were affected.
- Which tests or checks were run.
- Results of those checks.
- Any failures.
- Any assumptions.
- Anything not verified.
- Any remaining risks.
- Suggested next action when work is incomplete.

The final answer should never imply that a command, test, deployment, or validation occurred unless an event confirms it.

---

## 34. Security principles

The harness should assume that all of the following may be malicious:

- Repository contents.
- Comments.
- Documentation.
- `AGENTS.md`.
- Skills from untrusted sources.
- MCP servers.
- Tool output.
- Web content.
- Dependency metadata.
- Generated patches.
- Plugins.
- Subagent output.

The harness must distinguish data from instructions.

Security controls should include:

- Workspace boundaries.
- Canonical path resolution.
- Symlink checks.
- Credential isolation.
- Network controls.
- Output limits.
- Timeouts.
- Process limits.
- Plugin permissions.
- MCP trust configuration.
- Explicit approval.
- Audit logs.
- Sandbox isolation.
- Policy enforcement below the model.

---

## 35. Open design questions

The following questions should remain open until implementation constraints are clearer.

### Runtime

- Which primary implementation language best fits the desired portability, performance, and ecosystem?
- Should the runtime be a local process, daemon, service, or support all three?
- How should clients discover and connect to the runtime?

### Event model

- Which events are stable public API?
- How should event schemas be versioned?
- How much model-provider detail should be preserved?

### Context

- What token-budget policy should be used?
- How should file relevance be scored?
- When should semantic indexing be introduced?
- How should compaction quality be evaluated?

### Editing

- Which edit primitives should be first-class?
- When should syntax-aware edits be required?
- How should merge conflicts be exposed?

### Sandbox

- What is the default local sandbox?
- How should Windows, macOS, and Linux differ?
- Is remote execution a first-release requirement?

### Permissions

- What are the default permission modes?
- Which actions may be approved for the whole session?
- How should organizational policy override user preference?

### Skills

- Which skill locations are supported?
- How are skill versions resolved?
- How are skill scripts trusted?
- Should the harness maintain a skill registry?

### Plugins

- Are plugins loaded in-process or out-of-process?
- How is plugin compatibility managed?
- Is signature verification required?

### Subagents

- When is delegation allowed automatically?
- How are budgets divided?
- How are conflicting findings resolved?
- How are patches merged?

### Memory

- What may be stored automatically?
- What requires approval?
- How is memory deleted or expired?
- How is memory scoped by user, repository, and organization?

### Evaluation

- Which tasks represent the target workload?
- Which metrics determine whether a feature should be retained?
- What is the acceptable cost and latency envelope?

---

## 36. Decision rules for future implementation

When selecting an implementation approach, prefer the option that:

1. Makes behavior observable.
2. Keeps policy enforceable outside the model.
3. Supports cancellation.
4. Supports deterministic testing.
5. Preserves user control.
6. Avoids unnecessary protocol coupling.
7. Supports replay.
8. Minimizes irreversible side effects.
9. Allows components to be replaced.
10. Has measurable impact on task success.
11. Does not introduce a framework merely for conceptual elegance.
12. Keeps the core runtime understandable.

Any dependency or framework should justify itself through one or more of:

- Reduced implementation risk.
- Better interoperability.
- Stronger safety.
- Better reliability.
- Better performance.
- Better maintainability.
- Reduced duplicated work.

Popularity alone is not sufficient.

---

## 37. Summary of recommended direction

The recommended harness is:

- A modular, provider-neutral coding runtime.
- Built around a controlled asynchronous agent loop.
- Independent of any one client.
- Aware of hierarchical `AGENTS.md` instructions.
- Compatible with Agent Skills.
- Equipped with native coding tools.
- Compatible with MCP for external tools.
- Capable of ACP-based editor integration.
- Capable of A2A only for genuine remote-agent federation.
- Protected by a central policy and approval engine.
- Executing code inside replaceable sandbox backends.
- Using structured context management and compaction.
- Using explicit goals and quality gates.
- Persistent, resumable, and replayable.
- Observable through OpenTelemetry.
- Evaluated through realistic repository tasks.
- Single-agent by default.
- Multi-agent only under controlled delegation.
- Extensible without allowing extensions to bypass safety.

The most important strategic point is this:

A high-quality coding harness is not primarily differentiated by the number of models, agents, tools, or integrations it supports. It is differentiated by how reliably it selects context, applies edits, controls side effects, recovers from failure, verifies results, and tells the truth about what happened.
