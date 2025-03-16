import os.path
import sys

from pydantic import BaseModel

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from llm import ollama_agent


class CityLocation(BaseModel):
    city: str
    country: str


agent = ollama_agent(result_type=CityLocation)
result = agent.run_sync("Where were the Olympics held in 2012?")
print(result.data)
# > city='London' country='United Kingdom'

print(result.usage())
# > Usage(requests=1, request_tokens=174, response_tokens=24, total_tokens=198, details=None)
