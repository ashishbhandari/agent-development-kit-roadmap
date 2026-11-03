
from google.adk.tools.tool_context import ToolContext
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """Retrieves a nerdy joke about the specified topic."""
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    jokes = {
        "python": "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "javascript": "Why did the JavaScript developer go broke? Because he kept using 'var' instead of 'let'!",
        "java": "Why do Java developers wear glasses? Because they don't C#!",
        "programming": "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
        "math": "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else.",
        "physics": "Why can't you trust an atom? Because they make up everything!",
        "chemistry": "What do you do with a sick chemist? If you can't helium, and you can't curium, then you might as well barium.",
        "biology": "Why did the biologist go on a date with a microscope? He wanted to find a closer connection.",
        "default": "Why did the computer go to the doctor? Because it had a virus!",
    }

    joke = jokes.get(topic.lower(), jokes["default"])
    
    # Update state with the last joke topic
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}

    

funny_nerd = Agent(
    # model='gemini-3.5-flash',
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    name='funny_nerd',
    description='A funny nerd agent that provides humorous and nerdy responses to user queries',
    instruction="""
    You are a funny nerd agent that tells nerdy jokes about various topics.
    
    When asked to tell a joke:
    1. Use the get_nerd_joke tool to fetch a joke about the requested topic
    2. If no specific topic is mentioned, ask the user what kind of nerdy joke they'd like to hear
    3. Format the response to include both the joke and a brief explanation if needed
    
    Available topics include:
    - python
    - javascript
    - java
    - programming
    - math
    - physics
    - chemistry
    - biology
    
    Example response format:
    "Here's a nerdy joke about <TOPIC>:
    <JOKE>
    
    Explanation: {brief explanation if needed}"

    If the user asks about anything else, 
    you should delegate the task to the manager agent.
    """,
    tools=[get_nerd_joke],
)
