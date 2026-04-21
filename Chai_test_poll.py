import streamlit as st

st.title("Chai Taste Poll")
st.image("https://b.zmtcdn.com/data/pictures/3/19868963/a88abfe458c5ea4f0da7801ae5fca721.jpeg?fit=around|960:500&crop=960:500;*,*", width=500 , caption="Welcome to Chai Taste Poll")


col1, col2 = st.columns(2)    

with col1:
    st.header("Masala Chai")
    st.image("https://t3.ftcdn.net/jpg/12/54/00/18/240_F_1254001879_wMdQEYuwSq8l8IB5j4aemul9fNElintv.jpg ", width=200 )
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image(" https://as1.ftcdn.net/v2/jpg/18/68/93/14/1000_F_1868931444_v0mx4Zjm7TJDGwhuLHVHYeV3d887V7yV.jpg", width=200 )
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")


name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "kesar", "Adrak","Tulsi", "Elaichi", "Lemon", "Ginger", "Green", "Black"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("Show Chai Making INstructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
 """)
    
st.markdown('# Welcome to Chai App')
st.markdown('> Blockquote ')
st.markdown('**Bold Text**')
# st.markdown('~~Strikethough~~')

st.markdown('''- List Item 1)
- List Item 2
- List Item 3
''')
rate =st.slider("Rate your chai experience", 0, 10, 5)
st.write(f"Your rating is {rate} out of 10")

location = st.text_input ( "enter your location ")
if location:
    st.write(f"your location is {location}")

contry= st.sidebar.selectbox("select your contry ", [" india ", "America ", "dubai", "pakistan ","maleshiya "," maaldives ", "other contry"], index=0)
st.write(f"you have selected {contry} as your contry")

