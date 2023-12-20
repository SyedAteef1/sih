# app.py
from xgboost import XGBClassifier
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from streamlit_option_menu import option_menu
import home, trending, test, your, about ,temp,livedata,finalpredict
def app():

# Read the Excel file
    df = pd.read_csv('finaltrainingdata.csv')

# Assuming 'diameter', 'speed', 'vibration', and 'temperature' are the columns for prediction
    X = df[['Speed', 'temperature', 'Vibration', 'sound', 'age', 'Strength']]
    y = df['condition']

# Label encoding for classification
    le = LabelEncoder()
    y = le.fit_transform(y)

# Train a logistic regression model (replace with your own model)
    model=XGBClassifier()
    model.fit(X, y)

    def main():
        st.title("Poly Pully Condition Prediction")

    # Add input fields to collect user input
        Speed = st.number_input("Enter speed:")
        temperature = st.number_input("Enter temperature:")
        Vibration = st.number_input("Enter Vibration:")
        sound = st.number_input("Enter sound:")
        age = st.number_input("Enter age:")
        Strength = st.number_input("Enter Strength:")
    

    # Placeholder for displaying results
        result_placeholder = st.empty()

    # Check if the button is clicked
        if st.button("Predict Condition"):
        # Call the function to make predictions
            predict_condition(result_placeholder, Speed, temperature, Vibration, sound, age, Strength)

    def predict_condition(result_placeholder, Speed, temperature, Vibration, sound, age, Strength):
    # Use the trained model to predict condition
        input_data = pd.DataFrame({
            'Speed': [Speed],
            'temperature': [temperature],
            'Vibration': [Vibration],
            'sound': [sound],
            'age': [age],
            'Strength': [Strength]
        
        })

    # Predict condition
        condition_code = model.predict(input_data)[0]
        predicted_condition = le.inverse_transform([condition_code])[0]

    # Display results in the Streamlit app
        result_placeholder.success(f"Predicted Condition: {predicted_condition}")

        if condition_code == 1:
            st.markdown(
            """
                <style>
                    #fullscreen-popup {
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                        background-color: rgba(0, 0, 0, 0.5);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        z-index: 9999;
                    }

                    #popup-content {
                        background-color: red;
                        padding: 20px;
                        border-radius: 10px;
                    }
                </style>
                <div id="fullscreen-popup">
                    <div id="popup-content">
                        <h2>Alert: Condition is 1. Please take action!</h2>
                        <!-- You can add more content or buttons here -->
                        <button onclick="closePopup()">Close</button>
                </div>
            </div>
            <script>
                function closePopup() {
                    document.getElementById('fullscreen-popup').style.display = 'none';
                }
            </script>
            """
                ,   unsafe_allow_html=True
            )

    if __name__ == "__main__":
        main()

