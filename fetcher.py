import yfinance as yf
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your-user",
  password="your-password"
)
