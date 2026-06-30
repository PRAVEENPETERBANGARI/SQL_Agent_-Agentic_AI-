import pytest
from src.safety import validate_sql

def test_valid_select():
    # A standard safe query should pass through unmodified (just lowercased/stripped)
    sql = "SELECT * FROM products WHERE category = 'electronics';"
    result = validate_sql(sql)
    assert result.lower() == "select * from products where category = 'electronics'"

def test_blocked_keywords():
    # Any query with a blocked keyword like DROP or DELETE should raise a ValueError
    with pytest.raises(ValueError, match="Destructive or write SQL is blocked."):
        validate_sql("DROP TABLE stores;")
        
    with pytest.raises(ValueError, match="Destructive or write SQL is blocked."):
        validate_sql("DELETE FROM customers WHERE customer_id = 'C1';")

def test_non_select():
    # Queries that don't start with SELECT should be blocked
    with pytest.raises(ValueError, match="Only SELECT queries are allowed."):
        validate_sql("EXPLAIN stores;")

def test_multiple_statements():
    # Queries attempting SQL injection via multiple statements should be blocked
    with pytest.raises(ValueError, match="Multiple SQL statements are not allowed."):
        validate_sql("SELECT * FROM stores; SELECT * FROM products")