import streamlit as st

applicants = []

st.write("Haii !!!!!")
# Title of the app
st.title("WELCOME TO INDIAN TOURISM")

# Header
st.header("Enter some information below:")

# Text input box for the user to enter their surname
user_surname = st.text_input("Enter your Surname:")

# Text input box for the user to enter their middle name
user_middle_name = st.text_input("Enter your Middle Name:")

# Slider for selecting age
user_age = st.slider("Select your age:", 0, 100, 25)

# Dropdown for selecting a country
user_country = st.selectbox("Select your country:", ["USA", "Canada", "UK", "Other", "INDIA", "AUSTRALIA", "CHITTOOR", "Other"])

# Button to submit the form
if st.button("Submit"):
    # Display the user's information
    st.success(f"Hello, {user_surname} {user_middle_name}! You are {user_age} years old and from {user_country}.")

    # Add the applicant to the list
    applicant = {'surname': user_surname, 'middle_name': user_middle_name, 'age': user_age, 'country': user_country}
    applicants.append(applicant)
