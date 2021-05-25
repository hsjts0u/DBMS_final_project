import yfinance as yf
import mysql.connector

#mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="",
    #database="db_stock"
#)

#cursor = mydb.cursor()

def _fetch_earning(ticker, mydb, mycursor):

    sql = "INSERT INTO earning_data (ticker, year, earning) VALUES (%s, %s, %s)"
    msft = yf.Ticker(ticker)
    ern = msft.earnings
    for i in range(len(ern.index)):
        query = "SELECT * FROM earning_data WHERE ticker= ' " + ticker + " ' AND year=' " + str(ern.index[i].item()) + "'"
        cursor.execute(query)
        result = cursor.fetchall()

        if not result:
            val = ( ticker, ern.index[i].item(), ern.loc[ern.index[i],'Earnings'].item() )
            mycursor.execute(sql, val)
            mydb.commit()

#_fetch_earning('MSFT', mydb, cursor)




