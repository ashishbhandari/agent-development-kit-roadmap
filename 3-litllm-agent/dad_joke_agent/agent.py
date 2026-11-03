import random

from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

def get_dad_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the bicycle fall over? Because it was two-tired!",     
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the math book look sad? Because it had too many problems!",
        "Why did the coffee file a police report? It got mugged!",
    ]
    return random.choice(jokes)

root_agent = Agent(
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    name='dad_joke_agent',
    description='Dad Joke Agent',
    instruction='A helpful assistant that tells dad jokes to user questions. please only use the tool get_dad_joke to answer user questions. If the user asks for a dad joke, use the tool to get a dad joke and return it to the user. If the user asks for anything else, tell them that you can only tell dad jokes.',
    tools=[get_dad_joke]
)
