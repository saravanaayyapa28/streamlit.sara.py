import streamlit as st
import pandas as pd
import base64  # Added import for base64

# Sample data for available rooms
room_data = {
    'Room Number': [101, 102, 103, 201, 202, 203],
    'Capacity': [2, 2, 2, 4, 4, 4],
    'Price per Night': [100, 120, 150, 200, 250, 300],
    'Availability': [True, True, True, True, True, True]
}

df_rooms = pd.DataFrame(room_data)

# Function to book a room
def book_room(room_number):
    index = df_rooms.index[df_rooms['Room Number'] == room_number].tolist()[0]
    df_rooms.at[index, 'Availability'] = False

# Streamlit app
def main():
    # Set background color
    main_bg = 'C:\Users\DELL\Desktop\Images.jpg'  # Replace with the path to your main background image
    side_bg = 'C:\Users\DELL\Desktop\Images.jpg'  # Replace with the path to your sidebar background image
    main_bg_ext = "jpg"  # Replace with the extension of your main background image
    side_bg_ext = "jpg"  # Replace with the extension of your sidebar background image

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        }}
        .sidebar .sidebar-content {{
            background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Hotel Room Booking System")

    option1 = st.sidebar.selectbox('Select action 1', ['View Rooms', 'Book a Room'])
    option2 = st.sidebar.selectbox('Select action 2', ['Option A', 'Option B'])
    option3 = st.sidebar.selectbox('Select action 3', ['Action X', 'Action Y', 'Action Z'])

    if option1 == 'View Rooms':
        st.subheader('Available Rooms')
        st.dataframe(df_rooms[df_rooms['Availability'] == True])

    elif option1 == 'Book a Room':
        st.subheader('Book a Room')
        selected_room = st.selectbox('Select a Room', df_rooms[df_rooms['Availability'] == True]['Room Number'])
        book_button = st.button('Book Room')

        if book_button:
            book_room(selected_room)
            st.success(f"Room {selected_room} booked successfully!")

    # Additional logic for option2
    if option2 == 'Option A':
        st.write("You selected Option A.")
    elif option2 == 'Option B':
        st.write("You selected Option B.")

    # Additional logic for option3
    if option3 == 'Action X':
        st.write("You selected Action X.")
    elif option3 == 'Action Y':
        st.write("You selected Action Y.")
    elif option3 == 'Action Z':
        st.write("You selected Action Z.")

if __name__ == "__main__":
    main()
