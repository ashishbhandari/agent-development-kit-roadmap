class TVAgent:
    def __init__(self, name):
        self.name = name

    def answer(self, question, state):
        print(f"{self.name} is thinking...")

        if "favorite TV show" in question.lower():
            show = state.get("favorite_tv_show", "Unknown")
            return f"Your favorite TV show is {show}."

        return "Sorry, I don't know the answer."   