import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def objects(ticker, mydb):
    mycursor = mydb.cursor()
    st.header('Growth Rate')
    
    st.subheader('Earnings')
    query = "SELECT year, earning FROM earning_data WHERE ticker='"+ticker+"' ORDER BY year DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    df = pd.DataFrame(result, columns=['year','earning'])
    
    fig = go.Figure(data=[go.Bar(x=df['year'], y=df['earning'])])
    st.plotly_chart(fig)
    
    df.set_index("year", inplace=True)
    st.table(df)
    
    st.subheader('Revenue')
    query = "SELECT year, revenue FROM revenue_data WHERE ticker='"+ticker+"' ORDER BY year DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    df = pd.DataFrame(result, columns=['year','revenue'])
    
    fig = go.Figure(data=[go.Bar(x=df['year'], y=df['revenue'])])
    st.plotly_chart(fig)
    
    df.set_index("year", inplace=True)
    st.table(df)
