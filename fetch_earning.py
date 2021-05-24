import yfinance as yf
from pandas import DataFrame

def _fetch_earning(ticker, mydb, mycursor):
    
    sql = "INSERT INTO earning_data (ticker, 2017revenue, 2018revenue, 2019revenue, 2020revenue, 2017earning, 2018earning, 2019earning, 2020earning) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    msft = yf.Ticker(ticker)
    ern = msft.earnings

    val = (
            ticker, 
            ern.loc[2017,'Revenue'].item(), 
            ern.loc[2018,'Revenue'].item(), 
            ern.loc[2019,'Revenue'].item(), 
            ern.loc[2020,'Revenue'].item(), 
            ern.loc[2017,'Earnings'].item(), 
            ern.loc[2018,'Earnings'].item(), 
            ern.loc[2019,'Earnings'].item(), 
            ern.loc[2020,'Earnings'].item()  
          )

    mycursor.execute(sql, val)
    mydb.commit()






