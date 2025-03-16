from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# ollama serve llama3.1
ollama_model = OpenAIModel(
    model_name="llama3.2", base_url="http://localhost:11434/v1", api_key="test-api-key"
)


gemma_model = OpenAIModel(
    model_name="gemma3:1b", base_url="http://localhost:11434/v1", api_key="test-api-key"
)

deepseek_model = OpenAIModel(
    model_name="deepseek-r1:8b",
    base_url="http://localhost:11434/v1",
    api_key="test-api-key",
)

phi4_mini_model = OpenAIModel(
    model_name="phi4-mini", base_url="http://localhost:11434/v1", api_key="test-api-key"
)


# tool
def ollama_agent(**kwargs) -> Agent:
    return Agent(ollama_model, **kwargs)


# no tool
def gemma_agent(**kwargs) -> Agent:
    return Agent(gemma_model, **kwargs)


# no tool
def deepseek_agent(**kwargs) -> Agent:
    return Agent(deepseek_model, **kwargs)


def phi4_mini_agent(**kwargs) -> Agent:
    return Agent(phi4_mini_model, **kwargs)


# Usage:
# from pydantic_ai import Agent
# agent = Agent(
# ollama_model,
# system_prompt='Be concise, reply with one sentence.',
# )

# To import this from child directory:
# import os.path, sys; sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir));
