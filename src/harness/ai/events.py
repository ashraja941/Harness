from typing import Literal
from pydantic import BaseModel, ConfigDict


class ProviderResponseStartEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["response_start"] = "response_start"
    model: str


class ProviderResponseEndEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["response_end"] = "response_end"
    message: str  # TODO: Change to Agent specific type


class ProviderTextDeltaEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["text_delta"] = "text_delta"
    delta: str


class ProviderToolCallEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["tool_call"] = "tool_call"
    tool_call: str  # TODO: Change to Agent specific type


ProviderEvent = (
    ProviderResponseStartEvent
    | ProviderResponseEndEvent
    | ProviderTextDeltaEvent
    | ProviderToolCallEvent
)
