import yfinance as yf
import numpy as np
import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_stock"
)

cursor = mydb.cursor()

def _fetch_financial(ticker, mydb, mycursor):
    sql = "INSERT INTO financial VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    dic = {} 

    symb = yf.Ticker(ticker)
    Fin = ('Research Development', 'Net Income', 'Gross Profit', 'Ebit', 'Operating Income', 'Interest Expense')
    
    for i in Fin:
        dic[i] = symb.financials.loc[i]

    for i in range(len(dic['Research Development'])):
        temp = dic['Research Development'].index[i].strftime('%Y-%m-%d')
        val = ( ticker, temp, dic['Research Development'][i], dic['Net Income'][i], dic['Gross Profit'][i], dic['Ebit'][i], dic['Operating Income'][i], dic['Interest Expense'][i] )
       
        testing = "SELECT * FROM financial WHERE ticker='"+ ticker +"' AND date='" + temp + "'"
        cursor.execute(testing)
        result = cursor.fetchall()
        if not result :
            cursor.execute(sql, val)
            mydb.commit()
        
_fetch_financial('AMZN',mydb, cursor)
