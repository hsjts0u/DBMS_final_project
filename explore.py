import streamlit as st
import pandas as pd

def objects(mydb):
    mycursor = mydb.cursor()
    sql_cat = "SELECT DISTINCT category_name FROM stock_list ORDER BY category_name ASC"
    sql_exchange = "SELECT DISTINCT exchange FROM stock_list ORDER BY exchange ASC"
    sql_country = "SELECT DISTINCT country FROM stock_list ORDER BY country ASC"
    mycursor.execute(sql_cat)
    Cat = mycursor.fetchall()
    mycursor.execute(sql_exchange)
    Exc = mycursor.fetchall()
    mycursor.execute(sql_country)
    Coun = mycursor.fetchall()
    c = [ i[0] for i in Cat]
    e = [ i[0] for i in Exc]
    co = [ i[0] for i in Coun]
    options_country = st.multiselect('Select Country', co, ['Taiwan'])
    options_category = st.multiselect('Select Category', c)
    options_exchange = st.multiselect('Select Exchange', e)
  

    cat_name = ['category_name' for i in range(len(options_category))]
    cou_name = ['country' for i in range(len(options_country))]
    exc_name = ['exchange' for i in range(len(options_exchange))]
    options = list(zip(cou_name, options_country)) + list(zip(cat_name, options_category)) + list(zip(exc_name, options_exchange))
    
    orderby = st.radio("Data is ordered by ", ('Country', 'Category', 'Exchange'))
    if orderby == 'Country':
        order = 'country'
    elif orderby == 'Category':
        order = 'category_name'
    else:
        order = 'exchange'

    if not options:
        pass
    else:
        x = True
        query = "SELECT * FROM stock_list"
        for i in range(len(options)):
            if x == True:
                x = False
                query = query + " WHERE ("+ options[i][0] + "='" + options[i][1] + "'"
            
            elif options[i-1][0] != options[i][0]:
                query = query + ") AND ("+ options[i][0] + "='" + options[i][1] + "'"
            
            else:
                query = query + " OR "+ options[i][0] +"='" + options[i][1]+"'"

        query = query + ") ORDER BY " + order + " ASC" 
        mycursor.execute(query)
        result = mycursor.fetchall()
       
        DFC = pd.DataFrame(result, columns=['Ticker','Name' ,'Exchange','Category','Country'])
        DFC.reset_index(inplace=False)

        if orderby == 'Country':
            DFC.set_index("Country", inplace=True)
        elif orderby == 'Exchange':
            DFC.set_index("Exchange", inplace=True)
        else:
            DFC.set_index("Category", inplace=True)
        
        st.table(DFC)
