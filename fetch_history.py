import yfinance as yf
import datetime
import time
import numpy as np
import pandas as pd
import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="",
#  database="db_stock"
#)

#cursor = mydb.cursor()

def _fetch_history(ticker, mydb, mycursor):
    sql = "INSERT INTO history_stock_data VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dic = {} 
        
    symb = yf.Ticker(ticker).history(start = "2000-01-03", end = datetime.date.today())
   
    for i in range(len(symb.index)):
        temp = symb.index[i].strftime('%Y-%m-%d')
        query = "SELECT * FROM history_stock_data WHERE ticker='"+ticker+"' AND day='"+temp+"'"
        cursor.execute(query)
        result = cursor.fetchall()
        
        if not result :
            val = ( ticker, temp, symb['Open'][i].item(), symb['High'][i].item(), symb['Low'][i].item(), symb['Close'][i].item(), symb['Volume'][i].item() )
            cursor.execute(sql, val)
            mydb.commit()
    
#_fetch_history('AAPL', mydb,cursor)

