from typing import Literal
from pydantic import BaseModel, ConfigDict

from harness.agent.messages import AgentMessage, AssistantMessage
from harness.agent.tools import ToolCall


class ProviderResponseStartEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["response_start"] = "response_start"
    model: str


class ProviderResponseEndEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["response_end"] = "response_end"
    message: AssistantMessage


class ProviderTextDeltaEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["text_delta"] = "text_delta"
    delta: str


class ProviderToolCallEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["tool_call"] = "tool_call"
    tool_call: ToolCall


ProviderEvent = (
    ProviderResponseStartEvent
    | ProviderResponseEndEvent
    | ProviderTextDeltaEvent
    | ProviderToolCallEvent
)
