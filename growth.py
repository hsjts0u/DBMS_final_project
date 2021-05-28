import streamlit as st
import plotly.graph_objects as go
import pandas as pd


def objects(ticker, mydb):
    mycursor = mydb.cursor()
    st.header('Growth Rate')

    st.subheader('Earnings and Revenue')
    query = "SELECT year, earning FROM earning_data WHERE ticker='"+ticker+"' ORDER BY year DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    df = pd.DataFrame(result, columns=['year','earning'])
    
    fig = go.Figure()
    df.year = pd.to_datetime(df.year, format='%Y')
    fig.update_layout(title='Earnings')
    fig.add_trace(go.Bar(
        x=df["year"], y=df["earning"],
        xperiod="M12",
        xperiodalignment="middle"
    ))
    fig.update_xaxes(showgrid=True, ticklabelmode="period")
    st.plotly_chart(fig)
    
    query = "SELECT year, revenue FROM revenue_data WHERE ticker='"+ticker+"' ORDER BY year DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    df = pd.DataFrame(result, columns=['year','revenue'])
    
    fig = go.Figure()
    df.year = pd.to_datetime(df.year, format='%Y')
    fig.update_layout(title='Revenue')
    fig.add_trace(go.Bar(
        x=df["year"], y=df["revenue"],
        xperiod="M12",
        xperiodalignment="middle"
    ))
    fig.update_xaxes(showgrid=True, ticklabelmode="period")
    st.plotly_chart(fig)
    
    query = """
            SELECT e.year, earning, revenue
            FROM
                (
                    SELECT * 
                    FROM earning_data
                    WHERE ticker = %s
                ) e,
                (
                    SELECT *
                    FROM revenue_data
                    WHERE ticker = %s
                ) r
            WHERE e.year = r.year
            ORDER BY e.year DESC
            """
    val = (ticker, ticker)
    mycursor.execute(query, val)
    result = mycursor.fetchall()
    df = pd.DataFrame(result, columns=['year', 'earning','revenue'])
    df.set_index("year", inplace=True)
    st.table(df)
    
    st.subheader("Growth Indices")
    # most recent stock price close / future eps info
    query = """
            SELECT c.close / f.forwardEps
            FROM 
                (
                    SELECT close 
                    FROM history_stock_data
                    WHERE ticker = %s
                    ORDER BY day DESC
                    LIMIT 1
                ) c,
                (
                    SELECT forwardEps
                    FROM info_data
                    WHERE ticker = %s
                ) f
            """
    val = (ticker, ticker)
    mycursor.execute(query, val)
    result = mycursor.fetchall()
    pe = result[0][0]
    st.write(f"P/E ratio: {round(result[0][0], 2)}")
    
    query = """
            SELECT net_income
            FROM financial
            WHERE ticker = '"""+ ticker +"""'
            ORDER BY date DESC
            LIMIT 2
            """
    mycursor.execute(query)
    result = mycursor.fetchall()
    st.write(f'FPEG ratio: {max(0, round(pe/(result[0][0]/result[1][0] - 1), 2))}')
    
    query = "SELECT priceToBook FROM info_data WHERE ticker='"+ticker+"'"
    mycursor.execute(query)
    result = mycursor.fetchall()
    st.write(f"Book to Price ratio: {round(1/result[0][0], 2)}")
    
