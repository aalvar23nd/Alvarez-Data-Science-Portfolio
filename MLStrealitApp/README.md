# Lessons in Supervised Machine Learning Applications: <br> A Streamlit App to Train a Supervised Machine Learning Model <br> (Linear Regression)

## Project Overview
### "Lessons in Supervised Machine Learning Applications" is a streamlit app that allows users to explore linear regression. 
Users can:<br>
1. Upload their own dataset (csv file)
  <br>or
3. Use the sample dataset provided (California Housing)<br>
### "Lessons in Machine Learning Applications" allows users to:
1. Select their own feature or target variables<br>
2. Split the data into training and testing sets<br>
3. Train a linear regression model<br>
4. View model performance metrics like r2 and mean absolute error<br>
5. Visualize predicitons and residuals<br>
6. Identify the model's coefficients<br>

## Instructions

```
# Cloning

git clone https://github.com/aalvar23nd/MLStrealitApp

# Repository

cd MLStreaLitApp

# Install Dependencies

pip install -r requirements.txt

# Run

streamlit run main.py

```
## Dataset
### This dataset is adapted from https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html. The dataset shows information about different attributes of various houses in California such as median income (of a block group), average number of bedrooms per hosusehold, and the median house age (of a block group) among many others. 

### For the purposes of my dataset, I selected the variables: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude as my features to predict the target variable, Med_House_Value.

## References
### For further reading on:
#### Linear Regression: https://machinelearningmastery.com/linear-regression-for-machine-learning/
#### Utilizing LinearRegression in Python: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html


## Expected Outputs
### After running the script, the expected outputs are:<br>
#### - Model Evaluation Metrics:
##### - R2 Score
##### - Mean Absolute Error
#### - Two visualizations:
##### - Predictions vs Actual Values
##### - Residuals Plot
