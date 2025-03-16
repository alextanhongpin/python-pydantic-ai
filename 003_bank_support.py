from dataclasses import dataclass
from typing import Mapping, Union

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

from llm import ollama_model


@dataclass
class SupportDependencies:
    customer_id: int
    db: Mapping[int, Mapping[str, Union[str, int]]]  # name by customer id mapping.


class SupportResult(BaseModel):
    support_advice: str = Field(description="Advice returned to customer")
    block_card: bool = Field(description="Whether to block the card or not")
    risk: int = Field(description="Risk level of the query", ge=0, le=10)


support_agent = Agent(
    ollama_model,
    deps_type=SupportDependencies,
    result_type=SupportResult,
    system_prompt=(
        "You are a support agent in our bank, give the ",
        "customer support and judge the risk level of their query.",
    ),
)

db = {
    1: {"name": "Alice", "balance": -100.0},
}


@support_agent.system_prompt
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    """Returns the customer's name."""
    customer_name = ctx.deps.db[ctx.deps.customer_id]["name"]
    return f"The customer's name is {customer_name}"


@support_agent.tool
async def customer_balance(
    ctx: RunContext[SupportDependencies], include_pending: bool
) -> float:
    """Returns the customer's current account balance."""
    return ctx.deps.db[ctx.deps.customer_id]["balance"]


async def main():
    deps = SupportDependencies(customer_id=1, db=db)
    result = await support_agent.run("What is my balance?", deps=deps)
    print(result.data)

    # deps = SupportDependencies(customer_id=2, db=db)
    result = await support_agent.run("I just lost my card!", deps=deps)
    print(result.data)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
