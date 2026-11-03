
import asyncio


class Runner:

    def __init__(self, agent, session_service):
        self.agent = agent
        self.session_service = session_service

    async def run_async(self, session_id, question):

        print("Runner started")

        session = await self.session_service.get_session(
            session_id
        )

        if session is None:
            raise ValueError("Session not found")

        print("Running agent...")
        await asyncio.sleep(1)

        answer = self.agent.answer(question, session)

        yield {
            "type": "final_response",
            "text": answer
        }

        print("Runner finished")
