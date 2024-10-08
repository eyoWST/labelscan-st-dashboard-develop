import streamlit as st
import time
import api_client

def welcome_page():
    # Welcome page with terms and conditions
    # st.title("Welcome to the App!")

    # Show input fields for user details once terms are accepted
    st.subheader("Login to Access the Dashboard")
    st.session_state.manager_name = st.text_input("Name")
    st.session_state.manager_password = st.text_input("Password")

    # Button to submit the user details
    if st.button("Submit Credentials"):
        # Ensure both fields are filled out
        if st.session_state.manager_name and st.session_state.manager_password:
            # Check if the user exists in the system
            user_exists = api_client.check_manager(st.session_state.manager_name, st.session_state.manager_password)
            if user_exists:
                st.success("Login successful! Redirecting to the dashboard...")
                # Wait for 2 seconds before processing the response
                time.sleep(2)
                # Set the session state to move to the next page
                st.session_state.accepted_to_database = True
                st.rerun()  # Refresh the app to navigate to the next page
            else:
                st.write("Access denied. Please check your credentials or contact your administrator for access.")
        else:
            # Show an error if fields are incomplete
            st.error("Both name and password fields must be completed.")