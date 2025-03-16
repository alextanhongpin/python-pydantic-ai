import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent

agent = ollama_agent(system_prompt="Be a helpful assistant.")


async def main():
    async with agent.run_stream("Tell me a joke.") as result:
        # Incomplete messages before the stream finishes.
        print(result.all_messages())

        async for text in result.stream_text():
            print(text)

        # Complete messages once the stream finishes.
        print(result.all_messages())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
