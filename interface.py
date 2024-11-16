import streamlit as st
import requests

# Set up the Streamlit app
st.title("Player Price Prediction")

# User inputs
appearance = st.number_input("Appearance")
minutes_played = st.number_input("Minutes Played")
award = st.number_input("Award")
highest_value = st.number_input("Highest Value")

# Prediction button
if st.button("Predict Price"):
    # API request URL
    url = "https://lab7-app-1.onrender.com/predict"
    
    # Data for the POST request
    data = {
         "appearance": appearance,
         "minutes_played": minutes_played,
         "award": award,
         "highest_value": highest_value
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors
        prediction = response.json()  # Parse JSON response
        
        # Interpret the prediction result
        if prediction['pred'] == 0:
            result = "Cheap Price"
        elif prediction['pred'] == 1:
            result = "Good Price"
        else:
            result = "Unknown Prediction"
        
        st.write(f"Estimated Price: {result}")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)