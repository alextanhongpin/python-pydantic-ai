from llm import ollama_agent
from pydantic_ai import RunContext
from dataclasses import dataclass

@dataclass
class MyDeps:
    name: str


agent = ollama_agent(deps_type=MyDeps)

@agent.system_prompt
def my_system_prompt(ctx: RunContext[MyDeps]) -> str:
    return f"The user name is {ctx.deps.name}"

result = agent.run_sync("Hi", deps=MyDeps(name="Alice"))
print(result.data)
print(result.all_messages())
