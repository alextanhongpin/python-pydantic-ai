from pydantic_ai import ModelRetry, UnexpectedModelBehavior, capture_run_messages

from llm import ollama_agent

agent = ollama_agent()


@agent.tool_plain
def calc_volume(size: int) -> int:
    """calculates the volume of a box with a given size"""
    if size == 42:
        return size**3
    raise ModelRetry("Please try again.")


with capture_run_messages() as messages:
    try:
        result = agent.run_sync("Please get me the volume of a box with size 6.")
        print(result.all_messages())
    except UnexpectedModelBehavior as e:
        print("An error occured:", e)
        print("cause:", repr(e.__cause__))
        print("messages:", messages)
    else:
        print(result.data)
