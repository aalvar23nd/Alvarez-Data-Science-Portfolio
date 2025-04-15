# import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# title 
st.title("Supervised Machine Learning: Linear Regression") # sets the main title of the app
st.write("Hello there! This app lets you explore a linear regression supervised learning model by uploading your own dataset or choosing a sample.") # displays a welcome message that describes what the app does

# sidebar
st.sidebar.header("Data Options: Please choose one") # creates a sidebar to allow user to choose between the sample dataset or uploading their own csv file
dataset_choice = st.sidebar.selectbox("Chooose a dataset", ("California Housing", "Upload your own")) # options for sidebar

# dataset upload
if dataset_choice == "California Housing": # if user selects the california housing dataset, then
    housing = fetch_california_housing() # loads the sample dataset
    X = pd.DataFrame(housing.data, columns=housing.feature_names) # identitfies the features (or predictor variables)
    y = pd.Series(housing.target, name = "med_house_value") # identifies the target (or what we want to predict, which, in this case, is the median house value)
else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type = ["csv"])
    if uploaded_file: # if the user uploads their own csv file
        df = pd.read_csv(uploaded_file) # dataset is read
        st.write("Preview of uploaded data;")
        st.write(df.head()) # shows a preview of the first few rows
        target_column = st.sidebar.selectbox("Select target column", df.columns) # allows the user to select the target column to predict
        feature_columns = st.sidebar.multiselect("Select feature columns", df.columns.drop(target_column)) # allows user to select the feature columns to use as predictors
        if feature_columns:
            X = df[feature_columns] # assigns selected features for predictors
            y = df[target_column] # assigns selected target column to predict
        else:
            st.warning("Please select feature columns to continue.")
            st.stop() # stops execution if no features are selected
    else:
        st.warning("Upload a CSV file to proceed.")
        st.stop() # stops execution if no file is uploaded or dataset is chosen

# sidebar
st.sidebar.header("Model Settings") # lets the user set the test size and randome state
test_size = st.sidebar.slider("Test size (percentage %)", 10, 50, 20, step = 5) # allows user to select how much data goes into the test set
random_state = st.sidebar.number_input("Random State") # allows for reproduction of findings

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = test_size / 100, random_state = int(random_state)) # splits the data into training and testing sets and adjusts test size from percentage to decimal

# fit model
model = LinearRegression()
model.fit(X_train, y_train) # creates and trains a linear regression model
y_pred = model.predict(X_test) # makes predictions on the test set

# display
st.subheader("Model Performance")
r2 = r2_score(y_test, y_pred) # shpws how well the predictions match the actual values
mae = mean_absolute_error(y_test, y_pred) # average of absolute errors
st.metric("R2 Score", f"{r2:.4f}")
st.metric("Mean Absolute Error", f"{mae:.4f}")

# plot: predicitions vs actual
st.subheader("Predictions vs Actual Values")
fig1, ax1 = plt.subplots()
sns.scatterplot(x = y_test, y = y_pred, alpha = .6, ax = ax1) # creates a scatterplot comparing predicted values against the actual values
ax1.set_xlabel("Actual")
ax1.set_ylabel("Predicted")
ax1.set_title("Predictions vs Actual Values")
st.pyplot(fig1)

# plot: residuals
st.subheader("Residuals Plot")
residuals = y_test - y_pred # computres and plots the residuals (or prediction errors)
fig2, ax2 = plt.subplots()
sns.histplot(residuals, kde = True, ax = ax2) # shows distribution with histogram and kernel density estimate
ax2.set_title("Distribution of Residuals")
ax2.set_xlabel("Residual")
st.pyplot(fig2)

# coefficients
st.subheader("Model Coefficients")
coeff_df = pd.DataFrame({ #displays table of regression coefficients
    "Feature": X.columns,
    "Coefficient": model.coef_
})
st.write(coeff_df)

# complete
st.success("Model training complete. You can change settings in the sidebar.") # informs user that training went successfully

