import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

sample_stock_list = ('PHM','AOS','GM','FGEN','GOOGL')

tickerSymbol = st.selectbox(
    'How would you like to be contacted?',
    sample_stock_list)


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


st.text('Close price of stock')

st.line_chart(tickerDf.Close)

st.text('Volume of stock')

st.line_chart(tickerDf.Volume)
