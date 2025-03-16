import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent

agent = ollama_agent(system_prompt="Be a helpful assistant.")

result = agent.run_sync("Tell me a joke.")
print(result.data)

"""
Here's one:

What do you call a fake noodle?

(wait for it...)

An impasta.

I hope that one made you laugh! Do you want to hear another?
"""

print(result.all_messages())
"""
[ModelRequest(parts=[SystemPromptPart(content='Be a helpful assistant.', dynamic_ref=None, part_kind='system-prompt'), UserPromptPart(content='Tell me a joke.', timestamp=datetime.datetime(2025, 3, 16, 13, 18, 13, 989383, tzinfo=datetime.timezone.utc), part_kind='user-prompt')], kind='request'), ModelResponse(parts=[TextPart(content="Here's one:\n\nWhat do you call a fake noodle?\n\n(wait for it...)\n\nAn impasta.\n\nI hope that one made you laugh! Do you want to hear another?", part_kind='text')], model_name='llama3.2', timestamp=datetime.datetime(2025, 3, 16, 13, 18, 14, tzinfo=datetime.timezone.utc), kind='response')]
"""
