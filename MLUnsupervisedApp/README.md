# Lessons in Unsupervised Machine Learning: Clustering Exploration: <br> A Streamlit App to Explore K-Means and Hierarchical Clustering

## Project Overview
### "Unsupervised Machine Learning: Clustering Exploration" is a streamlit app that allows users to explore unsupervised learning techniques through clustering. 
Users can:<br>
1. Upload their own dataset (csv file)
  <br>or
2. Use the sample dataset provided (Iris)<br>
### "Unsupervised Machine Learning: Clustering Exploration" allows users to:
1. Select their own numeric feature to cluster<br>
2. Choose between K-Means and Hierarchical clustering<br>
3. Perform principal component analysis for visualization<br>
4. View a scatterplot of PCA features colored by cluster groups<br>
5. Examine the silhouette score<br>
6. Use the elbow method to detemrine the right amount of clusters<br>
7. View cluster centers<br>

## Instructions

```
# Cloning

git clone https://github.com/aalvar23nd/MLUnsupervisedApp

# Repository

cd MLUnsupervisedApp

# Install Dependencies

pip install -r requirements.txt

# Run

streamlit run main.py

```
## Dataset
### This dataset is adapted from https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html. The dataset shows information about different types of irises (setosa, versicolour, and virgincia), specifically, their petal and sepal length and width. 

### For the purposes of my streamlit app, if users upload their own dataset, their will need to be two numeric variables perform the model. 

## References
### For further reading on:
#### K-Means: https://machinelearningmastery.com/linear-regression-for-machine-learning/](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
#### Hierarchical Clustering: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html
#### PCA: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
#### Silhouette Score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
#### Elbow Method: https://www.scikit-yb.org/en/latest/api/cluster/elbow.html


## Expected Outputs
### After running the script, the expected outputs are:<br>
#### PCA Scatterplot with cluster groups:<br>
![PCA_Scatter](https://github.com/user-attachments/assets/e57589b9-c9e1-49f6-ad65-2ac394324ea5)
#### Silhouette Score
#### Elbow Curve for Optimal K:<br>
![EC_OK](https://github.com/user-attachments/assets/9fca1e8f-ac3e-4d99-abef-ec1d2ed4d95e) 
#### Cluster Center Table
