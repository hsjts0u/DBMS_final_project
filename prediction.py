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

    fig, ax = plt.subplots()
    ax.plot('day', 'Close', data=data_copy)

    # Major ticks every 6 months.
    fmt_half_year = mdates.MonthLocator(interval=6)
    ax.xaxis.set_major_locator(fmt_half_year)

    # Minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax.xaxis.set_minor_locator(fmt_month)

    # Text in the x axis will be displayed in 'YYYY-mm' format.
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Round to nearest years.
    datemin = np.datetime64(data_copy['day'][0], 'Y')
    datemax = np.datetime64(data_copy['day'][21], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(datemin, datemax)

    # Format the coords message box, i.e. the numbers displayed as the cursor moves
    # across the axes within the interactive GUI.
    ax.format_xdata = mdates.DateFormatter('%Y-%m')
    ax.format_ydata = lambda x: f'${x:.2f}'  # Format the price.
    ax.grid(True)

    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()
    
    st.pyplot(plt)







'''    data = data.filter(['Close'])
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
	
	
	plt.figure(figsize=(16,8))
	plt.title = 'Model'

	plt.xlabel('Date', fontsize = 18)
	plt.ylabel('Close Price', fontsize = 18)
	plt.plot(train['Close'])
	plt.plot(valid[['Close','Predictions']])
	plt.show()
	
	'''
