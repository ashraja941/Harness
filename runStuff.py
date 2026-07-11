from src.harness.llm.providers.openai import ChatOpenAI
import asyncio
from dotenv import load_dotenv


async def main():
    _ = load_dotenv()
    llm = ChatOpenAI()
    print(await llm.test())


asyncio.run(main())
