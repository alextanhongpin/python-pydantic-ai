# This example demonstrates how validation works with streamed text.

import os
import sys
from datetime import date

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from typing_extensions import TypedDict

from llm import ollama_agent


class UserProfile(TypedDict, total=False):
    name: str
    dob: date
    bio: str


agent = ollama_agent(
    result_type=UserProfile,
    system_prompt="Extract a user profile from the input",
)


async def main():
    user_input = "My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid."
    async with agent.run_stream(user_input) as result:
        async for profile in result.stream():
            print(profile)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
