import streamlit as st

applicants = []

st.write("Haii GOOD MORNING ")
# Title of the app
st.title("WELCOME TO OUR WORLD")

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

    # Add the applicant to the list
    applicant = {'name': user_name, 'age': user_age, 'country': user_country}
    applicants.append(applicant)
