import yfinance as yf
import datetime


def _fetch_history(ticker, mydb, mycursor):
    mycursor = mydb.cursor()
    sql = "INSERT INTO history_stock_data VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dic = {} 
    
    symb = yf.Ticker(ticker).history(start = "2000-01-03", end = datetime.date.today())
    
    for i in range(len(symb.index)):
        temp = symb.index[i].strftime('%Y-%m-%d')
        query = "SELECT * FROM history_stock_data WHERE ticker='"+ticker+"' AND day='"+temp+"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if not result :
            val = ( ticker, temp, symb['Open'][i].item(), symb['High'][i].item(), symb['Low'][i].item(), symb['Close'][i].item(), symb['Volume'][i].item() )
            mycursor.execute(sql, val)
            mydb.commit()

def _fetch_recent(ticker, mydb, mycursor):  
    mycursor = mydb.cursor()
    sql = "INSERT INTO SP500_stock_data VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dic = {}
    
    symb = yf.Ticker(ticker).history(start = datetime.date.today() - datetime.timedelta(days=30), end = datetime.date.today())
    
    for i in range(len(symb.index)):
        temp = symb.index[i].strftime('%Y-%m-%d')
        query = "SELECT * FROM SP500_stock_data WHERE ticker='"+ticker+"' AND day='"+temp+"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if not result :
            val = ( ticker, temp, symb['Open'][i].item(), symb['High'][i].item(), symb['Low'][i].item(), symb['Close'][i].item(), symb['Volume'][i].item() )
            mycursor.execute(sql, val)
            mydb.commit()
    
def _fetch_info(ticker, mydb, mycursor):
    mycursor = mydb.cursor()
    query = "SELECT * FROM info_data WHERE ticker='"+ ticker +"'"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    info_dict = yf.Ticker(ticker).info
    
    if not result:   
        sql = "INSERT INTO info_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        val = (ticker, info_dict['dividendRate'], info_dict['beta'], info_dict['52WeekChange'], info_dict['shortName'],info_dict['longName'],
        info_dict['forwardEps'], info_dict['bookValue'], info_dict['priceToBook'], info_dict['shortRatio'], info_dict['longBusinessSummary'],
        info_dict['logo_url'])
        
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        sql = """
                UPDATE info_data 
                SET 
                    dividendRate = %s, beta = %s, 52WeekChange = %s, 
                    shortName = %s, longName = %s, forwardEps = %s, 
                    bookValue = %s, priceToBook = %s, shortRatio = %s,
                    longBusinessSummary = %s, logo_url = %s
                WHERE ticker = %s
              """
        
        val = (info_dict['dividendRate'], info_dict['beta'], info_dict['52WeekChange'], info_dict['shortName'],info_dict['longName'],
        info_dict['forwardEps'], info_dict['bookValue'], info_dict['priceToBook'], info_dict['shortRatio'], info_dict['longBusinessSummary'],
        info_dict['logo_url'], ticker)
        
        mycursor.execute(sql, val)
        mydb.commit()
        

def _fetch_financial(ticker, mydb, mycursor):
    mycursor = mydb.cursor()
    sql = "INSERT INTO financial VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    dic = {} 
    mycursor = mydb.cursor()
    
    symb = yf.Ticker(ticker)
    Fin = ('Research Development', 'Net Income', 'Gross Profit', 'Ebit', 'Operating Income', 'Interest Expense')
    
    for i in Fin:
        dic[i] = symb.financials.loc[i]
    
    for i in range(len(dic['Research Development'])):
        temp = dic['Research Development'].index[i].strftime('%Y-%m-%d')
        query = "SELECT * FROM financial WHERE ticker='"+ ticker +"' AND date='" + temp + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        
        if not result :
            val = ( ticker, temp, dic['Research Development'][i], dic['Net Income'][i], dic['Gross Profit'][i], dic['Ebit'][i], dic['Operating Income'][i], dic['Interest Expense'][i] )
            mycursor.execute(sql, val)
            mydb.commit()


def _fetch_earning(ticker, mydb, mycursor):
    mycursor = mydb.cursor()
    sql = "INSERT INTO earning_data (ticker, year, earning) VALUES (%s, %s, %s)"
    msft = yf.Ticker(ticker)
    ern = msft.earnings
    for i in range(len(ern.index)):
        query = "SELECT * FROM earning_data WHERE ticker= '" + ticker + "' AND year='" + str(ern.index[i].item()) + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()

        if not result:
            val = ( ticker, ern.index[i].item(), ern.loc[ern.index[i],'Earnings'].item() )
            mycursor.execute(sql, val)
            mydb.commit()
            


def _fetch_revenue(ticker, mydb, mycursor):
    mycursor = mydb.cursor()
    sql = "INSERT INTO revenue_data (ticker, year, revenue) VALUES (%s, %s, %s)"
    msft = yf.Ticker(ticker)
    ern = msft.earnings

    for i in range(len(ern.index)):
        query = "SELECT * FROM revenue_data WHERE ticker= '" + ticker + "' AND year='" + str(ern.index[i].item()) + "'"
        mycursor.execute(query)
        result = mycursor.fetchall()

        if not result:
            val = ( ticker, ern.index[i].item(), ern.loc[ern.index[i],'Revenue'].item() )
            mycursor.execute(sql, val)
            mydb.commit()
            
