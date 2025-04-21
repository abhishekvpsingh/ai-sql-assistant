import streamlit as st
from query_generator import generate_sql
from snowflake_utils import run_query, get_table_schema 

st.title("AI-Powered SQL Assistant")

provider = st.radio("Choose Model Provider:", options=["OpenAI", "Ollama"])

table_input = st.text_input("Enter table name(s) separated by commas (e.g. raw_orders, customer_info):")

prompt = st.text_input("Ask a question about your data:")

if prompt and table_input:
    table_names = [t.strip() for t in table_input.split(",")]

    with st.spinner("Fetching table schema..."):
        try:
            table_info = get_table_schema(table_names)
            st.text_area("📘 Table Schema Fetched:", table_info, height=200)
        except Exception as e:
            st.error(f"❌ Error fetching schema: {e}")
            table_info = ""

    if table_info:
        with st.spinner("Generating SQL..."):
            sql_query = generate_sql(prompt, table_info, provider=provider.lower())
            st.code(sql_query, language='sql')

            with st.spinner("Running SQL..."):
                try:
                    result = run_query(sql_query)
                    st.success("Query executed successfully!")

                    # Handle single value result (like COUNT)
                    if len(result) == 1 and len(result[0]) == 1:
                        st.metric(label="Result", value=result[0][0])
                    else:
                        # For multi-row or multi-column results
                        import pandas as pd
                        df = pd.DataFrame(result)
                        st.dataframe(df)

                except Exception as e:
                    st.error(f"Error running query: {e}")

