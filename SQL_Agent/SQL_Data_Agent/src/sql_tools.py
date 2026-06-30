import mysql.connector
from src.config import MYSQL_CONFIG

def run_select(sql: str) -> list:
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise ValueError(f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()
