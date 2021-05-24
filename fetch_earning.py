import yfinance as yf
from pandas import DataFrame

def _fetch_earning(ticker, mydb, mycursor):

    sql = "INSERT INTO earning_data (ticker, year, earning) VALUES (%s, %s, %s)"

    msft = yf.Ticker(ticker)
    ern = msft.earnings


    val = [   (ticker, ern.index[0].item(), ern.loc[ern.index[0],'Earnings'].item()),
                (ticker, ern.index[1].item(), ern.loc[ern.index[1],'Earnings'].item()),
                (ticker, ern.index[2].item(), ern.loc[ern.index[2],'Earnings'].item()),
                (ticker, ern.index[3].item(), ern.loc[ern.index[3],'Earnings'].item())
            ]

    mycursor.executemany(sql, val)
    mydb.commit()






