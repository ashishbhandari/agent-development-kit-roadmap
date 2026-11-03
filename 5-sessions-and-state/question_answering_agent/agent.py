from google.adk.agents.llm_agent import Agent

question_answering_agent = Agent(
    model='gemini-3.5-flash',
    name='question_answering_agent',
    description='A helpful assistant for user questions.',
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)
