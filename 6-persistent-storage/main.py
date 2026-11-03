import asyncio

from dotenv import load_dotenv
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

# ===== PART 1: Initialize Persistent Session Service =====
# Using SQLite database for persistent storage
# db_url = "sqlite:///./session_storage.db"
db_url = "sqlite+aiosqlite:///./session_storage.db"
session_service_persistent = DatabaseSessionService(db_url=db_url)


# Define Intial State

initial_state = {
    "user_name": "Ashish Bhandari",
    "reminders": []
}

async def main_async():
    APP_NAME = "Ashb AI Bot"
    USER_ID = "ashb_with_ai"

    # begin the process of Existing session and 
    existing_sessions = await session_service_persistent.list_sessions(
        app_name=APP_NAME, 
        user_id=USER_ID,
        )
    

    if existing_sessions.sessions:
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Existing session found. Session ID: {SESSION_ID}")
    else:
        new_session = await session_service_persistent.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created New Session: {SESSION_ID}")


    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service_persistent,
    )   


      # ===== PART 5: Interactive Conversation Loop =====
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the conversation. Your data has been saved to the database. Goodbye!")
            break

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


if __name__ == "__main__":
    asyncio.run(main_async())
