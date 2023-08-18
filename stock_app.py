import yfinance as yf
import streamlit as st
import pandas as pd

# Create a text input widget for user to input ticker symbol with default value and custom key
user_input = st.text_input("Enter a Ticker Symbol:", value='^GSPC', key='ticker_input')

# Display a custom name for the S&P 500 ticker
if user_input == '^GSPC':
    display_ticker_name = "the S&P 500"
else:
    display_ticker_name = user_input

st.write(f"""
## Simple Stock Data Visualization App

Shown are the stock **closing price** and ***volume*** of {display_ticker_name}!

""")  

# Get data on the user-input ticker
tickerData = yf.Ticker(user_input)

# Get the historical prices for the user-input ticker up to the current day
tickerDf = tickerData.history(period='1d', start='2010-5-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)
