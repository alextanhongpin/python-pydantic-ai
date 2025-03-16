# Using "prepare" to dynamically modify the tool definition.

from __future__ import annotations

import pprint
from typing import Literal

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.test import TestModel
from pydantic_ai.tools import Tool, ToolDefinition


def greet(name: str) -> str:
    return f"hello {name}"


async def prepare_greet(
    ctx: RunContext[Literal["human", "machine"]], tool_def: ToolDefinition
) -> ToolDefinition | None:
    d = f"Name of the {ctx.deps} to greet."
    tool_def.parameters_json_schema["properties"]["name"]["description"] = d
    return tool_def


# greet_tool = Tool(greet)
greet_tool = Tool(greet, prepare=prepare_greet)
test_model = TestModel()
agent = Agent(test_model, tools=[greet_tool], deps_type=Literal["human", "machine"])

result = agent.run_sync("testing...", deps="human")
print(result.data)
# > {"greet":"hello a"}

pprint.pp(test_model.last_model_request_parameters.function_tools)
"""
[ToolDefinition(name='greet',
                description='',
                parameters_json_schema={'properties': {'name': {'title': 'Name',
                                                                'type': 'string',
                                                                'description': 'Name '
                                                                               'of '
                                                                               'the '
                                                                               'human '
                                                                               'to '
                                                                               'greet.'}},
                                        'required': ['name'],
                                        'type': 'object',
                                        'additionalProperties': False},
                outer_typed_dict_key=None)]
"""
