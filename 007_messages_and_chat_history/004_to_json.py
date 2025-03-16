import json
import os
import pprint
import sys

from pydantic_ai.messages import ModelMessagesTypeAdapter
from pydantic_core import to_jsonable_python

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent

agent = ollama_agent(system_prompt="Be a helpful assistant.")

result1 = agent.run_sync("Tell me a joke.")
print(result1.data)
history_step_1 = result1.all_messages()
as_python_objects = to_jsonable_python(history_step_1)
print(json.dumps(as_python_objects, indent=2))


same_history_as_step_1 = ModelMessagesTypeAdapter.validate_python(as_python_objects)


result2 = agent.run_sync(
    "Tell me a different joke.", message_history=same_history_as_step_1
)
print(result2.data)
