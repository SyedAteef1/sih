import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from  query import *
from streamlit_option_menu import option_menu
from firebase_admin import firestore

st.set_page_config(page_title="Onedumbteam", page_icon="😏", layout="wide")
st.subheader("👾Poly Pulley Prediction")
result = view_all_data()
df = pd.DataFrame(result, columns=["Diameter", "Speed", "Vibrations", "Temperature", "Condition", "id"])
st.subheader("Raw Data:")
st.write(df)