from typing import Protocol


class ModelProvider(Protocol):
    """
    Provider Neutral interface to get streaming outputs
    """

    # TODO:: Change types to Agent specific types
    def stream_response(
        self,
        *,
        model: str,
        system: str,
        messages: list[str],
        tools: list[str],
        signal: bool | None,
    ): ...
