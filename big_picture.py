import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import timedelta, datetime

def show_all_TW(mydb):
    mycursor = mydb.cursor() 
    st.header("TW Stocks Trend and Today's Price")
    st.write('Data from two of the most recent market open days')
    try:        
        query = """
        SELECT test2.ticker, test2.open, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as increase_rate
        FROM
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data WHERE day != (SELECT day FROM TW_stock_data ORDER BY day DESC Limit 1) ORDER BY day DESC Limit 1)
            ) as test,
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2)
        ORDER BY increase_rate DESC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','open','close','increase_rate(%)'])
        DF.set_index('ticker',inplace=True)
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")

def show_all_SP500(mydb):
    mycursor = mydb.cursor() 
    st.header("SP500 Trend and Today's Price")
    st.write('Data from two of the most recent market open days')
    try:        
        query = """
        SELECT test2.ticker, test2.open, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as increase_rate
        FROM
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data WHERE day != (SELECT day FROM SP500_stock_data ORDER BY day DESC Limit 1) ORDER BY day DESC Limit 1)
            ) as test,
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2)
        ORDER BY increase_rate DESC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','open','close','increase_rate(%)'])
        DF.set_index('ticker',inplace=True)
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")

def up_most_SP500(mydb):
    mycursor = mydb.cursor() 
    st.header('SP500 30 Day Largest Uptrend')
    try:
        query = """
        SELECT test2.ticker, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as increase_rate
        FROM
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data WHERE day >= (SELECT CURDATE() - interval 30 day) ORDER BY day ASC Limit 1)
            ) as test,
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2) > 0
        ORDER BY increase_rate DESC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','close','increase_rate(%)'])
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")

def up_most_TW(mydb):
    mycursor = mydb.cursor() 
    st.header('TW Stocks 30 Day Largest Uptrend')
    try:
        query = """
        SELECT test2.ticker, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as increase_rate
        FROM
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data WHERE day >= (SELECT CURDATE() - interval 30 day) ORDER BY day ASC Limit 1)
            ) as test,
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2) > 0
        ORDER BY increase_rate DESC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','close','increase_rate(%)'])
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")
        
def down_most_SP500(mydb):
    mycursor = mydb.cursor() 
    st.header('SP500 30 Day Largest Downtrend')
    try:
        query = """
        SELECT test2.ticker, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as decrease_rate
        FROM
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data WHERE day >= (SELECT CURDATE() - interval 30 day) ORDER BY day ASC Limit 1)
            ) as test,
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2) < 0
        ORDER BY decrease_rate ASC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','close','decrease_rate(%)'])
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")
        
def down_most_TW(mydb):
    mycursor = mydb.cursor() 
    st.header('TW Stocks 30 Day Largest Downtrend')
    try:
        query = """
        SELECT test2.ticker, test2.close, ROUND((test2.close - test.close) / test.close * 100, 2) as decrease_rate
        FROM
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data WHERE day >= (SELECT CURDATE() - interval 30 day) ORDER BY day ASC Limit 1)
            ) as test,
            (SELECT *
            FROM TW_stock_data
            WHERE day = (SELECT day FROM TW_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test2.close - test.close) / test.close * 100, 2) < 0
        ORDER BY decrease_rate ASC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','close','decrease_rate(%)'])
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")