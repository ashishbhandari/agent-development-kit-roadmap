import asyncio
import uuid
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

from dotenv import load_dotenv


load_dotenv()

session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Ashish Bhandari",
    "user_preferences": """
        I like to play Cricket, Swimming, and Tennis.
        My favorite food is Chicken Curry.
        My favorite TV show is Reacher.
        Loves it when people like and subscribe to his YouTube channel.
    """,
}

APP_NAME = "Ashb AI Bot"
USER_ID = "ashb_with_ai"


async def main() -> None:
    session_id = str(uuid.uuid4())
    await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
        state=initial_state,
    )
    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {session_id}")

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )
    
    # Creates a structured message object
    new_message = types.Content(
        role="user", parts=[types.Part(text="What is Ashish favorite TV show?")]
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=new_message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

    print("==== Session Event Exploration ====")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=session_id
    )
    if session is None:
        raise RuntimeError(f"Session {session_id} was not found after the run.")

    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
