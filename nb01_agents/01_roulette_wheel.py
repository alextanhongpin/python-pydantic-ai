import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Agents

        https://ai.pydantic.dev/agents/#introduction
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    import nest_asyncio

    from llm import ollama_agent

    nest_asyncio.apply()
    return mo, nest_asyncio, ollama_agent


@app.cell
def _(mo):
    system_prompt = mo.ui.text_area(
        "Use the `roulette_wheel` function to see if the customer has won based on the number they provide.",
        label="System Prompt",
    )
    system_prompt
    return (system_prompt,)


@app.cell
def _(ollama_agent, system_prompt):
    from pydantic_ai import RunContext

    roulette_agent = ollama_agent(
        retries=3,
        deps_type=int,
        output_type=bool,
        system_prompt=system_prompt.value,
    )

    @roulette_agent.tool
    async def roulette_wheel(ctx: RunContext[int], square: int) -> str:
        """Check if the square is a winner"""
        return "winner" if square == ctx.deps else "loser"

    success_number = 18
    return RunContext, roulette_agent, roulette_wheel, success_number


@app.cell
def _(mo):
    square = mo.ui.dropdown(
        options=["Put my money on square eighteen", "I bet five is the winner"]
    )
    square
    return (square,)


@app.cell
def _(square):
    square.value
    return


@app.cell
def _(mo, roulette_agent, square, success_number):
    mo.stop(not square.value)

    output = ""
    messages = None

    with mo.status.spinner("Running roulette agent ...") as _spinner:
        try:
            result = roulette_agent.run_sync(square.value, deps=success_number)
            output = result.output
            messages = result.all_messages_json()
        except Exception as e:
            output = f"Error: {e}"

    mo.md(output)
    return messages, output, result


@app.cell
def _(messages, mo):
    mo.md(str(messages))
    return


if __name__ == "__main__":
    app.run()
