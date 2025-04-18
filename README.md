# 💬 AI-Powered SQL Query Assistant

This project is an AI-based tool that allows users to enter plain English questions about their data, converts them into SQL queries using **OpenAI or Ollama**, and runs them directly on a **Snowflake** data warehouse. It is built using **Python** and **Streamlit** for a simple and interactive interface.

---

## 📌 Features

- Convert natural language questions into SQL queries using **OpenAI GPT** or **Ollama (free & local)**.
- Run queries on Snowflake and display results in a user-friendly format.
- Choose your AI model provider directly from the UI.
- Simple web UI built with Streamlit.
- Easy setup and extensible for real-world use.

---

## 🧠 Tech Stack

- Python 3.9+
- OpenAI GPT-4o or GPT-3.5 Turbo
- Ollama (local LLM like LLaMA3)
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

### 4. Install & Run Ollama (Optional if using local models)

#### ✅ macOS

```bash
brew install ollama
ollama run llama3
```

#### ✅ Windows (via WSL recommended)

1. Install WSL (Windows Subsystem for Linux)
2. Inside WSL:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama run llama3
   ```

#### ✅ Linux (Ubuntu/Debian)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3
```

This will pull and start the **llama3** model locally at `http://localhost:11434`.

> ❗ Make sure `ollama` is running before you start the Streamlit app if you select "Ollama" as the model provider.

---

### 5. Start the Streamlit App

```bash
streamlit run app.py
```

Then go to [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💡 Sample Table Metadata (for testing)

You can define your Snowflake schema in `app.py` to give the AI context. Example:

```plaintext
Available tables:
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
```

---

## 📂 Project Structure

```
ai-sql-assistant/
│
├── app.py                    # Streamlit UI and logic
├── query_generator.py        # Handles OpenAI & Ollama-based SQL generation
├── snowflake_utils.py        # Snowflake connection and query execution
├── .env                      # Environment variables (excluded from Git)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 🔧 Future Enhancements

- ✅ Use either OpenAI or Ollama for SQL generation
- ✅ Add authentication (login interface)
- ✅ Display SQL query execution time and record count
- ✅ Save history of queries and results
- ✅ Add chat-style interface with memory
- ✅ Use RAG (Retrieval-Augmented Generation) for better schema-awareness
- ✅ Export results as CSV/Excel
- ✅ Improve error handling and give AI-powered suggestions on failure

---

## 👨‍💻 Author

**Abhishek Singh**

If you found this helpful, feel free to ⭐ the repo and connect with me on [LinkedIn](https://www.linkedin.com/in/abhishekvpsingh/)