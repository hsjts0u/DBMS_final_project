import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go


def objects(ticker, mydb):

    st.header(f'Predict stock prices for {ticker}')
    
    mycursor = mydb.cursor()

    n_years = st.sidebar.slider('Years of prediction:', 1, 4)
    period = n_years * 365
    
    
    #data_load_state = st.text('Loading data...')
    data = load_data(ticker)
    #data_load_state.text('Loading data... done!')

    st.subheader('Historical stock price data')
    st.write(data.tail())


    plot_raw_data(data)

    # Predict forecast with Prophet.
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Show and plot forecast
    st.subheader('Predict data')
    st.write(forecast.tail())
        
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, "2011-01-01", date.today().strftime("%Y-%m-%d"))
    data.reset_index(inplace=True)
    return data


# Plot raw data
def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

