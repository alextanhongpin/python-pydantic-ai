import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from pydantic import BaseModel
from pydantic_ai import Agent, ModelRetry, RunContext

from llm import ollama_agent


class DatabaseConn:
    async def execute(self, query: str):
        print("Executing:", query)


class Success(BaseModel):
    sql_query: str


class InvalidRequest(BaseModel):
    error_message: str


Response = Success | InvalidRequest

agent: Agent[DatabaseConn, Response] = ollama_agent(
    result_type=Response,
    deps_type=DatabaseConn,
    system_prompt=("Generate PostgreSQL flavored SQL queries based on user input."),
)


@agent.result_validator
async def validate_result(ctx: RunContext[DatabaseConn], result: Response) -> Response:
    if isinstance(result, InvalidRequest):
        return result
    try:
        await ctx.deps.execute(f"EXPLAIN {result.sql_query}")
    except Exception as e:
        raise ModelRetry(f"Invalid query: {e}") from e
    else:
        return result


result = agent.run_sync(
    "get me users who were last active yesterday", deps=DatabaseConn()
)
print(result.data)
# > sql_query='SELECT user_id FROM activity_log WHERE timestamp >= NOW() - INTERVAL 1 DAY'
