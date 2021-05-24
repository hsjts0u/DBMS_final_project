import mysql.connector
import yfinance as yf
import datetime
import requests
import time
import numpy as np
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="ghaad123",
  password="",
  database="exam"
)

cursor = mydb.cursor()
#yf.Ticker(ticker).history(start = "2000-01-03", end = datetime.date.today()).to_csv(ticker+'_history.csv')
def _fetch_history(ticker, mydb, mycursor):
    sql = "INSERT INTO financial VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    dic = {} 
    
    symb = yf.Ticker(ticker).history(start = "2000-01-03", end = datetime.date.today())
    #print(symb)
    Fin = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
    print(symb.iloc['Open'])
    """
    for i in Fin:
        dic[i] = symb.loc[i]
    """
    """
    for i in range(len(dic['Date'])):
        #temp = dic['Date'].index[i].strftime('%Y-%m-%d')
        val = ( ticker, dic['Date'][i], dic['Open'][i], dic['High'][i], dic['Low'][i], dic['Close'][i], dic['Volume'][i] )
        cursor.execute(sql, val)
        mydb.commit()
    """
_fetch_history('AAPL', mydb,cursor)

