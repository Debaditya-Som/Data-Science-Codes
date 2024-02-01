# K-means clustering
# It is a clustering method that subdivides a single cluster or a collection of data points into k differnet clusters or groups
# It is an unsupervised learing algorithm that groups the unlabelled dataset into different clusters. Here, k defines the number of pre defined clusters that needs to b e created in the process
# for eg,: if k = 2, there will be 2 clusters, if k = 3, there will be 3 clusters and so on.
# It is an iterative algorithm that divides the unlabelled dataset into k different clusters in such a way that each data set belongs to only one group that has similar properties.

from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

Data = { 'x' : [185,170,168,179,182,188,180,180,183,180,180,177],
         'y' : [72,56,60,68,72,77,71,70,84,88,67,76]    
}

df = DataFrame(Data,columns=['x','y'])
wcss = [] #initialize empty list to store the WCSS Value.

for i in range(1,13):    #Each iteration corresponds to a differemnt number of clusters (k)
    km = KMeans(n_clusters=i) 
    km.fit_predict(df) #fits model into data(df)
    wcss.append(km.inertia_)

wcss

plt.plot(wcss)
plt.xlabel('Number of cluster')
plt.ylabel('WCSS')
plt.title("Elbow point graph for optimal value of k")
plt.show()

my_centroids = np.array([[185,75],[170,56],[168,60]])
kmeans = KMeans(n_clusters = 3, init= my_centroids).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

X = df.iloc[:,:].values
y_means = kmeans.fit_predict(X)

plt.scatter(X[y_means == 0,0], X[y_means==0,1],s=60,c='blue',label='Cluster 1')
plt.scatter(X[y_means == 1,0], X[y_means==1,1],s=60,c='chocolate',label='Cluster 2')
plt.scatter(X[y_means == 2,0], X[y_means==2,1],s=60,c='pink',label='Cluster 3')

plt.scatter(centroids [:,0],centroids [:,1], c = 'black',s=100,marker='+',label ='centroids ')
plt.legend(loc = 'lower right')
plt.show()
