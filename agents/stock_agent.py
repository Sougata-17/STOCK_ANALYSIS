from tools.data_fetcher import fetch_stock_data
from tools.technical_analysis import technical_indicators
from tools.fundamental_analysis import fundamental_metrics
from tools.news_analysis import sentiment_analysis

from models.llm import call_llm
from config.prompts import SYSTEM_PROMPT, ANALYSIS_PROMPT
from memory.conversation_memory import ConversationMemory

# ---------------------------------------------------
# Initialize agent-level memory (persists across calls)
# ---------------------------------------------------
memory = ConversationMemory()


def analyze_stock(symbol, query="Full stock analysis"):
    """
    Main stock analysis agent.
    Returns:
        - AI-generated analysis text
        - Historical price dataframe
    """

    # ---- Store user intent in memory ----
    memory.add("user", f"{symbol}: {query}")

    # ---- Fetch stock data ----
    hist, info = fetch_stock_data(symbol)

    # ---- Tool-based analysis ----
    technical = technical_indicators(hist)
    fundamental = fundamental_metrics(info)
    sentiment = sentiment_analysis(info.get("news", []))

    # ---- Build LLM prompt ----
    prompt = ANALYSIS_PROMPT.format(
        symbol=symbol,
        technical=technical,
        fundamental=fundamental,
        sentiment=sentiment
    )

    # ---- Call LLM with memory ----
    response = call_llm(
        SYSTEM_PROMPT,
        prompt,
        memory.get()
    )

    # ---- Store AI response in memory ----
    memory.add("assistant", response)

    return response, hist
