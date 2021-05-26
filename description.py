import streamlit as st
import plotly.graph_objects as go
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
        
        st.subheader("Safety Index")
        query = "SELECT dividendRate / beta FROM info_data WHERE ticker='" + ticker +"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        si = 0
        if result[0][0] > 0:
            si = max(si, result[0][0])
        
        fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = round(si, 2),
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Safety Index"},
                        gauge = {'axis': {'range': [0, 24]},
                                 'bar': {'color': "white"},
                                 'steps' : [
                                    {'range': [0, 8], 'color': "#e3361b"}, 
                                    {'range': [8, 16], 'color': "#f5e556"}, 
                                    {'range': [16, 24], 'color': "#45c449"}]} 
                        ))
        st.plotly_chart(fig)
        
        st.header(f'News on {ticker}')
        googlenews = GoogleNews('en')
        googlenews.search(ticker)
        for i in range(min(5, len(googlenews.results()))):
            st.subheader(googlenews.results()[i]['title'])
            st.write(googlenews.results()[i]['link'])
    
    except:
        st.error(f"There is no data on {ticker} in your database, try pressing the update button.")
