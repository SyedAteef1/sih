import streamlit as st
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import time
from streamlit_option_menu import option_menu


import home, trending, test, your, about ,temp,livedata
# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sih"
)

cursor = connection.cursor()

# Streamlit app

# Function to fetch and display data from MySQL
def display_data():
    while True:
        query = "SELECT * FROM finaltrainingdata LIMIT 1"
        cursor.execute(query)
        data = cursor.fetchone()

        if data:
            st.write("Fetched at:", time.strftime("%Y-%m-%d %H:%M:%S"))
            st.write("Data:", data)
            st.write("---")

            # Assume data is a tuple (id, feature1, feature2, ..., target)
            # Extract features and target
            features = data[1:-1]
            target = data[-1]

            # Create a DataFrame for the current data point
            current_df = pd.DataFrame([data], columns=['id', 'feature1', 'feature2', 'feature3','feature4','feature5','feature6','target'])

            # Train a simple linear regression model using all data so far
            X = current_df[['feature1', 'feature2']]
            y = current_df['target']
            model = LinearRegression()
            model.fit(X, y)

            # Make a prediction
            prediction = model.predict(X)

            st.write("Model Prediction:", prediction)

        else:
            st.warning("No data found in the table.")

        time.sleep(5)  # Wait for 5 seconds before the next iteration

# Display data
if st.button("Start Fetching Data Every 5 Seconds"):
    display_data()

# Close the MySQL connection (Note: This won't be reached in the example since the while loop is infinite)
cursor.close()
connection.close()
