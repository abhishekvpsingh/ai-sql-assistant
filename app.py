import streamlit as st
from query_generator import generate_sql
from snowflake_utils import run_query

st.title("AI-Powered SQL Assistant")

provider = st.radio("Choose Model Provider:", options=["OpenAI", "Ollama"])

prompt = st.text_input("Ask a question about your data:")

table_info = """Available tables:
raw_orders(
    InvoiceNo VARCHAR,
    StockCode VARCHAR,
    Description VARCHAR,
    Quantity NUMBER,
    InvoiceDate TIMESTAMP_NTZ,
    UnitPrice NUMBER,
    CustomerID NUMBER,
    Country VARCHAR
)
"""

if prompt:
    with st.spinner("Generating SQL..."):
        sql_query = generate_sql(prompt, table_info, provider=provider.lower())
        st.code(sql_query, language='sql')

        with st.spinner("Running SQL..."):
            try:
                result = run_query(sql_query)
                st.success("Query executed successfully!")
                st.write(result)
            except Exception as e:
                st.error(f"Error running query: {e}")
