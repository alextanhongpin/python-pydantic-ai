# This example demonstrates how the function parameters are extracted from docstrings.
# Pydanctic uses griffe to extract docstrings, which supports multiple types: google, numpy and sphinx.


import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import pprint

from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import AgentInfo, FunctionModel

from llm import ollama_agent

agent = ollama_agent()


@agent.tool_plain(docstring_format="google", require_parameter_descriptions=True)
def foobar(a: int, b: str, c: dict[str, list[float]]) -> str:
    """Get me foobar.

    Args:
        a: apple pie
        b: banana cake
        c: carrot smoothie
    """
    return f"{a} {b} {c}"


def print_schema(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
    tool = info.function_tools[0]
    print(tool.description)
    # > Get me foobar.

    pprint.pp(tool.parameters_json_schema)
    """
{'properties': {'a': {'description': 'apple pie',
                      'title': 'A',
                      'type': 'integer'},
                'b': {'description': 'banana cake',
                      'title': 'B',
                      'type': 'string'},
                'c': {'additionalProperties': {'items': {'type': 'number'},
                                               'type': 'array'},
                      'description': 'carrot smoothie',
                      'title': 'C',
                      'type': 'object'}},
 'required': ['a', 'b', 'c'],
 'type': 'object',
 'additionalProperties': False}
    """

    return ModelResponse(parts=[TextPart("foobar")])


agent.run_sync("hello", model=FunctionModel(print_schema))
