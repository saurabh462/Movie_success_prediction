import pandas as pd

Y=pd.read_csv('tmdb_5000_movies.csv')
a=Y.title
c=0
n=input('--')
for i in range(a[0]):
    if (a[0].find(n[i]) == -1):
        c=c
    else:
        c=c+1
if(c==len(a[0])):
    print('y')
else:
    print('n')
