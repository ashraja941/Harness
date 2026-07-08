import os
from openai import AsyncOpenAI


class ChatOpenAI:
    def __init__(self) -> None:
        OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
        if not OPENAI_API_KEY:
            raise KeyError("Missing the OPENAI_API_KEY")

        self.client: AsyncOpenAI = AsyncOpenAI(api_key=OPENAI_API_KEY)

    async def test(self):
        response = await self.client.responses.create(
            model="gpt-5.5",
            instructions="You are a helpful assistant",
            input="respond with HI",
        )

        return response.output_text
