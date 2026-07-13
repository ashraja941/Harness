import os
from openai import AsyncOpenAI, OpenAIError


class ChatOpenAI:
    def __init__(self) -> None:
        OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise KeyError("Missing the OPENAI_API_KEY")

        self.client: AsyncOpenAI = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def test(self):
        """
        Use this function to check if the openai async responses actually work.

        uses a minimal REAL API call to get this to happen
        """
        response = await self.client.responses.create(
            model="gpt-5.5",
            instructions="You are a helpful assistant",
            input="respond with HI",
        )

        return response.output_text

    async def completeText(self, prompt: str) -> str:
        try:
            response = await self.client.responses.create(
                model="gpt-5.5",
                instructions="You are a helpful coding assistant",
                input=prompt,
            )
            return response.output_text

        except OpenAIError as exc:
            raise RuntimeError(f"OpenAI request failed : {exc}") from exc
