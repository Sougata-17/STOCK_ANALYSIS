def route_tools(query: str):
    query = query.lower()

    tools = []

    if any(word in query for word in ["rsi", "trend", "overbought", "oversold"]):
        tools.append("technical")

    if any(word in query for word in ["profit", "fundamental", "pe", "eps"]):
        tools.append("fundamental")

    if any(word in query for word in ["news", "sentiment", "why", "reason"]):
        tools.append("news")

    if not tools:
        tools = ["technical", "fundamental", "news"]

    return tools
