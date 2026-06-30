class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_interaction(self, question: str, answer: str, sql: str):
        self.history.append({"question": question, "sql": sql, "answer": answer})

    def get_context(self) -> str:
        if not self.history:
            return "No previous context."
        context = "Recent conversation history:\n"
        for idx, item in enumerate(self.history[-3:]):
            context += f"Q: {item['question']}\nSQL Used: {item['sql']}\nA: {item['answer']}\n"
        return context
