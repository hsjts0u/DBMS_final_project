import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import timedelta, datetime

def objects(mydb):
    mycursor = mydb.cursor() 
    st.header('SP500的今日收盤價和漲跌幅')
    st.write('資料為最近兩次開盤日')
    try:        
        query = """
        SELECT test.ticker, test.close, ROUND((test.close - test2.close) / test.close * 100, 2) as increase_rate
        FROM
            (SELECT *
            FROM history_stock_data
            WHERE day = (SELECT day FROM history_stock_data WHERE day != (SELECT day FROM history_stock_data ORDER BY day DESC Limit 1) ORDER BY day DESC Limit 1)
            ) as test,
            (SELECT *
            FROM history_stock_data
            WHERE day = (SELECT day FROM history_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test.close - test2.close) / test.close * 100, 2)
        ORDER BY increase_rate DESC
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','close','increase_rate(%)'])
        DF.set_index('ticker',inplace=True)
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")