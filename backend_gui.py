import pandas as pd
import streamlit as st
import api_client
import welcome_page

# Initialize session variables
def initialize_session_variables():
    if 'accepted_to_database' not in st.session_state:
        st.session_state.accepted_to_database = False

####################################################
# backend gui
####################################################
def app():
    # Display the banner image at the top of the app
    # st.image('assets/Fnac VdB logo.png', width=100)

    if not st.session_state.accepted_to_database:
        welcome_page.welcome_page()
    else:
        st.title("Dashboard")
        tab1, tab2 = st.tabs(["User Management", "Data Views"])
        
        with tab1:
            st.subheader("Add new user")
            with st.form(key='user_form'):
                user_name = st.text_input("User Name")
                user_phone = st.text_input("Phone Number")
                submit_button = st.form_submit_button(label='Add User')
                if submit_button:
                    response = api_client.send_user_to_flask(user_name, user_phone)
                    if response:
                        st.success(response.get("message", "User added successfully"))
            
            # Remove existing user from the Users DataFrame
            st.subheader("Remove existing user")
            user_data = api_client.fetch_user_data()  # Fetch the user data

            # Assuming user_data is a DataFrame
            if not user_data.empty:
                # Create a list of strings combining user name and phone number
                user_list = [f"{row['user_name']} ({row['user_phone']})" for index, row in user_data.iterrows()]
                with st.form(key='remove_user_form'):
                    user_to_remove = st.selectbox("Select User to Remove", user_list)
                    remove_button = st.form_submit_button(label='Remove User')
                    if remove_button:
                        # Extract the user name from the selection for removal
                        selected_user_name = user_to_remove.split(" (")[0]  # Assuming the format "Name (Phone)"
                        response = api_client.remove_user(selected_user_name)  # Assuming this function removes the user by name
                        if response:
                            st.success(response.get("message", "User removed successfully"))
                        st.experimental_rerun()
            else:
                st.error("No user data available.")
            
            user_count = len(user_data)  # Count the number of users
            st.write(f"User count: {user_count}/10")  # Display the user count
            
            # Display the Users DataFrame at the bottom of the User Management tab
            df_users = api_client.fetch_user_data()
            if df_users.empty:
                st.error("Failed to fetch user data.")
            else:
                st.write("Users DataFrame:")
                st.dataframe(df_users)

        with tab2:
            options = ['Registered Products', 'Unique Models (Beta)']  # Removed 'Users' from options
            selected_dataframe = st.selectbox('Choose a DataFrame to view:', options)
            
            if selected_dataframe == 'Registered Products':
                df_product = api_client.fetch_product_data()
                if df_product.empty:
                    st.error("Failed to fetch product data.")
                else:
                    st.write("Products DataFrame:")
                    st.dataframe(df_product)
            
            elif selected_dataframe == 'Unique Models (Beta)':
                df_models = api_client.fetch_model_data()
                if df_models.empty:
                    st.error("Failed to fetch model data.")
                else:
                    st.write("Models DataFrame:")
                    st.dataframe(df_models)
            
            if st.button('Check for New Data'):
                st.experimental_rerun()

if __name__ == "__main__":
    initialize_session_variables()
    app()


