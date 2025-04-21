import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

def run_query(query):
    
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def get_table_schema(table_names: list) -> str:
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA") )

    cur = conn.cursor()
    schema_details = []

    for table in table_names:
        cur.execute(f"DESCRIBE TABLE {table}")
        columns = cur.fetchall()
        if columns:
            schema = f"{table}(\n" + ",\n".join(
                [f"    {col[0]} {col[1]}" for col in columns]
            ) + "\n)"
            schema_details.append(schema)

    cur.close()
    conn.close()
    return "\n\n".join(schema_details)
