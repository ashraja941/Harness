from dataclasses import dataclass, field
from typing import Any, Literal, TypeAlias

Role: TypeAlias = Literal["system", "user", "assistant", "tool"]


@dataclass(frozen=True)
class TextPart:
    text: str


@dataclass(frozen=True)
class ToolCallPart:
    call_id: str
    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class ToolResultPart:
    call_id: str
    output: str
    is_error: bool = False


MessagePart: TypeAlias = TextPart | ToolCallPart | ToolResultPart


@dataclass(frozen=True)
class Message:
    id: str
    role: Role
    parts: tuple[MessagePart]
    metadata: dict[Any, Any] = field(default_factory=dict)
