import requests
import streamlit as st
import pandas as pd
from typing import Dict, Optional, Any

####################################################
# api client
####################################################


# Fetch data from Flask
def fetch_data_from_flask(url: str) -> Dict[str, Any]:
    """
       Fetch data from a Flask endpoint.

       Args:
           url (str): The URL of the Flask endpoint.

       Returns:
           dict: The JSON response data from the Flask endpoint, or an empty dictionary if an error occurs.
       """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return {}

# Send new user data to Flask
def send_user_to_flask(user_name: str, user_phone: str) -> Dict[str, Any]:
    """
        Send user data to a Flask endpoint.

        Args:
            user_name (str): The name of the user.
            user_phone (str): The phone number of the user.

        Returns:
            dict: The JSON response data from the Flask endpoint, or an empty dictionary if an error occurs.
        """
    try:
        response = requests.post(st.secrets["api_calls"]["ADD_USER"], json={"user_name": user_name, "user_phone": user_phone})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error sending data to Flask: {e}")
        return {}


def fetch_product_data() -> pd.DataFrame:
    # Fetch initial data from Flask
    product_data = fetch_data_from_flask(st.secrets["api_calls"]["GET_PRODUCT_DF"])

    # Initialize DataFrames from fetched data
    df_product = pd.DataFrame(product_data.get('products', []))

    return df_product


def fetch_user_data() -> pd.DataFrame:
    # Fetch initial data from Flask
    users_data = fetch_data_from_flask(st.secrets["api_calls"]["GET_USERS_DF"])

    # Initialize DataFrames from fetched data
    df_users = pd.DataFrame(users_data.get('users', []))

    return df_users


def fetch_model_data() -> pd.DataFrame:
    # Fetch initial data from Flask
    models_data = fetch_data_from_flask(st.secrets["api_calls"]["GET_MODEL_DF"])

    # Initialize DataFrames from fetched data
    df_models = pd.DataFrame(models_data.get('models', []))

    return df_models


# Additional function to remove a user from the database
def remove_user_from_database(user_to_remove: str) -> Optional[Dict[str, Any]]:
    user_id_to_remove = user_to_remove.split(";")[0]
    try:
        response = requests.post(st.secrets["api_calls"]["REMOVE_USER"], json={"user_id": str(user_id_to_remove)})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error removing user: {e}")
    return None

# Additional function to check manager credentials
def check_manager(name: str, password: str) -> bool:
    try:
        response = requests.post(st.secrets["api_calls"]["CHECK_MANAGER"], json={"manager_name": name, "manager_password": password})
        manager_access = response.json().get('manager_access', False)
        return manager_access
    except requests.RequestException as e:
        st.error(f"Error checking manager credentials: {e}")
    return False

# Additional function to send a WhatsApp message
def send_whatsapp_message(user_to_message: str) -> Optional[Dict[str, Any]]:
    user_number_to_message = user_to_message.split(";")[2]
    user_name = user_to_message.split(";")[1]
    try:
        response = requests.post(st.secrets["api_calls"]["MESSAGE_USER"], json={"user_number": str(user_number_to_message), "user_name": str(user_name)})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error sending WhatsApp message: {e}")
    return None