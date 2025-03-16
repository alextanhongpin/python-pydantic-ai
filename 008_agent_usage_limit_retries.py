from typing import TypedDict

from pydantic_ai import Agent, ModelRetry
from pydantic_ai.exceptions import UsageLimitExceeded
from pydantic_ai.usage import UsageLimits

from llm import ollama_model


class NeverResultType(TypedDict):
    """Never ever coerce data to this type"""

    never_use_this: str


agent = Agent(
    ollama_model,
    retries=3,
    result_type=NeverResultType,
    system_prompt="Any time you get a response, call the `infinite_retry_tool` to produce another response",
)


@agent.tool_plain(retries=4)
def infinite_retry_tool() -> int:
    raise ModelRetry("Please try again.")


try:
    result_sync = agent.run_sync(
        "Begin infinite retry loop!", usage_limits=UsageLimits(request_limit=3)
    )
except UsageLimitExceeded as e:
    print(e)
    # > The next request would exceed the request_limit of 3
