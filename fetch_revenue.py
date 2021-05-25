import yfinance as yf
import mysql.connector

#mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="",
    #database="db_stock"
#)

#cursor = mydb.cursor()

def _fetch_revenue(ticker, mydb, mycursor):

    sql = "INSERT INTO revenue_data (ticker, year, revenue) VALUES (%s, %s, %s)"
    msft = yf.Ticker(ticker)
    ern = msft.earnings

    for i in range(len(ern.index)):
        query = "SELECT * FROM revenue_data WHERE ticker= ' " + ticker + " ' AND year=' " + str(ern.index[i].item()) + "'"
        cursor.execute(query)
        result = cursor.fetchall()

        if not result:
            val = ( ticker, ern.index[i].item(), ern.loc[ern.index[i],'Revenue'].item() )
            mycursor.execute(sql, val)
            mydb.commit()

#_fetch_revenue('MSFT', mydb, cursor)






