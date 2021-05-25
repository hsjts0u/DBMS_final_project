import yfinance as yf

def _fetch_financial(ticker, mydb, mycursor):
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
        
