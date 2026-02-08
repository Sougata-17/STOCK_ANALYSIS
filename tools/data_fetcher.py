import yfinance as yf

def fetch_stock_data(symbol, period="6mo"):
    stock = yf.Ticker(symbol)
    hist = stock.history(period=period)
    info = stock.info
    return hist, info
