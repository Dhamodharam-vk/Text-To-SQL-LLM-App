from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):    
    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content([prompt[0], question])
    return response.text


# Function to retrieve query from the sql database
def read_sql_query(sql, db):
    conn=sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    
    for row in rows:
        print(row)
    return rows    

prompt=[
    """
    You are an expert in converting English question to SQL Query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor Example 1 - How many entries of records are present?,
    the sql command will something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 -  Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    WHERE CLASS="Data Science";
    also the sql code should not have ``` in begining or end and sql word in the output
    """
]    
    
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response=get_gemini_response(question, prompt)
    print(response)
    data=read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)

     