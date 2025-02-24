from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


class CityLocation(BaseModel):
    city: str
    country: str


# ollama serve llama3.1
ollama_model = OpenAIModel(model_name="llama3.1", base_url="http://localhost:11434/v1", api_key='test-api-key')
agent = Agent(ollama_model, result_type=CityLocation)

result = agent.run_sync("Where were the olympics held in 2012?")
print(result.data)
# > city='London' country='United Kingdom'
print(result.usage())
"""
Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
"""
