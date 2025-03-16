run:
	uv run $(name)


install:
	curl -LsSf https://astral.sh/uv/install.sh | sh


init:
	uv init


lint:
	@uvx ruff format
	@uvx ruff check --fix --select I
	@uv run mypy . # uvx runs in separate virtual environment.
