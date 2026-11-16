# Core logic for creatign our session, runner and handling suer queries.

import asyncio

from customer_service_agent.agent import customer_service_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from dotenv import load_dotenv

from utils import add_user_query_to_history, call_agent_async


load_dotenv()

# ===== PART 1: Initialize In-Memory Session Service =====
# Using in-memory storage for this example (non-persistent)
# Creates an ADK session service that stores sessions in RAM. This creates a session manager, but it does not create a conversation session yet. When the application stops or restarts, the sessions are lost.
session_service_stateful = InMemorySessionService()

# ===== PART 2: Define Initial State =====
# session service keeps the conversation history, and the Runner uses that history for subsequent agent turns.
initial_state = {
    "user_name": "Ashish Bhandari", 
    "purchased_coursees": [],
    "ineraction_history": [],
}

async def main_async():
    APP_NAME = "Customer Support"
    USER_ID = "ashb_with_ai"

     # ===== PART 3: Session Creation =====
    # create a new session with the initial state
    new_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )

    SESSION_ID = new_session.session_id
    print(f"Created new session with ID: {SESSION_ID}")

    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the main customer service agent
    runner = Runner(
        agent=customer_service_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    # ===== PART 5: Interactive Conversation Loop =====
    print("\nWelcome to Customer Service Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")


    while True:
        # Get user input
        user_input = input("You: ")
        
        # check if the user wants to exit the conversation 
        if user_input.lower() in ["exit", "quit"]:
            print("Ending the conversation. Goodbye!")
            break


        
        # Update interaction history with the user's query
        add_user_query_to_history(
            session_service_stateful, APP_NAME, USER_ID, SESSION_ID, user_input
        )
        
        # Process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

    # ===== PART 6: State Examination =====
    # Show final session state
    final_session = session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")


def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
