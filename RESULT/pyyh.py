import psycopg2
import streamlit as st
import pandas as pd
con= psycopg2.connect(
    host ="localhost",
    database="postgres",
    user="postgres",
    password="nikhil2005")
cur=con.cursor()
x=cur.execute ("select * from sem_1 ")
rows = cur.fetchall()
data=pd.DataFrame(rows)
data.columns=["regno","name","sem","pms","s_and_a","c_s","caeg","m_and_a","total","result"]
st.header("WELCOME TO GOVERNAMENT POLITECHNIC CHAMARAJANAGAR ")

button=st.button("GRT RESULT")
if button==True:
    st.table(data)


con.close()



