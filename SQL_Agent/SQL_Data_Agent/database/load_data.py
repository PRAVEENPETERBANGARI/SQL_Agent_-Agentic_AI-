import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def load_data():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    cursor = conn.cursor()
    
    files = {
        "stores": "data/stores.csv",
        "products": "data/products.csv",
        "customers": "data/customers.csv",
        "sales_transactions": "data/sales_transactions.csv",
        "returns": "data/returns.csv"
    }

    for table, file_path in files.items():
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
        
            df.columns = df.columns.str.strip()

            for col in df.columns:
                if 'date' in col.lower():
                    # Parse the date (dayfirst=True handles DD-MM-YYYY) and output as YYYY-MM-DD
                    df[col] = pd.to_datetime(df[col], dayfirst=True).dt.strftime('%Y-%m-%d')

            cols = ",".join([str(i) for i in df.columns.tolist()])
            placeholders = ",".join(["%s"] * len(df.columns))
            sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
            
            for i, row in df.iterrows():
                cursor.execute(sql, tuple(row))
            conn.commit()
            print(f"Loaded {len(df)} rows into {table}.")
        else:
            print(f"File {file_path} not found.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data()
