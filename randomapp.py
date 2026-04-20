import streamlit as st

st.title("My First Random practics  App 😍")
st.header("ALL about randoms  keywords  in this projects and also about data science projects")
st.subheader("This is a subheader")
st.text("This is some text")
st.markdown("this topics for a data science projects ")
st.markdown(" my name is  **Ramesh**")
# st.markdown("This is some *markdown*")
st.markdown("This is some ***Rameshrajput***")
st.markdown(" Google  [link](https://www.google.com)")
st.markdown(" gmai.com [link](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox)")
st.markdown("   chatgpt.com  [link](https://chatgpt.com/c/69e6206b-980c-83a5-a4e0-ef43e1ef1b8d)")

store= st.selectbox("your fav products :", ["skin care","helth care"," sexual products "," kitechen products "," home products "," gernal store "])
st.write("you have selected :",store)
st.success(" yor order is placed  successfully")
st.link_button("click here to visit google",url="https://www.flipkart.com/")


