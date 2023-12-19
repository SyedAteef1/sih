import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import *

custom_styles = """
    body {
        background-color: #f0f0f0;  /* Background color of the entire page */
        color: #333;  /* Text color */
    }
    .stApp {
        background-color: #f0f0f0;  /* Background color of the main content area */
    }
    .stMarkdown {
        color: #3498db;  /* Color of Markdown text */
    }
    .stButton {
        background-color: #3498db;  /* Background color of buttons */
        color: #fff;  /* Text color of buttons */
    }
"""

st.set_page_config(page_title="Onedumbteam", page_icon="😏", layout="wide")


st.subheader("👾HISTORICAL DATA")
st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)

result = view_all_data()    
df = pd.DataFrame(result, columns=["Diameter", "Speed", "Vibrations", "Temperature", "Condition", "id"])

# Sidebar
# st.sidebar.image("data/SIH.png", caption="Online Analytics")

# Switcher
# st.sidebar.header("Please Filter")

# Diameter = st.sidebar.multiselect(
#     "Select Diameter",
#     options=df["Diameter"].unique(),
#     default=df["Diameter"].unique(),
# )
# Speed = st.sidebar.multiselect(
#     "Select Speed",
#     options=df["Speed"].unique(),
#     default=df["Speed"].unique(),
# )
# Vibrations = st.sidebar.multiselect(
#     "Select Vibrations",
#     options=df["Vibrations"].unique(),
#     default=df["Vibrations"].unique(),
# )

# Apply filters to update df_selection
# df_selection = df.query(
#     "Diameter==@Diameter & Speed==@Speed & Vibrations==@Vibrations"
#     )
# st.subheader("Raw Data:")
# st.write(df)

# Display the filtered DataFrame
# st.dataframe(df_selection)
def Home():
    df = pd.DataFrame(result, columns=["Diameter", "Speed", "Vibrations", "Temperature", "Condition", "id"])

# Display the raw data
    condition_mapping = {0: "Good", 1: "Not Good", 2: "Bad", 3: "Critical",4:"broken"}

# Create a new column "ModifiedCondition" based on the mapping
    df['ModifiedCondition'] = df['Condition'].map(condition_mapping)
    df = df.drop(columns=['Condition'])
# Display the modified DataFrame
    st.subheader("Modified Raw Data:")
    st.write(df)
Home()
#         top1,top2,top3=st.columns(gap='large')
#         with top1:
#             st.info('Top  Temperature', icon="😁")
#             st.metric_row(label="Average TZS", value=avg_temperature, delta=0)
#         with top2:
#             st.info('low Temperature', icon="😁")
#             st.metric_row(label="Average TZS", value=avg_temperature, delta=0)

#         # Assuming avg_temperature is calculated correctly before this point


# # Display the average temperature using st.metric_row
#         with top3:
#             st.info('Average Temperature', icon="😁")
#             st.metric_row(label="Average TZS", value=avg_temperature, delta=0)
#         st.markdown("-------")

#graps



# Display a bar chart using Plotly Express
st.subheader("3D Scatter Plot:")
fig = px.scatter_3d(df, x="Diameter", y="Speed", z="Vibrations", title="3D Scatter Plot")
st.plotly_chart(fig, use_container_width=True)
# Example: Scaling the temperature values
 # Adjust the scaling factor as needed


