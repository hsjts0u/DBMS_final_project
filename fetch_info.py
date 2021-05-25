import yfinance as yf
import mysql.connector

#mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="",
    #database="db_stock"
#)

#cursor = mydb.cursor()

def _fetch_info(ticker, mydb, mycursor):
    query = "SELECT * FROM info_data WHERE ticker='"+ ticker +"'"
    cursor.execute(query)
    result = cursor.fetchall()
    if not result:   
        sql = "INSERT INTO info_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        info_dict = yf.Ticker(ticker).info
        
        val = (ticker, info_dict['dividendRate'], info_dict['beta'], info_dict['52WeekChange'], info_dict['shortName'], info_dict['longName'], info_dict['forwardEps'], info_dict['bookValue'], info_dict['priceToBook'], info_dict['shortRatio'])
        
        cursor.execute(sql, val)
        mydb.commit()


#_fetch_info("AMZN", mydb, cursor)
