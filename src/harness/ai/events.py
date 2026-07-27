from __future__ import annotations

from typing import Literal

from harness.agent.base import WireModel
from harness.agent.messages import AssistantMessage
from harness.agent.tools import ToolCall


class ProviderResponseStartEvent(WireModel):
    type: Literal["response_start"] = "response_start"
    model: str


class ProviderResponseEndEvent(WireModel):
    type: Literal["response_end"] = "response_end"
    message: AssistantMessage


class ProviderTextDeltaEvent(WireModel):
    type: Literal["text_delta"] = "text_delta"
    delta: str


class ProviderToolCallEvent(WireModel):
    type: Literal["tool_call"] = "tool_call"
    tool_call: ToolCall


class ProviderErrorEvent(WireModel):
    type: Literal["error"] = "error"
    error: str


ProviderEvent = (
    ProviderResponseStartEvent
    | ProviderResponseEndEvent
    | ProviderTextDeltaEvent
    | ProviderToolCallEvent
)
