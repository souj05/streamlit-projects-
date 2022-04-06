import numpy as np
import pandas as pd
import streamlit as st
# Yfinance is a python package which is used to download historical stock data &
# from yahoo finance api in pythonic way and the problem is it is time taking
import yfinance as yf

st.write("""
# Simple Stock Price App
Shown are the stock     **Open , Close** , **volume** , **Highest ,Lowest prices**   of    ***Freshworks!***
""")
st.markdown("""This App is Built By **Sowjanya!** """)

# define ticker symbol
tickerSymbol = 'FRSH'
# get the data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2021-4-5', end='2022-4-5')

# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.write("""
## Open Price
""")
st.line_chart(tickerDf.Open)
st.write("""
## Highest
""")
st.line_chart(tickerDf.High)
st.write("""
## Lowest
""")
st.line_chart(tickerDf.Low)





