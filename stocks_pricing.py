import datetime
import pandas as pd
import streamlit as st
import yfinance as yf

#st.image("./apple_logo.png",width=100)

st.write("""

# Stock Price Analyser

Shown are the the Apple Stock's **closing prices** and **volume of shares** traded.

""")


col1, col2,col3 = st.columns(3)

ticker_symbol = col1.selectbox("Select stock", ['Apple','Meta','Google','Amazon','Netflix','Tesla'])

if ticker_symbol == 'Apple':
    ticker_symbol = 'AAPL'
elif ticker_symbol == 'Meta':
    ticker_symbol = 'META'
elif ticker_symbol == 'Google':
    ticker_symbol = 'GOOGL'
elif ticker_symbol == 'Amazon':
    ticker_symbol = 'AMZN'
elif ticker_symbol == 'Netflix':
    ticker_symbol = 'NFLX'
elif ticker_symbol == 'Tesla':
    ticker_symbol = 'TSLA'



with col2:
   start_date = st.date_input("Enter strating date",datetime.date(2019,1,1))

with col3:
    end_date = st.date_input("Enter ending date",datetime.date(2022,1,1))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",start=f"{start_date}", end=f"{end_date}")

st.dataframe(ticker_df)

st.write("""
## Daily closing Price Chart
""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume of shares traded
""")
st.line_chart(ticker_df.Volume)


with st.expander("See explanation"):
    st.write("""
        - The chart above shows the Apple stock's closing prices from 2010-2022.
        - It's a line chart and hovering over a particular point will show the details in a tooltip.
        - You can also zoom in and out to play witht the detailing of the chart.
    """)
    #st.image("./images/apple.jpeg",width=50)
