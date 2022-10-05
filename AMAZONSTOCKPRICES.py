import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## AMAZON Stock prices
""")


tickerSymbol = 'AMZN'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2020-1-31')


st.line_chart(tickerDf.High)
st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Volume)
