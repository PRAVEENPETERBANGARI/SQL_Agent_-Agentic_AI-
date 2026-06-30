from src.memory import ConversationMemory

def test_memory_retention():
    # Initialize memory and add a mock interaction
    mem = ConversationMemory()
    mem.add_interaction(
        question="How many stores are there?", 
        answer="There are 50 stores.", 
        sql="SELECT COUNT(*) FROM stores"
    )
    
    # Retrieve the context and verify the data is present
    context = mem.get_context()
    assert "How many stores are there?" in context
    assert "SELECT COUNT(*) FROM stores" in context
    assert "There are 50 stores." in context
    
def test_empty_memory():
    # Ensure a brand new memory object handles empty context gracefully
    mem = ConversationMemory()
    assert mem.get_context() == "No previous context."

def test_memory_limit():
    # Ensure memory only keeps the most recent 3 interactions (based on our memory.py logic)
    mem = ConversationMemory()
    for i in range(5):
        mem.add_interaction(f"Q{i}", f"A{i}", f"SQL{i}")
        
    context = mem.get_context()
    # Q0 and Q1 should be forgotten, Q2, Q3, and Q4 should remain
    assert "Q0" not in context
    assert "Q4" in context