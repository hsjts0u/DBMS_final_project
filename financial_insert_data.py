import mysql.connector
import yfinance as yf
import numpy as np

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_stock"
)

cursor = mydb.cursor()
sql = "INSERT INTO financial VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
dic = {} 

msft = yf.Ticker("MSFT")
Fin = ('Research Development', 'Net Income', 'Gross Profit', 'Ebit', 'Operating Income', 'Interest Expense')
for i in Fin:
     dic[i] = msft.financials.loc[i]

for i in range(len(dic['Research Development'])):
    temp = dic['Research Development'].index[i].strftime('%Y-%m-%d')
    val = ( 'MSFT',temp, dic['Research Development'][i], dic['Net Income'][i], dic['Gross Profit'][i], dic['Ebit'][i], dic['Operating Income'][i], dic['Interest Expense'][i] )
    cursor.execute(sql,val)
    mydb.commit()
