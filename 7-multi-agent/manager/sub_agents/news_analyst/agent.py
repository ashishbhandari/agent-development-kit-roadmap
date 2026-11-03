
import os

from google.adk.agents import Agent
from tavily import TavilyClient
from google.adk.models.lite_llm import LiteLlm
from tools.tools import get_current_time

def search_news(query: str) -> dict:
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise RuntimeError("TAVILY_API_KEY is not set")

    response = TavilyClient(api_key=api_key).search(
        query=query,
        topic="news",
        max_results=5,
    )
    return {
        "results": [
            {
                "title": item.get("title"),
                "url": item.get("url"),
                "content": item.get("content"),
                "published_date": item.get("published_date"),
            }
            for item in response.get("results", [])
        ]
    }


news_analyst = Agent(
    # model='gemini-3.5-flash',     
    model=LiteLlm(model="chatgpt/gpt-6.1-sol"),  
    name='news_analyst',
    description="A news analyst that searches for and summarizes current news.",
    instruction="""
    For news requests, call search_news and summarize the returned results.
    For relative dates such as "today" or "last week", call get_current_time
    and use it to clarify the search query.
    """,
    tools=[search_news, get_current_time],
)
