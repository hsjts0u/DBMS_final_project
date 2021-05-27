import streamlit as st
import pandas as pd

def objects(mydb):
    mycursor = mydb.cursor()
    sql_cat = "SELECT DISTINCT category_name FROM stock_list"
    mycursor.execute(sql_cat)
    Cat = mycursor.fetchall()
    options = st.multiselect(
     'Select Country',
     ['Canada','India','China','South Korea','Hong Kong','Malaysia','France','Taiwan','Germany', 'United Kingdom',
      'Mexico','Spain','Sweden','Indonesia','Australia','Thailand','Switzerland','Ireland','Singapore','USA','Italy','Argentina',
      'Greece','Denmark','Netherlands','Brazil','New Zealand','Venezuela','Austria','Belgium','Israel','Qatar','Russia','Norway',
      'Finland','Turkey','Portugal','Lithuania','Estonia','Latvia','Icelandreen'],
     ['Taiwan']
     )
    c = [ i[0] for i in Cat]
    print(c)
    options_category = st.multiselect('Select Category', c)

     
    if not options:
        pass
    else:
        query = "SELECT * FROM stock_list WHERE country='"+options[0]+"'"
        for i in range(len(options)-1):
            query = query + " OR country='" + options[i+1]+"'"
        st.write(query)
        mycursor.execute(query)
        result = mycursor.fetchall()
       

        DF = pd.DataFrame(result, columns=['Ticker','Name' ,'Exchange','Category','Country'])
        DF.reset_index(inplace=False)
        DF.set_index("Country", inplace=True)
        st.table(DF)
