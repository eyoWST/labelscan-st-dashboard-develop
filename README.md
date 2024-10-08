# LabelScan Streamlit Dashboard

## Overview

LabelScan is a Streamlit-based dashboard application designed to manage users and view data related to registered products and unique models. The application interfaces with a Flask backend to fetch and manipulate data.

## Features

- **User Management**: Add and remove users from the database.
- **Data Views**: View data related to registered products and unique models.
- **Login System**: Secure access to the dashboard with manager credentials.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/labelscan-st-db-dashboard.git
   cd labelscan-st-db-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Streamlit secrets**:
   - Create a `.streamlit/secrets.toml` file.
   - Add your API endpoints and other secrets in the following format:
     ```toml
     [api_calls]
     ADD_USER = "http://your-flask-api/add_user"
     GET_USERS_DF = "http://your-flask-api/get_users"
     GET_PRODUCT_DF = "http://your-flask-api/get_products"
     GET_MODEL_DF = "http://your-flask-api/get_models"
     REMOVE_USER = "http://your-flask-api/remove_user"
     CHECK_MANAGER = "http://your-flask-api/check_manager"
     MESSAGE_USER = "http://your-flask-api/message_user"
     ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run backend_gui.py
   ```

2. **Access the dashboard**:
   - Open your web browser and go to `http://localhost:8501`.

## Code Structure

- [`backend_gui.py`](backend_gui.py): Main application file for the Streamlit dashboard.
- [`welcome_page.py`](welcome_page.py): Handles the login page and user authentication.
- [`api_client.py`](api_client.py): Contains functions to interact with the Flask backend.
