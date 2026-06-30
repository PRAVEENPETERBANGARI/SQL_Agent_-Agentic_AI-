from typing import TypedDict
from langgraph.graph import StateGraph, END
from src.tiger_gateway_client import call_llm
from src.safety import validate_sql
from src.sql_tools import run_select
import re

class AgentState(TypedDict):
    question: str
    context: str
    sql: str
    rows: list
    answer: str
    error: str

SCHEMA = """
Tables:
- stores (store_id, store_name, region, city, store_type)
- products (product_id, product_name, category, sub_category, base_price)
- customers (customer_id, customer_segment, signup_date, preferred_channel, city)
- sales_transactions (order_id, order_date, store_id, product_id, customer_id, sales_channel, units_sold, unit_price, discount_pct, payment_status, delivery_status)
- returns (return_id, order_id, return_date, return_reason)
"""

def generate_sql(state: AgentState):
    prompt = f"""
    You are an expert Data Analyst. Translate the user's question into a valid MySQL query.
    
    Data Dictionary & Calculation Rules:
    - The 'discount_pct' column in 'sales_transactions' is stored as a whole number (e.g., 20 represents 20%).
    - When calculating discounted revenue, you MUST convert the discount to a decimal by dividing by 100.
    - MANDATORY REVENUE FORMULA: SUM(units_sold * unit_price * (1 - (COALESCE(discount_pct, 0) / 100.0)))
    
    Database Schema: 
    {SCHEMA}
    
    Additional Context:
    {state.get('context', '')}
    
    Question: {state['question']}
    
    Output ONLY the valid SQL query without markdown formatting or explanation.
    """
    sql_raw = call_llm([{"role": "user", "content": prompt}])
    sql_cleaned = re.sub(r"```sql|```", "", sql_raw).strip()
    return {"sql": sql_cleaned}

def execute_sql(state: AgentState):
    try:
        valid_sql = validate_sql(state["sql"])
        rows = run_select(valid_sql)
        return {"rows": rows, "error": ""}
    except Exception as e:
        return {"error": str(e), "rows": []}

def summarize(state: AgentState):
    if state.get("error"):
        return {"answer": f"I couldn't retrieve the data. Error: {state['error']}"}
    
    prompt = f"Question: {state['question']}\nData Result: {state['rows'][:50]}\nProvide a concise business summary."
    answer = call_llm([{"role": "user", "content": prompt}])
    return {"answer": answer}

graph = StateGraph(AgentState)
graph.add_node("generate_sql", generate_sql)
graph.add_node("execute_sql", execute_sql)
graph.add_node("summarize", summarize)

graph.set_entry_point("generate_sql")
graph.add_edge("generate_sql", "execute_sql")
graph.add_edge("execute_sql", "summarize")
graph.add_edge("summarize", END)

agent_app = graph.compile()
