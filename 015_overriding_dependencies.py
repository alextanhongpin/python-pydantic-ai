from dataclasses import dataclass

from pydantic_ai import RunContext

from llm import ollama_agent


@dataclass
class MyDeps:
    prompt: str


joke_agent = ollama_agent()


@joke_agent.system_prompt
def my_system_prompt(ctx: RunContext[MyDeps]) -> str:
    return f"{ctx.deps.prompt}"


def application_code(prompt: str):
    deps = MyDeps("The user name is John. Greet the user first.")
    result = joke_agent.run_sync(prompt, deps=deps)
    print(result.data)


application_code("Tell me a joke")
print("###")

with joke_agent.override(deps=MyDeps("The user name is Alice. Greet the user first.")):
    application_code("Tell me a joke")
