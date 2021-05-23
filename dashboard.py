import streamlit as st
import requests
import json
# import fetcher
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import mysql.connector

# MySQL connection objects
mydb = None
mycursor = None

# Streamlit Interface

st.title("Stock Analysis")

st.sidebar.title("Options")

option = st.sidebar.selectbox('Action', ('Start Here', 'B', 'C'))

st.header(option)

if option == 'Start Here':
    #left_column, right_column = st.beta_columns(2)
    
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
                database=mydb
            )
            st.write("Connection Succesful !")
        except:
            st.write("Your database does not exist, proceed to create a new database by pressing ' Create new database! '")
    
    if st.button("Create new database !"):
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            mycursor = mydb.cursor()
            mycursor.execute(f"CREATE DATABASE {dbname}")
        except:
            st.write("Oops! It seems that we are unable to connect you to MySQL.")

if option == 'B':
    pass

if option == 'C':
    pass
