import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import timedelta, datetime

def objects(mydb):
    mycursor = mydb.cursor() 
    st.header('30 Day Largest Downtrend')
    try:
        query = """
        SELECT test.ticker, ROUND((test.close - test2.close) / test.close * 100, 2) as decrease_rate
        FROM
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data WHERE day >= (SELECT CURDATE() - interval 30 day) ORDER BY day ASC Limit 1)
            ) as test,
            (SELECT *
            FROM SP500_stock_data
            WHERE day = (SELECT day FROM SP500_stock_data ORDER BY day DESC Limit 1)
            ) as test2
        WHERE test.ticker = test2.ticker and  ROUND((test.close - test2.close) / test.close * 100, 2) < 0
        ORDER BY decrease_rate ASC
        LIMIT 100
                """
        mycursor.execute(query)
        result = mycursor.fetchall()
        DF = pd.DataFrame(result, columns=['ticker','decrease_rate(%)'])
        DF.set_index('ticker',inplace=True)
        st.table(DF)
    except:
        st.error(f"There is no data in your database, try pressing the quick start button.")
