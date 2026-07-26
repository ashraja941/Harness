from __future__ import annotations

from typing import Literal

from pydantic import Field

from harness.agent.messages import AgentMessage, AssistantMessage, WireModel
from harness.agent.tools import AgentToolResult
from harness.agent.types import JSONValue

"""


```text
agent_start
turn_start
message_start
message_delta       "I'll inspect the file."
message_end         AssistantMessage(... tool_calls=[read])
tool_execution_start
tool_execution_end  AgentToolResult(...)
turn_end
turn_start
message_start
message_delta       "The README says..."
message_end         AssistantMessage(... no tool calls)
turn_end
agent_end
```

"""


class AgentStartEvent(WireModel):
    type: Literal["agent_start"] = "agent_start"


class AgentEndEvent(WireModel):
    type: Literal["agent_end"] = "agent_end"
    messages: list[AgentMessage] = Field(default_factory=list)


class TurnStartEvent(WireModel):
    type: Literal["turn_start"] = "turn_start"


class TurnEndEvent(WireModel):
    type: Literal["turn_end"] = "turn_end"
    message: AgentMessage
    tool_results: list[AgentToolResult] = Field(default_factory=list)


class MessageStartEvent(WireModel):
    type: Literal["message_start"] = "message_start"
    message: AgentMessage


class MessageUpdateEvent(WireModel):
    type: Literal["message_update"] = "message_update"
    message: AgentMessage
    # TODO : Fix the types
    # assistant_message_event: AssistantMessageEvent = Field(
    #     serialization_alias="assistantMessageEvent"
    # )


class MessageEndEvent(WireModel):
    type: Literal["message_end"] = "message_end"
    message: AgentMessage


class ToolExecutionStartEvent(WireModel):
    type: Literal["tool_execution_start"] = "tool_execution_start"
    tool_call_id: str
    tool_name: str
    args: dict[str, JSONValue] = Field(default_factory=dict)


class ToolExecutionUpdateEvent(WireModel):
    type: Literal["tool_execution_update"] = "tool_execution_update"
    tool_call_id: str
    tool_name: str
    args: dict[str, JSONValue] = Field(default_factory=dict)
    partial_result: AgentToolResult


class ToolExecutionEndEvent(WireModel):
    type: Literal["tool_execution_end"] = "tool_execution_end"
    tool_call_id: str
    tool_name: str
    result: AgentToolResult
    is_error: bool


type AgentEvent = (
    AgentStartEvent
    | AgentEndEvent
    | TurnStartEvent
    | TurnEndEvent
    | MessageStartEvent
    | MessageUpdateEvent
    | MessageEndEvent
    | ToolExecutionStartEvent
    | ToolExecutionUpdateEvent
    | ToolExecutionEndEvent,
)
