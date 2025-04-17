import openai
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

def generate_sql(prompt: str, table_schema: str) -> str:
    full_prompt = f"""
    You are an assistant that helps convert natural language questions into clean SQL queries.
    Generate only the SQL query without any extra explanation or markdown formatting.

    Table Schema:
    {table_schema}

    Question:
    {prompt}
    """

    response = openai.chat.completions.create(
        model="gpt-4o",  # You can also try "gpt-3.5-turbo" if needed
        messages=[{"role": "system", "content": "You're a helpful SQL generator."},
                {"role": "user", "content": full_prompt}]
    )

    sql_response = response.choices[0].message.content.strip()

        # Clean up common wrappers like ```sql ... ```
    if sql_response.startswith("```sql"):
        sql_response = sql_response.replace("```sql", "").replace("```", "").strip()

    return sql_response


