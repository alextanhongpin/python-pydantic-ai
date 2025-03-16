from pydantic_ai import Agent

from llm import ollama_model

agent = Agent(ollama_model)

result_sync = agent.run_sync("What is the capital of Singapore?")
print(result_sync.data)
# > The capital of Singapore is Singapore itself, as it is a city-state. There is no separate administrative capital in Singapore.


async def main():
    result = await agent.run("What is the capital of Malaysia?")
    print(result.data)
    # > The capital of Malaysia is Kuala Lumpur.

    async with agent.run_stream("What is the capital of the UK?") as response:
        print(await response.get_data())
        """
        The United Kingdom is made up of four countries: England, Scotland, Wales, and Northern Ireland.

        Each country has its own capital:

        - The capital of England is London.
        - The capital of Scotland is Edinburgh.
        - The capital of Wales is Cardiff.
        - The capital of Northern Ireland is Belfast.

        So, the UK does not have a single capital.
        """


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
