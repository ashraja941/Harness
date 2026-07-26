from typing import Literal
from pydantic import BaseModel, ConfigDict

from harness.agent.messages import AgentMessage, AssistantMessage, WireModel
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


ProviderEvent = (
    ProviderResponseStartEvent
    | ProviderResponseEndEvent
    | ProviderTextDeltaEvent
    | ProviderToolCallEvent
)
