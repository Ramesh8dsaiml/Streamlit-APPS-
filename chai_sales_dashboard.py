import streamlit as st 
import pandas as pd 
st.title("chai sales  dashboard")
files = st.file_uploader("upload your files here", type=["csv","xlsx","json","txt","pdf"],accept_multiple_files= True )
df=None

if files:
     for file in files:
          st.write(f"file name: {file.name}")
          st.write(f"file type: {file.type}")
          file.seek(0)

          if file.type == "text/csv":
               df = pd.read_csv(file)
               st.dataframe(df)
          elif file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
               df = pd.read_excel(file)
               st.dataframe(df)
          elif file.type == "application/json":
               df = pd.read_json(file)
               st.dataframe(df)
          elif file.type == "text/plain":
               text = file.read().decode("utf-8")
               st.text(text)
          elif file.type == "application/pdf":
               st.write("PDF file uploaded successfully")


if files:
     file.seek(0)
     df=pd.read_csv(files[0])
     st.write(df)
     st.subheader("data preview")
     st.dataframe(df)
     # st.dataframe(df.head())
if files:
     st.subheader("summary stats")
     st.write(df.describe())

if files:
     cities =df["City"].unique()
     selected_city=st.selectbox("filter by cities",cities)
     filtered_data = df[df["City"]==selected_city]
     st.dataframe(filtered_data)
if files:
     cities= df["Price_per_Cup"].unique()
     selected_city=st.selectbox("filter by price",cities)
     filtered_data = df[df["Price_per_Cup"]==selected_city]
     st.dataframe(filtered_data)
     