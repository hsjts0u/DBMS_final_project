import streamlit as st
from GoogleNews import GoogleNews

def objects(ticker, mydb):
    mycursor = mydb.cursor()
    
    st.header('Company Description')
    try:
        query = "SELECT logo_url FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.image(result[0][0])
        
        query = "SELECT longName FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.subheader(result[0][0])
        
        query = "SELECT longBusinessSummary FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.write(result[0][0])
        
        st.subheader("Fundamental Data")
        
        query = "SELECT dividendRate FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.write(f"Dividend Rate: {result[0][0]}")
        
        query = "SELECT bookValue FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.write(f"Book Value: {result[0][0]}")
        
        query = "SELECT 52WeekChange FROM info_data WHERE ticker='"+ ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        st.write(f"52 Week Change: {result[0][0]}")
        
        st.header(f'News on {ticker}')
        googlenews = GoogleNews('en')
        googlenews.search(ticker)
        for i in range(min(5, len(googlenews.results()))):
            st.subheader(googlenews.results()[i]['title'])
            st.write(googlenews.results()[i]['link'])
    
    except:
        st.error(f"There is no data on {ticker} in your database, try pressing the update button.")
