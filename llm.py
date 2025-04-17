from pydantic_ai import Agent
from pydantic_ai.models.instrumented import InstrumentationSettings, InstrumentedModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

instrumentation_settings = InstrumentationSettings(event_mode="logs")

Agent.instrument_all(instrumentation_settings)

# ollama serve llama3.1
ollama_model = OpenAIModel(
    "llama3.2",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
)


gemma_model = OpenAIModel(
    model_name="gemma3:1b",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
)

deepseek_model = OpenAIModel(
    model_name="deepseek-r1:8b",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
)

phi4_mini_model = OpenAIModel(
    model_name="phi4-mini",
    provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
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


def separator(text: str):
    padding = (80 - len(text) - 2) // 2
    left_padding = "-" * padding
    right_padding = "-" * (padding - len(text) - 2)

    print(f"\n{left_padding} {text} {right_padding}\n")
