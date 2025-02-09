# Importing Libraries
import streamlit as st
import pandas as pd

# Title
st.title("Plenty'a Penguins ૮(•͈⌔•͈)ა: My First Streamlit App")

# Short Description
st.subheader("Plenty'a Penguins is designed to introduce users to the 'penguins' dataset, which has information on penguins by species, sex, year, island location, and flipper length (mm), among other key variables. Plenty'a Penguins allows users to filter data by penguin species and a range of flipper lengths (which they can choose). I hope you enjoy it!")

# Data
df = pd.read_csv("data/penguins.csv")

# Display Data
st.write("Here is the dataset loaded from a CSV file:")
st.dataframe(df)

# Interactive Filtering Options

## Dropdown: Penguin Species
penguin_species = st.selectbox("Select a species of penguin:", df["species"].unique()) # Allows user to choose penguin species
filtered_penguin_species = df[df["species"] == penguin_species] # Filters data by penguin species chosen

st.write(f"Data on {penguin_species} Penguins:") # Tells user what data is being shown
st.dataframe(filtered_penguin_species) # Displays data

## Slider: Flipper Length
flipper_length = st.slider("Select a range of flipper lengths (mm):", 172, 210, (180, 190)) # Allows user to select a range of flipper lengths (mm)
filtered_flipper_length = df[df["flipper_length_mm"].between(*flipper_length, inclusive = "both")] # Filters data to show penguins that fit range of flipper lengths (mm) chosen

st.write(f"Data on penguins with a flipper length range (mm) of {flipper_length}:") # Tells user what data is being shown
st.dataframe(filtered_flipper_length) # Displays data
