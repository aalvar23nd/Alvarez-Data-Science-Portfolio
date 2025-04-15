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
st.title("Supervised Machine Learning: Linear Regression")
st.write("Hello there! This app lets you explore a linear regression supervised learning model by uploading your own dataset or choosing a sample.")

# sidebar
st.sidebar.header("Data Options: Please choose one")
dataset_choice = st.sidebar.selectbox("Chooose a dataset", ("California Housing", "Student Performance", "Upload your own"))

# california dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns = housing.feature_names)
y = pd.Series(housing.target, name = 'med_house_value')

# user upload
if dataset_choice == "California Housing":
    housing = fetch_california_housing()
    X = pd.DataFrame(housing.data, columns=housing.feature_names)
    y = pd.Series(housing.target, name='med_house_value')
else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type = ["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data;")
        st.write(df.head())
        target_column = st.sidebar.selectbox("Select target column", df.columns)
        feature_columns = st.sidebar.multiselect("Select feature columns", df.columns.drop(target_column))
        if feature_columns:
            X = df[feature_columns]
            y = df[target_column]
        else:
            st.warning("Please select feature columns to continue.")
            st.stop()
    else:
        st.warning("Upload a CSV file to proceed.")
        st.stop()

# sidebar
st.sidebar.header("Model Settings")
test_size = st.sidebar.slider("Test size (percentage %)", 10, 50, 20, step = 5)
random_state = st.sidebar.number_input("Random State")

# split data
st.write(f"X shape: {X.shape}")
st.write(f"y shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = test_size / 100,
                                                    random_state = random_state)

# fit model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# display
st.subheader("Model Performance")
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
st.metric("R2 Score", f"{r2:.4f}")
st.metric("Mean Absolute Error", f"{mae:.4f}")

# plot: predicitions vs actual
st.subheader("Predictions vs Actual Values")
fig1, ax1 = plt.subplots()
sns.scatterplot(x = y_test, y = y_pred, alpha = .6, ax = ax1)
ax1.set_xlabel("Actual")
ax1.set_ylabel("Predicted")
ax1.set_title("Predictions vs Actual Values Values")
st.pyplot(fig1)

# plot: residuals
st.subheader("Residuals Plot")
residuals = y_test - y_pred
fig2, ax2 = plt.subplots()
sns.histplot(residuals, kde = True, ax = ax2)
ax2.set_title("Distribution of Residuals")
ax2.set_label("Residual")
st.pyplot(fig2)

# coefficients
st.subheader("Model Coefficients")
coeff_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})
st.write(coeff_df)

# complete
st.success("Model training complete. You can change settings in the sidebar.")

