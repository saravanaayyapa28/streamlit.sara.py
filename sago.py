import streamlit as st

def main():
    search_query = st.text_input('Search Famous Places')
    search_submit = st.button('Sagoooo')

    if search_submit:
        # Perform actions when the submit button is clicked
        pass

    st.title("Welcome To Hotel Reservation Prediction ")

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    # Add image
    st.image("computer-science.jpg", use_column_width=True)# Replace "images (1).jpg" with the path to your image file
    
    option1 = st.sidebar.selectbox('Select The Country ', ['India', 'USA', 'Singapore'])
    option2 = st.sidebar.selectbox('Select The city', ['Delhi','Mumbai','Bangalore',"Kerala",'Kolkata','Chennai','Hyderabad','Pune','Ahmedabad','Jaipur','Surat','Lucknow','Kanpur','Nagpur','Indore','Thane','Bhopal','Visakhapatnam','Pimpri-Chinchwad','Patna','Vadodara'])
    option6 = st.sidebar.selectbox('Select The Mode ', ['Online', 'Offline'])
    option7 = st.sidebar.selectbox('Select The District', ['Alleppey','Goa','Gokarna','Ooty','Sikkim','Amritsar','Leh','Rameshwaram','Munnar'])
    
    if search_query:
        filtered_cities = [city for city in ['Delhi','Mumbai','Bangalore',"Kerala",'Kolkata','Chennai','Hyderabad','Pune','Ahmedabad','Jaipur','Surat','Lucknow','Kanpur','Nagpur','Indore','Thane','Bhopal','Visakhapatnam','Pimpri-Chinchwad','Patna','Vadodara'] if search_query.lower() in city.lower()]
        option2 = st.sidebar.selectbox('Select The City', filtered_cities)

    st.sidebar.subheader("Additional Options")
    option3 = st.sidebar.checkbox('Include Breakfast')
    option4 = st.sidebar.slider('Number of Nights', min_value=1, max_value=30, step=1, value=5)
    option5 = st.sidebar.selectbox('Select Year', list(range(2020, 2030)), index=5)

    submit_button = st.sidebar.button("Predict")

    if submit_button:
        # Additional logic for option1
        if option1 == 'India':
            st.write("You selected  Country India.")
        elif option1 == 'USA':
            st.write("You selected USA.")
        elif option1 == 'Singapore':
            st.write("You selected Singapore.")

        # Additional logic for option2
        st.write(f"You selected State {option2}.")

        # Additional logic for option6
        st.write (f"You selected Mode {option6}.")

        # Additional logic for option2
        st.write(f"You selected  District {option7}.")

        # Additional logic for option3 and option4
        if option3:
            st.write("Breakfast included.")
        else:
            st.write("Breakfast not included.")

        st.write(f"Number of nights: {option4}.")

        # Additional logic for option5
        if option5 % 2 == 0:
            st.warning(f"You selected year {option5}. In this year, online Reservation is high.")
        else:
            st.warning(f"You selected year {option5}. In this year, offline Reservation is High.")

       
if __name__ == "__main__":
    main()
