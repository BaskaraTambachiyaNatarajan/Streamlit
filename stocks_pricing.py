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

stock = col1.selectbox("Select stock", ['Apple','Meta','Google','Amazon','Netflix','Tesla'])

ticker_symbol = 'AAPL'

if stock == 'Apple':
    ticker_symbol = 'AAPL'
elif stock == 'Meta':
    ticker_symbol = 'META'
elif stock == 'Google':
    ticker_symbol = 'GOOGL'
elif stock == 'Amazon':
    ticker_symbol = 'AMZN'
elif stock == 'Netflix':
    ticker_symbol = 'NFLX'
elif stock == 'Tesla':
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
    st.write(f"""
        - The chart above shows the {stock} stock's closing prices from {start_date.strftime("%d %b %Y")} to {end_date.strftime("%d %b %Y")}.
        - It's a line chart and hovering over a particular point will show the details in a tooltip.
        - You can also zoom in and out to play witht the detailing of the chart.
    """)
    #st.image("./images/apple.jpeg",width=50)
