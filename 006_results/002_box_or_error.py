import os
import sys

from pydantic import BaseModel
from pydantic_ai import Agent

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent


class Box(BaseModel):
    width: int
    height: int
    depth: int
    units: str


agent: Agent[None, Box | str] = ollama_agent(
    result_type=Box | str,
    system_prompt=(
        "Extract me the dimensions of the box, ",
        "if you can't extract all data, ask the user to try again.",
    ),
)

result = agent.run_sync("The box is 10x20x30")
print(result.data)
# > Please provide the units for the dimensions (e.g., cm, in, m).


result = agent.run_sync("The box is 10x20x30 cm")
print(result.data)
# > width=10 height=20 depth=30 units='cm'
