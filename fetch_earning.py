import mysql.connector
import yfinance as yf
import json
from pandas import DataFrame

mydb = mysql.connector.connect(
  host="localhost",
  user="tcu",
  password="9453",
  database = "final"
  
)

mycursor = mydb.cursor()
sql = "INSERT INTO earning_data (ticker, 2017revenue, 2018revenue, 2019revenue, 2020revenue, 2017earning, 2018earning, 2019earning, 2020earning) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


msft = yf.Ticker("MSFT")
ern = msft.earnings
print(ern.loc[2017,'Revenue'])
print(type(ern.loc[2017,'Earnings'].item()))

val = ('MSFT', ern.loc[2017,'Revenue'].item(), ern.loc[2018,'Revenue'].item(), ern.loc[2019,'Revenue'].item(), ern.loc[2020,'Revenue'].item(), ern.loc[2017,'Earnings'].item(), ern.loc[2018,'Earnings'].item(), ern.loc[2019,'Earnings'].item(), ern.loc[2020,'Earnings'].item()  )
	
	
	
	
mycursor.execute(sql, val)

mydb.commit()






