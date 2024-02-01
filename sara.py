import streamlit as st
st.write("Haii S.GOWTHAMI GOOD MORING ")
# Import the Streamlit library
import streamlit as st

# Streamlit app begins with the 'st' commands

# Title of the app
st.title("WELCOME TO OUR WORLD Saravan")

# Header
st.header("Enter some information below:")

# Text input box for the user to enter their name
user_name = st.text_input("Enter your name:")

# Slider for selecting age
user_age = st.slider("Select your age:", 0, 100, 25)

# Dropdown for selecting a country
user_country = st.selectbox("Select your country:", ["USA", "Canada", "UK", "Other","INDIA", "AUSTRIALA", "CHITTOOR", "Other"])

# Button to submit the form
if st.button("Submit"):
    # Display the user's information
    st.success(f"Hello, {user_name}! You are {user_age} years old and from {user_country}.")
