# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:22:58 2020

@author: saura
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

X=pd.read_csv('movie_metadata.csv')
x1=X[['budget','gross']]
x1.fillna(method ='ffill', inplace = True) 
A = np.array(x1['budget']).reshape(-1, 1) 
B = np.array(x1['gross']).reshape(-1, 1)
x1.dropna(inplace = True)
X_train, X_test, y_train, y_test = train_test_split(A, B, test_size = 0.99)
regr = LinearRegression() 
regr.fit(X_train, y_train) 
y_pred = regr.predict(X_test)
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regr.predict(X_train),color="blue")
plt.xlabel("budget")
plt.ylabel("gross")
plt.show()
