import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("./datasets/dataset.csv")
data.plot()
 ##  if you dont want to plot all parameters, uncomment the following line
 ##  data[["Age","Fare","Cabin"]].plot()
plt.show()