from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


root_agent = Agent(
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)