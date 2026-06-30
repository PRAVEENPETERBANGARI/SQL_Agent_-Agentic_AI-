import re

BLOCKED = ["insert", "update", "delete", "drop", "alter", "truncate", "create", "replace"]

def validate_sql(sql: str) -> str:
    cleaned = sql.strip().lower()
    if any(re.search(rf"\b{word}\b", cleaned) for word in BLOCKED):
        raise ValueError("Destructive or write SQL is blocked.")    
    elif not cleaned.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")
    elif ";" in cleaned.rstrip(";"):
        raise ValueError("Multiple SQL statements are not allowed.")

    return sql.strip().rstrip(";")

# validate_sql("DROP TABLE stores;")
