from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field
from collections.abc import Awaitable, Mapping

from harness.agent.types import JSONValue
from harness.agent.messages import WireModel


class ToolCancellationToken(Protocol):
    """If this token is there then stop the tool execution"""

    def is_cancelled(self) -> bool:
        """return whether the tool should stop"""
        ...


class ToolExecutor(Protocol):
    """Async callable to execute the tool"""

    def __call__(
        self,
        arguments: Mapping[str, JSONValue],
        signal: ToolCancellationToken | None = None,
    ) -> Awaitable[AgentToolResult]:
        """execute a tool with cancellation support"""
        ...


class ToolCall(WireModel):
    """Agent asks for this tool to be executed"""

    id: str
    name: str
    arguments: dict[str, JSONValue] = Field(default_factory=dict)


class AgentToolResult(WireModel):
    """Result from an executed tool call"""

    tool_call_id: str
    name: str
    ok: bool
    content: str
    data: dict[str, JSONValue] | None = None
    details: dict[str, JSONValue] | None = None
    error: str | None = None


@dataclass(frozen=True, slots=True)
class AgentTool:
    """This is the type of a tool that can be created"""

    name: str
    description: str
    input_schema: Mapping[str, JSONValue]
    executor: ToolExecutor
    prompt_snippet: str | None = None
    prompt_guidelines: tuple[str, ...] = ()

    async def execute(
        self,
        arguments: Mapping[str, JSONValue],
        signal: ToolCancellationToken | None = None,
    ):
        """Execute the tool with JSON like arguments"""
        return await self.executor(arguments, signal=signal)
