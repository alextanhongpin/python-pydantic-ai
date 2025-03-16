import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent

agent = ollama_agent()


async def main():
    async with agent.run_stream('where does "hello world" comes from?') as result:
        async for message in result.stream_text():
            print(message)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
