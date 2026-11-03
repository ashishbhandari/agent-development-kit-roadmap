import asyncio


class SessionService:

    def __init__(self):
        self.sessions = {}

    async def create_session(self, session_id, initial_state):
        print("Creating session...")
        # simulates an asynchronous operation that takes one second. It represents waiting for something like a database or network service.
        await asyncio.sleep(1)
        
        # Create an entry in the sessions dictionary using session_id as the key, and store a copy of initial_state as its value.
        self.sessions[session_id] = initial_state.copy()

        print("Session created!")
        return self.sessions[session_id]

    async def get_session(self, session_id):
        print("Retrieving session...")
        # simulates an asynchronous operation that takes one second. It represents waiting for something like a database or network service.
        await asyncio.sleep(1)
        return self.sessions.get(session_id)