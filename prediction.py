import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import timedelta, datetime

import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('fivethirtyeight')
from matplotlib.dates import DateFormatter
import matplotlib.cbook as cbook


def objects(ticker, mydb):

    mycursor = mydb.cursor()
    
    subtract_days = timedelta(days = 3650)
    
    startdate = datetime.today() - subtract_days
    startdate = startdate.strftime("%Y-%m-%d") 
    
    query = "SELECT day, close FROM history_stock_data WHERE (ticker='"+ticker+"' AND day > '"+startdate+"') ORDER BY day ASC"
    
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    data = pd.DataFrame(result, columns=["day", "Close"])
    data_copy = data
      
    data = data.filter(['Close'])
    dataset = data.values
    training_data_len = math.ceil(len(dataset) * .8)
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)
    train_data = scaled_data[0:training_data_len, :]
    x_train = []
    y_train = []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i,0])
        y_train.append(train_data[i,0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape = (60,1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
        
        
    model.compile(optimizer='adam', loss = 'mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=1)
        
    test_data = scaled_data[training_data_len-60: , :]
    x_test = []
    y_test = dataset[training_data_len: , :]
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i,0])
      
    x_test = np.array(x_test)
      
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
      
    predictions = model.predict(x_test)

    predictions = scaler.inverse_transform(predictions)


    train = data[:training_data_len]
    valid = data[training_data_len:]
    valid['Predictions'] = predictions

    x = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    xi = list(range(len(x)))
    plt.title = 'Model'

    plt.xlabel('Date', fontsize = 18)
    plt.ylabel('Close Price', fontsize = 18)
    plt.xticks(xi, x)
    plt.plot(train['Close'])
    plt.plot(valid[['Close','Predictions']])
    
    st.pyplot(plt)


    
