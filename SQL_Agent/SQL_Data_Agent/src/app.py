from src.graph import agent_app
from src.memory import ConversationMemory

def main():
    print("Starting Retail SQL Data Analyst Agent...")
    print("Type 'exit' to quit.")
    
    memory = ConversationMemory()
    
    while True:
        question = input("\nAsk a business question: ")
        if question.lower() == 'exit':
            break
            
        initial_state = {
            "question": question,
            "context": memory.get_context(),
            "sql": "",
            "rows": [],
            "answer": "",
            "error": ""
        }
        
        print("Thinking...")
        result = agent_app.invoke(initial_state)
        
        print("\n--- AGENT RESPONSE ---")
        if result.get("error"):
            print(f"[SAFETY/DATA ERROR]: {result['error']}")
        else:
            print(f"[GENERATED SQL]: {result['sql']}")
            print(f"[SUMMARY]: {result['answer']}")
            memory.add_interaction(question, result['answer'], result['sql'])

if __name__ == "__main__":
    main()
