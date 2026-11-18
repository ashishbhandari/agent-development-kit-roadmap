from google.adk import Agent
from google.adk import Workflow
from google.adk import Event
from pydantic import BaseModel

city_generator_agent = Agent(
    model='gemini-3.5-flash',
    name='city_generator_agent',
    instruction="""Return the name of a random city.
      Return only the name, nothing else.""",
)

class CityTime(BaseModel):
    time_info:str
    city_name:str


def lookup_time_function(node_input: str):
    """Simulate returning the current time in the specified city."""
    return CityTime(time_info="10:10 AM", city_name=node_input)

city_report_agent = Agent(
    name="city_report_agent",
    model='gemini-3.5-flash',
    input_schema=CityTime,
    instruction="""You receive a CityTime with time_info and city fields.
    Output a single line stating that it is that time in that city right
    now.""",
)

def completed_message_function(node_input: str):
    return Event(
        message=f"{node_input}\n WORKFLOW COMPLETED.",
    )

root_agent = Workflow(
    name="root_agent",
    edges=[
        ("START", city_generator_agent, lookup_time_function,
          city_report_agent, completed_message_function)
    ],
)
