import streamlit as st
from query_generator import generate_sql
from snowflake_utils import run_query

st.title("AI-Powered SQL Assistant")
prompt = st.text_input("Ask a question about your data:")

table_info = """Available tables:
1. claims(id, status, claim_date, customer_id)
2. customers(id, name, age, location)
"""  # Customize this per your schema

if prompt:
    with st.spinner("Generating SQL..."):
        sql_query = generate_sql(prompt, table_info)
        st.code(sql_query, language='sql')

        with st.spinner("Running SQL..."):
            try:
                result = run_query(sql_query)
                st.success("Query executed successfully!")
                st.write(result)
            except Exception as e:
                st.error(f"Error running query: {e}")