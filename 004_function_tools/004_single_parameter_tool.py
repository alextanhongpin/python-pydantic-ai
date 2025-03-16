import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import pprint

from pydantic import BaseModel
from pydantic_ai.models.test import TestModel

from llm import ollama_agent

agent = ollama_agent()


class Foobar(BaseModel):
    """This is a Foobar"""

    x: int
    y: str
    z: float = 3.14


@agent.tool_plain
def foobar(f: Foobar) -> str:
    return str(f)


test_model = TestModel()
result = agent.run_sync("hello", model=test_model)
print(result.data)
# > {"foobar":"x=0 y='a' z=3.14"}

pprint.pp(test_model.last_model_request_parameters.function_tools)
"""
[ToolDefinition(name='foobar',
                description='This is a Foobar',
                parameters_json_schema={'properties': {'x': {'title': 'X',
                                                             'type': 'integer'},
                                                       'y': {'title': 'Y',
                                                             'type': 'string'},
                                                       'z': {'default': 3.14,
                                                             'title': 'Z',
                                                             'type': 'number'}},
                                        'required': ['x', 'y'],
                                        'title': 'Foobar',
                                        'type': 'object'},
                outer_typed_dict_key=None)]
"""
