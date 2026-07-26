from __future__ import annotations

from time import time
from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field
from harness.agent.tools import ToolCall
from harness.agent.types import JSONValue


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(part.title() for part in parts[1:])


def current_timestamp_ms() -> int:
    """Return the current Unix timestamp in milliseconds."""
    return int(time() * 1000)


class WireModel(BaseModel):
    """harness specific Basemodel with strict validaions"""

    model_config = ConfigDict(
        extra="forbid",
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
        alias_generator=_to_camel,
    )


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
