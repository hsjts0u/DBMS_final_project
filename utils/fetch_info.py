import yfinance as yf

def _fetch_info(ticker, mydb, mycursor):
    query = "SELECT * FROM info_data WHERE ticker='"+ ticker +"'"
    mycursor.execute(query)
    result = mycursor.fetchall()
    if not result:   
        sql = "INSERT INTO info_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        info_dict = yf.Ticker(ticker).info
        
        val = (ticker, info_dict['dividendRate'], info_dict['beta'], info_dict['52WeekChange'], info_dict['shortName'], info_dict['longName'], info_dict['forwardEps'], info_dict['bookValue'], info_dict['priceToBook'], info_dict['shortRatio'], info_dict['longBusinessSummary'], info_dict['logo_url'])
        
        mycursor.execute(sql, val)
        mydb.commit()

