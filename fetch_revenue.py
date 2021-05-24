import yfinance as yf
from pandas import DataFrame

def _fetch_revenue(ticker, mydb, mycursor):
    sql = "INSERT INTO revenue_data (ticker, year, revenue) VALUES (%s, %s, %s)"

    msft = yf.Ticker(ticker)
    ern = msft.earnings


    val = [   (ticker, ern.index[0].item(), ern.loc[ern.index[0],'Revenue'].item()),
                (ticker, ern.index[1].item(), ern.loc[ern.index[1],'Revenue'].item()),
                (ticker, ern.index[2].item(), ern.loc[ern.index[2],'Revenue'].item()),
                (ticker, ern.index[3].item(), ern.loc[ern.index[3],'Revenue'].item())
            ]

    mycursor.executemany(sql, val)
    mydb.commit()






