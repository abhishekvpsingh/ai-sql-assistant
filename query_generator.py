import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sql(prompt, table_info):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a data analyst. Use the following table info:\n{table_info}"},
            {"role": "user", "content": f"Write a SQL query for: {prompt}"}
        ]
    )
    return response['choices'][0]['message']['content']
