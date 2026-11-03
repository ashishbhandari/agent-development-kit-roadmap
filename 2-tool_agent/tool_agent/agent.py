from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search
from datetime import datetime


def get_current_time() -> dict:
    """Returns the current time as a string in the format YYYY-MM-DD HH:MM:SS."""
    
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    # model='gemini-3.5-flash',
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    name='root_agent',
    description='Tool agent',
    instruction='Youa re a helpful assistant for user questions. You have access to the following tools: google_search, get_current_time. Use them to answer user questions to the best of your knowledge.',
    tools=[get_current_time],
)
