from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

from llm import ollama_model

agent = Agent(ollama_model)

result_sync = agent.run_sync(
    "What is the capital of Italy? Answer with just the city.",
    usage_limits=UsageLimits(response_tokens_limit=10),
)
print(result_sync.data)
# > Rome

print(result_sync.usage())
# > Usage(requests=1, request_tokens=38, response_tokens=3, total_tokens=41, details=None)


try:
    result_sync = agent.run_sync(
        "What is the capital of Singapore? Answer with a paragraph",
        usage_limits=UsageLimits(response_tokens_limit=10),
    )
except UsageLimitExceeded as e:
    print(e)
    # > Exceeded the response_tokens_limit of 10 (response_tokens=131)
