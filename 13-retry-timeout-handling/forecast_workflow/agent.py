from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='forecast_workflow',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
