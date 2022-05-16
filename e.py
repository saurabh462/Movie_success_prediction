import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 


X=pd.read_csv('movie_metadata.csv')
gr=X.gross
a1=X.actor_1_name
bud=X.budget
fa1=bud.mean()
x1=X[['budget','gross']]
print(x1.head())
'''sns.lmplot(x ='budget', y ='gross', data = x1, order = 2, ci = None)'''
x1.fillna(method ='ffill', inplace = True) 
A = np.array(x1['budget']).reshape(-1, 1) 
B = np.array(x1['gross']).reshape(-1, 1)
x1.dropna(inplace = True)
X_train, X_test, y_train, y_test = train_test_split(A, B, test_size = 0.25)
regr = LinearRegression() 
regr.fit(X_train, y_train) 
print(regr.score(X_test, y_test)) 
print()
y_pred = regr.predict(X_test) 
plt.scatter(X_test, y_test, color ='b') 
plt.plot(X_test, y_pred, color ='k')  
plt.show()
