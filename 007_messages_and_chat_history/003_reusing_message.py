import os
import pprint
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent

agent = ollama_agent(system_prompt="Be a helpful assistant.")

result1 = agent.run_sync("Tell me a joke.")
print(result1.data)

result2 = agent.run_sync("explain?", message_history=result1.new_messages())
print(result2.data)

pprint.pp(result2.all_messages())
