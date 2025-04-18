import os
from dotenv import load_dotenv
load_dotenv()

def generate_sql(prompt: str, table_schema: str, provider: str = "openai") -> str:
    full_prompt = f"""
    You are an assistant that helps convert natural language questions into clean SQL queries.
    Generate only the SQL query without any extra explanation or markdown formatting.

    Table Schema:
    {table_schema}

    Question:
    {prompt}
    """

    if provider == "ollama":
        from openai import OpenAI
        MODEL = "llama3"
        openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    else:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        MODEL = "gpt-4o"

    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You're a helpful SQL generator."},
            {"role": "user", "content": full_prompt}
        ]
    )

    sql_response = response.choices[0].message.content.strip()

    if sql_response.startswith("```sql"):
        sql_response = sql_response.replace("```sql", "").replace("```", "").strip()

    return sql_response
