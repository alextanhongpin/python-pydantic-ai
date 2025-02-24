run:
	uv run $(name)


install:
	curl -LsSf https://astral.sh/uv/install.sh | sh


init:
	uv init


lint:
	@#uvx black .
	uv run black .
