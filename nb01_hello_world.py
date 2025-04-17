import marimo

__generated_with = "0.12.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Hello World""")
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    # https://ai.pydantic.dev/troubleshooting/
    import nest_asyncio

    nest_asyncio.apply()
    from llm import ollama_agent

    return nest_asyncio, ollama_agent


@app.cell
def _(ollama_agent):
    agent = ollama_agent()
    return (agent,)


@app.cell
def _(mo):
    input = mo.ui.text_area(
        'Where does "hello world" comes from?', label="Enter question"
    )
    input
    return (input,)


@app.cell
def _(agent, input, mo):
    result = agent.run_sync(input.value)
    mo.md(result.output)
    return (result,)


if __name__ == "__main__":
    app.run()
