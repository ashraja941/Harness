from __future__ import annotations

from typing import Protocol
from collections.abc import AsyncIterator

from harness.agent.messages import AgentMessage
from harness.agent.tools import AgentTool, ToolCall
from harness.ai.events import ProviderEvent


class ModelProvider(Protocol):
    """
    Provider Neutral interface to get streaming outputs
    """

    def stream_response(
        self,
        *,
        model: str,
        system: str,
        messages: list[AgentMessage],
        tools: list[AgentTool],
        signal: bool | None,
    ) -> AsyncIterator[ProviderEvent]:
        """Stream a models response in the form of a provider event"""
        ...
