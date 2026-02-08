from agents.stock_agent import analyze_stock

def run_analysis(symbol: str, query: str = "Full stock analysis"):
    """
    Application-level function.
    Called by Streamlit or any other interface.
    """
    return analyze_stock(symbol, query)
