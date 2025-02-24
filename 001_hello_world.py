from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# ollama serve llama3.1
ollama_model = OpenAIModel(model_name="llama3.1", base_url="http://localhost:11434/v1", api_key='test-api-key')
agent = Agent(  
    ollama_model,
    system_prompt='Be concise, reply with one sentence.',  
)

result = agent.run_sync('explain bayesian optimization in laymens term')  
print(result.data)
