import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
df = DataFrame(pd.read_csv('stock.csv'))
print(df)
X = df[['Interest_Rate','Unemployment_Rate']]
Y = df ['Stock_Index_Price']
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print('Intercept value: \n', regr.intercept_)
print('Coefficient value: \n', regr.coef_)
New_Interest_Rate= 2.75
New_Unemployment_Rate = 5.3
print('predicted stock index price: \n', regr.predict([[New_Interest_Rate,New_Unemployment_Rate]]))
r_sq = regr.score(X,Y)
print("Co-efficient of determintion(R-squared)",{r_sq})
X = sm.add_constant(X)
model = sm.OLS(Y,X).fit()
adjusted_r_sq = model.rsquared_adj
print("Adjusted r squared:",adjusted_r_sq)
