import yfinance as yf
import mysql.connector
import streamlit as st

#mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="",
    #database="db_stock"
#)

#cursor = mydb.cursor()

def _fetch_info(ticker, mydb, mycursor):
    st.write(ticker)
    st.write(mydb)
    st.write(mycursor)
    query = "SELECT * FROM info_data WHERE ticker='"+ ticker +"'"
    mycursor.execute(query)
    result = mycursor.fetchall()
    st.write(result)
    st.write("here")
    if not result:   
        sql = "INSERT INTO info_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        info_dict = yf.Ticker(ticker).info
        
        val = (ticker, info_dict['dividendRate'], info_dict['beta'], info_dict['52WeekChange'], info_dict['shortName'], info_dict['longName'], info_dict['forwardEps'], info_dict['bookValue'], info_dict['priceToBook'], info_dict['shortRatio'])
        
        cursor.execute(sql, val)
        mydb.commit()


#_fetch_info("AMZN", mydb, cursor)
