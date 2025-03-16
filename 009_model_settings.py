from pydantic_ai import Agent

from llm import ollama_model

agent = Agent(ollama_model)

result_sync = agent.run_sync(
    "Poem about Singapore", model_settings={"temperature": 0.0}
)
print(result_sync.data)

print("###")

result_sync = agent.run_sync(
    "Poem about Singapore", model_settings={"temperature": 1.0}
)
print(result_sync.data)
