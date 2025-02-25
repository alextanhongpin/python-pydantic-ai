from dataclasses import dataclass
from llm import ollama_model
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext, ModelRetry


@dataclass
class DatabaseConn:
    users: dict[int, str]


class ChatResult(BaseModel):
    user_id: int
    message: str


agent = Agent(ollama_model, deps_type=DatabaseConn, result_type=ChatResult, retries=3)


@agent.tool(retries=3)
def get_user_id_by_name(ctx: RunContext[DatabaseConn], name: str) -> int:
    """Get a user's ID from their full name"""
    for user_id, user_name in ctx.deps.users.items():
        if user_name == name:
            return user_id
    raise ModelRetry(f"No user found with the name {name}")


result = agent.run_sync(
    "Send a message to Alice asking for coffee next week",
    deps=DatabaseConn(users={1: "Alice"}),
)
print(result.data)
