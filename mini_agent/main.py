import asyncio
import uuid

from session_service import SessionService
from agent import TVAgent
from runner import Runner


async def main() -> None:

    # Step 1: Create Session Service
    session_service = SessionService()

    # Step 2: Generate Session ID
    session_id = str(uuid.uuid4())

    # Step 3: Define initial state
    initial_state = {
        "user_name": "Ashish",
        "favorite_tv_show": "Friends"
    }

    # Step 4: Create session
    await session_service.create_session(
        session_id,
        initial_state
    )

    # Step 5: Create agent
    agent = TVAgent(name="My TV Assistant")

    # Step 6: Create runner
    runner = Runner(
        agent=agent,
        session_service=session_service
    )

    # Step 7: Ask a question
    question = "What is my favorite TV show?"

    # Step 8: Run the agent
    async for event in runner.run_async(
        session_id,
        question
    ):
        if event["type"] == "final_response":
            print("Agent:", event["text"])

    # Step 9: Retrieve the session
    session = await session_service.get_session(session_id)

    # Step 10: Print session state
    print("=== Final Session State ===")

    for key, value in session.items():
        print(f"{key}: {value}")

    print("Main function completed!")


if __name__ == "__main__":
    asyncio.run(main())
