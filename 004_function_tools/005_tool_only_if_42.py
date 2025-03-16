# Using "prepare" to handle dynamic tool.
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from typing import Union

from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import ToolDefinition

agent = Agent("test")


async def only_if_42(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    if ctx.deps == 42:
        return tool_def


@agent.tool(prepare=only_if_42)
def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f"{ctx.deps} {answer}"


result = agent.run_sync("testing...", deps=41)
print(result.data)
# > success (no tool calls)

result = agent.run_sync("testing...", deps=42)
print(result.data)
# > {"hitchhiker":"42 a"}
