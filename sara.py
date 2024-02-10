import streamlit as st
import pandas as pd

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
    st.title("Hotel Room Booking System")

    option = st.sidebar.selectbox('Select an action', ['View Rooms', 'Book a Room'])

    if option == 'View Rooms':
        st.subheader('Available Rooms')
        st.dataframe(df_rooms[df_rooms['Availability'] == True])

    elif option == 'Book a Room':
        st.subheader('Book a Room')
        selected_room = st.selectbox('Select a Room', df_rooms[df_rooms['Availability'] == True]['Room Number'])
        book_button = st.button('Book Room')

        if book_button:
            book_room(selected_room)
            st.success(f"Room {selected_room} booked successfully!")

if __name__ == "__main__":
    main()
