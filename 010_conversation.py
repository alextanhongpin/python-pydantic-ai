from pydantic_ai import Agent

from llm import ollama_model

agent = Agent(ollama_model)


# First run.
result1 = agent.run_sync("Who was Albert Einstein?")
print(result1.data)


# Second run, passing previous message.
result2 = agent.run_sync(
    "What was his most famous equation?", message_history=result1.new_messages()
)
print(result2.data)
