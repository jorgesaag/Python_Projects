import  pandas as pd
import tabulate as tab
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans as km

Data = {'Abdominales': [25, 34, 22, 27, 33, 31, 22, 35, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45, 38, 43, 51, 46],
        'Sentadillas': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29, 27, 8, 7]}

df = pd.DataFrame({ key:pd.Series(value) for key, value in Data.items() })
df["Abdominales"] = df["Abdominales"].fillna(0)
print(tab.tabulate(df, headers="keys"))
plt.scatter(df['Abdominales'], df['Sentadillas'])
plt.show()

kmeans = km(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
plt.scatter(df['Abdominales'], df['Sentadillas'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=50)
plt.show()

kmeans = km(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
plt.scatter(df['Abdominales'], df['Sentadillas'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=50)
plt.show()
