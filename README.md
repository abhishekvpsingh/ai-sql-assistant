# 💬 AI-Powered SQL Query Assistant

This project is an AI-based tool that allows users to enter plain English questions about their data, converts them into SQL queries using OpenAI, and runs them directly on a Snowflake data warehouse. It is built using Python and Streamlit for a simple and interactive interface.

---

## 📌 Features

- Convert natural language questions into SQL queries using OpenAI.
- Run queries on Snowflake and display results in a friendly format.
- Simple web UI built with Streamlit.
- Easy setup and extensible for real-world use.

---

## 🧠 Tech Stack

- Python 3.9+
- OpenAI GPT-3.5 Turbo
- Streamlit
- Snowflake Connector for Python
- Dotenv for managing secrets

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abhishekvpsingh/ai-sql-assistant.git
cd ai-sql-assistant
```

### 2. Install Dependencies

Make sure you’re in a virtual environment, then run:

```bash
pip install -r requirements.txt
```

> You can generate `requirements.txt` using:
> ```bash
> pip freeze > requirements.txt
> ```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your credentials:

```
OPENAI_API_KEY=your_openai_api_key
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account_url
SNOWFLAKE_DATABASE=your_database
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_WAREHOUSE=your_warehouse
```

### 4. Start the Streamlit App

```bash
streamlit run app.py
```

This will launch the app in your browser at `http://localhost:8501`

---

## 📂 Project Structure

```
ai-sql-assistant/
│
├── app.py                    # Streamlit UI and logic
├── query_generator.py        # Logic to call OpenAI and generate SQL
├── snowflake_utils.py        # Snowflake connection and query execution
├── .env                      # Environment variables (not pushed to Git)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 💡 Sample Table Metadata (for testing)

You can define your Snowflake schema in `app.py` for AI context. For example:

```plaintext
Available tables:
1. claims(id, status, claim_date, customer_id)
2. customers(id, name, age, location)
```

---

## 🔧 Future Enhancements (Optional)

- ✅ Add authentication (login interface using Streamlit’s login manager or Firebase)
- ✅ Display SQL query execution time and record counts
- ✅ Save history of queries and results
- ✅ Add chat-like interaction with memory
- ✅ Use RAG (Retrieval-Augmented Generation) for better schema-awareness
- ✅ Export query results as CSV or Excel
- ✅ Improve error handling and display suggestions if query fails

---

## 👨‍💻 Author

**Abhishek Singh**

If you found this helpful, feel free to ⭐ the repo and connect with me on [LinkedIn](https://www.linkedin.com/abhishekvpsingh/)
