import streamlit as st

applicants = []

# Adding background color and image using CSS
background_style = """
    <style>
        body {
            background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), url('Data-Science-focuses-on-algorithms.jpg') center center fixed; /* Replace 'Data-Science-focuses-on-algorithms.jpg' with the URL or path to your image */
            background-size: cover;
            background-color: #f4f4f4; /* Light gray background color */
        }
    </style>
"""

st.markdown(background_style, unsafe_allow_html=True)

# Rest of your Streamlit app code
st.write("WELCOME TO TAMILNADU TOURISM ")
# Title of the app
st.title("WELCOME TO ONLINE HOTEL RESERVATION SYSTEM")

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

# Display the list of applicants
st.header("List of Applicants:")
for idx, applicant in enumerate(applicants, start=1):
    st.write(f"{idx}. {applicant['name']} - Age: {applicant['age']}, Country: {applicant['country']}")


