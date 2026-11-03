from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. Should be concise and informative.")
    body: str = Field(description="The main content of the email. Should be well-structured with proper greetings, paaragraphs, and a closing statement.")


root_agent = Agent(
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),
    name='email_agent',
    description='Generate professional emails based on users input.',
    instruction='You are an email assistant. You will receive a prompt from the user and generate a professional email based on that prompt. ' \
    'The email should be well-structured, with a clear subject line, proper greetings, paragraphs, and a closing statement. ' \
    'Ensure that the tone is appropriate for professional communication.' \
    'IMportant: The output should be in JSON format with the following structure: ' \
    '{"subject": "Email Subject", "body": "Email Body with proper formatting and structure."}' \
    'Do mnot include any additional text or explanations outside of the JSON structure.',
    output_schema=EmailContent, # Enforce JSON output
    output_key="email_content"  # Store result in state['email_content']
)
