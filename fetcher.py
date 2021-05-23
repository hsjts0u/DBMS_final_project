import yfinance as yf
import mysql.connector
from schema import tables

mydb = None
mycursor = None

for table in tables.tables:
    print(table)
