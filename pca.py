#PCA - PRINCIPAL COMPONENT ANALYSIS is dimestionality reduction method that is often used to reduce the dimensionality of large data sets by trnasforming
# a large set of variables into a smaller one that still contains most of the information in  the large set
#in this technique the variablrs are trnasformed into a new set of variables, which are linear comnbination of original variables. This new set of variables are know as principal components.
# The first principl component captures the most variation in data, but the second pricpal component captures the maximum variance, that is orthogonal to the first principal componenet and so on.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('iris.csv')
df.Species.replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2},inplace= True)
df.head()

features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
x = df.loc[:, features].values
y = df.loc[:,['Species']].values

x = StandardScaler().fit_transform(x)
pd.DataFrame(data=x,columns=features).head()

pca = PCA()
X_new = pca.fit_transform(x)
explained_variance = pca.explained_variance_ratio_ #VARIANCE

pca = PCA(n_components=2)
principalComponent = pca.fit_transform(x)
principalDF = pd.DataFrame(data= principalComponent, columns=['PC1','PC2'])
