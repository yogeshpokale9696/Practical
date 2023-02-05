import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("Mall_Customers.csv")
print(data.head(5))
x = data.iloc[:, [3, 4]].values
print(x)

wcss_list = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    print(kmeans.fit(x))  # Compute k-means clustering
    wcss_list.append(kmeans.inertia_)# Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.

print("hello")
print(wcss_list)
print("hello")

#plt.plot(range(1, 11), wcss_list)
#plt.title("Graph")
#plt.xlabel("Number of clusters")
#plt.ylabel("wcss_list")
#plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_predict = kmeans.fit_predict(x)

plt.scatter(x[y_predict == 0, 0], x[y_predict == 0, 1], s=100, c="blue", label="cluster1")
plt.scatter(x[y_predict == 1, 0], x[y_predict == 1, 1], s=100, c="green", label="cluster2")
plt.scatter(x[y_predict == 2, 0], x[y_predict == 2, 1], s=100, c="orange", label="cluster3")
plt.scatter(x[y_predict == 3, 0], x[y_predict == 3, 1], s=100, c="purple", label="cluster4")
plt.scatter(x[y_predict == 4, 0], x[y_predict == 4, 1], s=100, c="cyan", label="cluster5")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c="red", label="centroid")
plt.title("Cluster of customer")
plt.xlabel("Income")
plt.ylabel("spending")
plt.legend()
plt.show()
