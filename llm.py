from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# ollama serve llama3.1
ollama_model = OpenAIModel(
    model_name="llama3.2", base_url="http://localhost:11434/v1", api_key="test-api-key"
)


def ollama_agent(**kwargs) -> Agent:
    return Agent(ollama_model, **kwargs)

# Usage:
# from pydantic_ai import Agent
# agent = Agent(
# ollama_model,
# system_prompt='Be concise, reply with one sentence.',
# )
