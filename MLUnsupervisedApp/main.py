# import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# title
st.title("Unsupervised Machine Learning: Clustering Exploration")
st.write("Welcome! This app allows you to explore unsupervised learning using either K-Means or Hierarchical clustering. Upload your own dataset or try a sample to get started.")

# sidebar: data options
st.sidebar.header("Data Options")
sample_datasets = {
    "Iris Dataset (Sample)": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
}
dataset_choice = st.sidebar.selectbox("Choose a dataset", ("Upload your own", *sample_datasets.keys()))

# dataset upload or selection
if dataset_choice == "Upload your own":
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.write(df.head())
    else:
        st.warning("Please upload a CSV file to proceed.")
        st.stop() # Execution stops here if no file is uploaded
else:
    df = pd.read_csv(sample_datasets[dataset_choice])
    st.write(f"Using sample dataset: {dataset_choice}")
    st.write(df.head())

# --- Conditional rendering based on df ---
if 'df' in locals(): # Check if df is defined
    # numeric column selection
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Dataset must contain at least 2 numeric columns.")
        st.stop()

    # clustering method selection
    st.sidebar.header("Clustering Settings")
    clustering_method = st.sidebar.selectbox("Clustering method", ["K-Means", "Hierarchical"])
    selected_features = st.sidebar.multiselect("Select features for clustering", numeric_cols, default=numeric_cols[:2])
    if len(selected_features) < 2:
        st.warning("Please select at least 2 numeric features.")
        st.stop()

    X = df[selected_features].dropna()  # subset to selected features and drop missing
    scaler = StandardScaler()  # scale the data
    X_scaled = scaler.fit_transform(X)

    # slider for number of clusters
    k = st.sidebar.slider("Number of clusters (k)", 2, 10, 3)

    # apply clustering
    if clustering_method == "K-Means":
        model = KMeans(n_clusters=k, random_state=42)
        cluster_labels = model.fit_predict(X_scaled)
        silhouette_avg = silhouette_score(X_scaled, cluster_labels)
    else:
        model = AgglomerativeClustering(n_clusters=k)
        cluster_labels = model.fit_predict(X_scaled)
        silhouette_avg = silhouette_score(X_scaled, cluster_labels)

    # PCA for 2D plotting
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # scatterplot of PCA
    st.subheader("PCA Scatterplot with Cluster Labels")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=cluster_labels, palette="tab10", ax=ax1)
    ax1.set_xlabel("PCA 1")
    ax1.set_ylabel("PCA 2")
    ax1.set_title("2D PCA of Clusters")
    st.pyplot(fig1)

    # silhouette score
    st.subheader("Silhouette Score")
    st.metric("Silhouette Score", f"{silhouette_avg:.4f}")

    # elbow method for K-Means only
    if clustering_method == "K-Means":
        st.subheader("Elbow Method for Optimal k")
        distortions = []
        K_range = range(1, 11)
        for i in K_range:
            km = KMeans(n_clusters=i, random_state=42)
            km.fit(X_scaled)
            distortions.append(km.inertia_)

        fig2, ax2 = plt.subplots()
        ax2.plot(K_range, distortions, 'bx-')
        ax2.set_xlabel('Number of Clusters (k)')
        ax2.set_ylabel('Inertia')
        ax2.set_title('Elbow Method')
        st.pyplot(fig2)

        # display cluster centers
        st.subheader("Cluster Centers (scaled)")
        cluster_centers_df = pd.DataFrame(model.cluster_centers_, columns=selected_features)
        st.write(cluster_centers_df)

    # complete
    st.success("Clustering complete. You can adjust settings in the sidebar to explore different configurations.")
