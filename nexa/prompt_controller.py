class PromptController:
    def __init__(self, role):
        self.role = role

    def build(self, context, user_input):
        return f"""
You are NEXA, acting as a {self.role}.
Conversation so far:
{context}

User: {user_input}
NEXA:
"""
