import os.path
import pprint
import random
import sys

from pydantic_ai import RunContext

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent, separator

agent = ollama_agent(
    deps_type=str,
    system_prompt=(
        """You're a dice game, you should roll the die and see if the number you get matches the user's guess. If so, tell them they're a winner. Use the player's name in the response."""
    ),
)


@agent.tool_plain
def roll_die() -> str:
    """Roll a six-sided die and return the result."""
    return str(random.randint(1, 6))


@agent.tool
def get_player_name(ctx: RunContext[str]) -> str:
    """Get the player's name."""
    return ctx.deps


dice_result = agent.run_sync("My guess is 4", deps="Anne")

separator("Result")
print(dice_result.output)

separator("Messages")
pprint.pp(dice_result.all_messages())
