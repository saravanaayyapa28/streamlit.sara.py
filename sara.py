import streamlit as st

applicants = []

# Adding background color using CSS
background_color = """
    <style>
        body {
            background-color: #f4f4f4; /* Light gray background color */
        }
    </style>
"""

st.markdown(background_color, unsafe_allow_html=True)

# Rest of your Streamlit app code
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
user_country = st.selectbox("Select your country:", ["USA", "Canada", "UK","INDIA", "AUSTRIALA", "Other"])

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
