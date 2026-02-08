import streamlit as st
import plotly.graph_objects as go
from main import run_analysis

st.set_page_config(page_title="AI Stock Analyser", layout="wide")

st.title("📈 AI-Powered Stock Analyser")
st.caption("GenAI-based stock analysis using Groq")

symbol = st.text_input("Enter Stock Symbol (e.g. AAPL, TSLA, INFY)", "AAPL")

if st.button("Analyze"):
    with st.spinner("Analyzing stock data..."):
        analysis, hist = run_analysis(symbol)

    st.subheader("📊 Price Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["Close"],
        mode="lines",
        name="Close Price"
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🤖 AI Analysis")
    st.write(analysis)
