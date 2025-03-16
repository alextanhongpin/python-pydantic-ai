from pydantic_ai import Agent

from llm import ollama_model

agent = Agent(ollama_model)


async def main():
    nodes = []
    print(dir(agent))
    # Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph.
    with agent.iter("What is the capital of France?") as agent_run:
        async for node in agent_run:
            # Each node represent a step in the agent's execution.
            nodes.append(node)
            print(node.data)
            # >
    print(nodes)
    print(agent_run.result.data)
    # >

    # Accessing usage and the final result.
    print(agent_run.usage())
    """"""

    print(agent_run.final_result)
    """"""


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
