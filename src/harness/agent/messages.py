from __future__ import annotations

from typing import Literal
from pydantic import Field
from harness.agent.base import WireModel
from harness.agent.tools import ToolCall
from harness.agent.types import JSONValue


class HumanMessage(WireModel):
    """Message that has been sent by the user"""

    role: Literal["user"] = "user"
    content: str


class AssistantMessage(WireModel):
    """Message that has been sent by the AI assitant, with possible tool calls"""

    role: Literal["assistant"] = "assistant"
    tool_calls: list[ToolCall] = Field(default_factory=list)
    content: str = ""


class ToolResultMessage(WireModel):
    """Contains information about the last tool call"""

    role: Literal["tool"] = "tool"
    tool_call_id: str
    name: str
    content: str
    ok: bool = True
    data: dict[str, JSONValue] | None = None
    details: dict[str, JSONValue] | None = None
    error: str | None = None


type AgentMessage = HumanMessage | AssistantMessage | ToolResultMessage
