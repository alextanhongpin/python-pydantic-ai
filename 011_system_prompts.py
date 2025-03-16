from datetime import date

from pydantic_ai import Agent, RunContext

from llm import ollama_model

agent = Agent(
    ollama_model,
    deps_type=str,
    system_prompt="User the customer's name while replying to them.",
)


@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


@agent.system_prompt
def add_date() -> str:
    return f"The date today is {date.today()}."


result = agent.run_sync("What is the date?", deps="John")
print(result.data)
"""
Hello John,

Today's date is Monday, February 25th, 2025.
"""
