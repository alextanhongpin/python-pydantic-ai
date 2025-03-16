import os.path
import random
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from pydantic_ai import RunContext, Tool

from llm import ollama_agent


def roll_die() -> str:
    """Roll a six-sided die and return the result."""
    return str(random.randint(1, 6))


def get_player_name(ctx: RunContext[str]) -> str:
    """Get the player's name."""
    return ctx.deps


agent_a = ollama_agent(deps_type=str, tools=[roll_die, get_player_name])
agent_b = ollama_agent(
    deps_type=str,
    tools=[Tool(roll_die, takes_ctx=False), Tool(get_player_name, takes_ctx=True)],
)

dice_result = agent_b.run_sync("My guess is 4", deps="Anne")
print(dice_result.data)
