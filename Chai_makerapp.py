import streamlit as st

st.title("chai Maker App")
if st.button("click here to make a tea"):
    st.success("your tea is ready")
add_masala = st.checkbox("add masala")
if add_masala:
    st.write("masala added to your tea")
tea_type = st.radio("select your tea type", ["green tea", "black tea", "herbal tea", "oolong tea ","white tea "," cold tea"])
tea_contry_based = st.selectbox("select your contry ", [" indian ", "America ", "dubai", "pakistan ","maleshiya "," maaldives "])
st.write("you have selected :", tea_type)
st.write("you have selected :", tea_contry_based)
flavor = st.multiselect("select your flavor", ["mint", "ginger", "cardamom", "cinnamon", "clove", "pepper","tulsi","lemon","honey"])
st.write("you have selected :", flavor)
sugar = st.slider("select sugar level(spoon)", 0,10,5)
st.write(f"you have selected {sugar} spoons of sugar")
cups = st.number_input("enter number of cups",  min_value=2, max_value=10,step=1)
st.write(f" slected sugar lavel is {sugar} spoons and number of cups is {cups}")

name = st.text_input("enter your name ")
if name:
    st.write(f"hello ,{name} welcome to chai maker app ")
Area_Name = st.text_area("enter your name ")
if Area_Name:
    st.write(f"hello  ,{Area_Name} welcome to chai maker app ")

dob= st.date_input("enter your date of ")
if dob:
    st.write(f"your date of brith is {dob}")

