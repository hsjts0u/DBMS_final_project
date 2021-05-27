import streamlit as st
from schema import tables
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import mysql.connector
import fetch
import description
import price
#import prediction
import growth
import up_most
import down_most
import requests
# MySQL connection objects

@st.cache(allow_output_mutation=True)
def db_cursor_cache():
    return []

db_objects = db_cursor_cache()

# Streamlit Interface

st.title('Stock Analysis')

st.sidebar.title('Options')

option = st.sidebar.selectbox('Action', ('Start Here', 'Explore','Big Picture', 'Begin Analyzing'))



if option == 'Start Here':
    
    st.header('Start Here')
    
    st.write("Welcome to the dashboard for stock analysis. If you have not already created a database, one will be created for you in MySQL. Press the button below to initialize an empty database or connect to an existing database.")

    host = st.text_input('Host', value='', max_chars=None, key=None, type='default', help='Enter your hostname')
    user = st.text_input('MySQL user', value='', max_chars=None, key=None, type='default', help='Enter your MySQL user')
    password = st.text_input('MySQL password', value='', max_chars=None, key=None, type='password', help='Enter your MySQL password')
    dbname = st.text_input('MySQL database', value='', max_chars=None, key=None, type='default', help='Enter your database name')
    
    if st.button("Connect !"):
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )
            st.success("Connection Succesful !")
            
            # cache db and cursor
            mycursor = mydb.cursor
            db_objects.append(mydb)
            db_objects.append(mycursor)
            
        except mysql.connector.Error:
            st.error("Your database does not exist, proceed to create a new database by pressing ' Create new database! '")
    
    if st.button("Create new database !"):
        try:
            tmpdb = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            tmpcursor = tmpdb.cursor()
            tmpcursor.execute(f"CREATE DATABASE {dbname}")
            
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname,
                allow_local_infile=True
            )
            mycursor = mydb.cursor()
            
            # cache db and cursor
            db_objects.append(mydb)
            db_objects.append(mycursor)
            for table in tables.tables:
                mycursor.execute(table)
            mydb.commit()
            st.success("Creation and Connection Succesful !")
        except mysql.connector.Error as err:
            st.error("""Oops! An error occurred along the way ... 
                        {}""".format(err))

if option == 'Begin Analyzing':
    ### retrieve db and cursor
    try:
        mydb = db_objects[0]
        mycursor = db_objects[1]
    except:
        st.sidebar.error("Connect to a database first")
        
    ticker = st.sidebar.text_input('Ticker', value='2330.TW', max_chars=None, key=None, type='default', help='Enter the company ticker here')
    
    ### update data for ticker
    if st.sidebar.button("Update info for this company"):
        try:
            fetch._fetch_info(ticker, mydb, mycursor)
            fetch._fetch_financial(ticker, mydb, mycursor)
            fetch._fetch_earning(ticker, mydb, mycursor)
            fetch._fetch_revenue(ticker, mydb, mycursor)
            fetch._fetch_history(ticker, mydb, mycursor)
        except mysql.connector.Error as err:
            st.sidebar.error("Something went wrong: {}".format(err))
    
    #if st.sidebar.button("Show me a random company !"):
    #    st.sidebar.success("Now showing data for a random company")
        
    analysis_tool = st.sidebar.selectbox('Analysis Tools', ('Company Description', 'Historical Prices', 'Growth Rate', 'Prediction'))
    
    if analysis_tool == 'Company Description':
        description.objects(ticker, mydb)
    
    if analysis_tool == 'Historical Prices':
        price.objects(ticker, mydb)

    if analysis_tool == 'Growth Rate':
        growth.objects(ticker, mydb)
    if analysis_tool == 'Prediction':
    	#prediction.objects(ticker, mydb)
    	pass
    
if option == 'Big Picture': 
    ### retrieve db and cursor
    try:
        mydb = db_objects[0]
        mycursor = db_objects[1]
    except:
        st.sidebar.error("Connect to a database first")
    
    ###show the recent stock market
    url = 'https://www.slickcharts.com/sp500'
    headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    request = requests.get(url, headers = headers)

    data = pd.read_html(request.text)[0]
    stock_list = data.Symbol.apply(lambda x: x.replace('.', '-'))
    #st.write(stock_list)
    if st.sidebar.button("Quick start", help = 'Get the recent 30 days data from SP500'):
        try:
            for i in stock_list:
                fetch._fetch_recent(i, mydb, mycursor)
        except mysql.connector.Error as err:
            st.sidebar.error("Something went wrong: {}".format(err))
    
    analysis_tool = st.sidebar.selectbox('Analysis Tools', ('30日內最大漲幅', '30日內最大跌幅', 'Growth Rate', 'Prediction'))
    
    if analysis_tool == '30日內最大漲幅':
        up_most.objects(mydb)
    
    if analysis_tool == '30日內最大跌幅':
        down_most.objects(mydb)

    #if analysis_tool == 'Growth Rate':
        #growth.objects(ticker, mydb)


if option == 'Explore':
    st.header('Explore')
