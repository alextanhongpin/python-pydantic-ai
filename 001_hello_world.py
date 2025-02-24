from pydantic_ai import Agent
from llm import ollama_model

agent = Agent(ollama_model, system_prompt='Be concise, reply with one sentence.')

question = "explain bayesian optimization in laymens term"
result = agent.run_sync(question)
answer = result.data

print(f"Q: {question}")
print(f"A: {answer}")
