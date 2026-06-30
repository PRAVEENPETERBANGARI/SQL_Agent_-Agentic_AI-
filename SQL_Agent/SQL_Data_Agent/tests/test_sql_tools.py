import pytest
from src.sql_tools import run_select

def test_run_select_invalid_sql():
    # Tests that a bad SQL command throws the expected custom ValueError
    # rather than crashing the application entirely.
    with pytest.raises(ValueError, match="Database error:"):
        run_select("SELECT * FROM table_that_does_not_exist")