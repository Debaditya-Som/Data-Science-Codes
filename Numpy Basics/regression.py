import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm

# Reading the input data from csv file
df = DataFrame(pd.read_csv("stock.csv"))
df

df.shape

# Here we have 1 variable for simple regression.

X = df[['Interest_Rate']]
Y = df['Stock_Index_Price']


# Model fitting with sklearn

regr = linear_model.LinearRegression()
regr.fit(X,Y)

# Displaying Intercepts and coefficients

print('Intercept value: \n', regr.intercept_)
print('Coefficient value: \n', regr.coef_)


# Creating a scatter plot with a regression line

import seaborn as sn
import matplotlib.pyplot as plt

sn.regplot(x= 'Interest_Rate', y='Stock_Index_Price', data= df)
plt.title('Scatter plot for Stock_Index_Price versus Interest_Rate with a regression line',y=1.05)
plt.xlabel('Interest_Rate')
plt.ylabel('Stock_Index_Price')
plt.show()


y_pred = regr.predict(X)
# Convert y_pred to a DataFrame
df1 = pd.DataFrame({'Predicted Stock Index Price': y_pred})

# Print the DataFrame
print(df1)

#print(y_pred)  if required


# Prediction with sklearn

New_Interest_Rate = 2.90
print('Predicted Stock Index Price: \n',
      regr.predict([[New_Interest_Rate]]))


numeric_col = ['Interest_Rate', 'Stock_Index_Price']


df[numeric_col].corr()



X = sm.add_constant(X)   # (1)

model = sm.OLS(Y, X).fit()  # (2)

print_model = model.summary()  # (3)
print(print_model)  # (4)


# Write in copy

# R-squared:                       0.876
# Adj. R-squared:                  0.870

#                   Coefficient      Standard error         P values
# const              -99.4643           95.210               0.308
# Interest_Rate      564.2039           45.317               0.000








