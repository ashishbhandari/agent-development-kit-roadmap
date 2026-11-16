from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


root_agent = Agent(
    name='greeting_agent',
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    description="Greeting Agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)