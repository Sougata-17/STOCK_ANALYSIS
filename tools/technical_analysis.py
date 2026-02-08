import pandas as pd

def technical_indicators(df):
    df["SMA_20"] = df["Close"].rolling(20).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))

    latest = df.iloc[-1]

    return {
        "SMA_20": round(latest["SMA_20"], 2),
        "SMA_50": round(latest["SMA_50"], 2),
        "RSI": round(latest["RSI"], 2)
    }
