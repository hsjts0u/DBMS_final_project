import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import timedelta, datetime

def objects(ticker, mydb):
    num_days = st.sidebar.slider('Number of days', 0, 30, 0)
    num_months = st.sidebar.slider('Number of months', 1, 12, 1)
    num_years = st.sidebar.slider('Number of years', 0, 20, 0)
    mycursor = mydb.cursor()
    subtract_days = timedelta(days = 365 * num_years + 30 * num_months + num_days)
    startdate = datetime.today() - subtract_days
    startdate = startdate.strftime("%Y-%m-%d") 
    query = "SELECT day, open, high, low, close, volume FROM history_stock_data WHERE (ticker= ticker AND day > '"+startdate+"') ORDER BY day DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    DF = pd.DataFrame(result, columns=['Date','Open','High','Low','Close','Volume'])
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=DF['Date'], open=DF['Open'], high=DF['High'], low=DF['Low'], close=DF['Close']))
    DF.reset_index(inplace=False)
    DF.set_index("Date", inplace=True)
    st.line_chart(DF["Close"])
    st.plotly_chart(fig)
    st.table(DF)
    
