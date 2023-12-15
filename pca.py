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
df.info()
df.describe()
# This method in pandas provides descriptive statitics of the dataframes numeric columns.IT includes measures of central tendency, dispersion and shape of the distribution of the dataset

df.species.replace({'Setosa':0,'Versicolor':1,'Virginica':2},inplace= True)
df.head()

features = ['sepal_length',	'sepal_width',	'petal_length',	'petal_width'	]

x = df.loc[:, features].values

y = df.loc[:,['species']].values

x = StandardScaler().fit_transform(x)
print(pd.DataFrame(data=x,columns=features).head())

#PCA

pca = PCA()

X_new = pca.fit_transform(x)

#VARIANCE

explained_variance = pca.explained_variance_ratio_
explained_variance

pca = PCA(n_components=2)
principalComponent = pca.fit_transform(x)
principalDF = pd.DataFrame(data= principalComponent, columns=['PC1','PC2'])
print(principalDF)
