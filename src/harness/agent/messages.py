from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, ConfigDict
from harness.agent.types import JSONValue


class HumanMessage(BaseModel):
    """Message that has been sent by the user"""

    model_config = ConfigDict(extra="forbid")

    role: Literal["user"] = "user"
    content: str


class AssistantMessage(BaseModel):
    """Message that has been sent by the AI assitant, with possible tool calls"""

    model_config = ConfigDict(extra="forbid")

    role: Literal["assistant"] = "assistant"
    tool_calls: list[dict[str, Any]]  # TODO: Change to tool call type
    content: str


class ToolResultMessage(BaseModel):
    """Contains information about the last tool call"""

    model_config = ConfigDict(extra="forbid")

    role: Literal["tool"] = "tool"
    tool_call_id: str
    name: str
    content: str
    ok: bool = True
    data: dict[str, JSONValue] | None = None
    details: dict[str, JSONValue] | None = None
    error: str | None = None


type AgentMessage = HumanMessage | AssistantMessage | ToolResultMessage
