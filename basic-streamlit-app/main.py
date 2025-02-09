# Importing Libraries
import streamlit as st
import pandas as pd

# Title
st.title("Plenty'a Penguins: My First Streamlit App")

# Short Description
st.subheader("Plenty'a Penguins is designed to x")

# Data
df = pd.read_csv("penguins")

# Display Data
st.write("Here is the dataset loaded from a CSV file:")
st.dataframe(df)
