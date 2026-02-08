📈 AI-Powered Stock Analyser Agent

An advanced **GenAI-based stock analysis system** built using **Streamlit** and **Groq LLM**.  
This project implements a **tool-based AI agent architecture** capable of performing
technical, fundamental, and sentiment analysis on stocks with contextual memory.

---

## 🚀 Features

- 📊 Real-time stock data analysis
- 📈 Technical indicators (SMA, RSI)
- 🧾 Fundamental analysis (PE ratio, EPS, Market Cap)
- 📰 News sentiment analysis
- 🤖 AI-generated insights using Groq LLM
- 🧠 Conversation memory for contextual reasoning
- 🧩 Modular, agent-based architecture
- 🖥️ Interactive Streamlit dashboard

---

## 🧠 System Architecture
PROJECT/
│
├── app.py                  # Streamlit UI
├── main.py                 # Application orchestration layer
├── requirements.txt
├── .env
│
├── agents/
│   ├── __init__.py
│   └── stock_agent.py      # Core GenAI stock agent
│
├── tools/
│   ├── data_fetcher.py     # Stock data retrieval
│   ├── technical_analysis.py
│   ├── fundamental_analysis.py
│   └── news_analysis.py
│
├── models/
│   └── llm.py              # Groq LLM wrapper
│
├── memory/
│   └── conversation_memory.py
│
└── config/
    ├── prompts.py
    └── settings.py

