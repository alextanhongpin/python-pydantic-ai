import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from pydantic_ai import Agent

from llm import ollama_agent

agent: Agent[None, list[str] | list[int]] = ollama_agent(
    result_type=list[str] | list[int],
    system_prompt=("Extract either colors or sizes from the shapes provided",),
)

result = agent.run_sync("red square, blue circle, green triangle")
print(result.data)
# > ['red', 'blue', 'green']

result = agent.run_sync("square size 10, circle size 20, triangle size 30")
print(result.data)
# > [10, 20, 30]
