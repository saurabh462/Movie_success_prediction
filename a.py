import pandas as pd
from flask import Flask,redirect,url_for,request


app=Flask(__name__)
@app.route('/superhit/')
def superhit():
    return '<html><body align="center"><br><br><br><br><h1>!!! SUPER HIT !!!</h1></body></html>'

@app.route('/hit/')
def hit():
    return '<html><body align="center"><br><br><br><br><h1>!!! HIT !!!</h1></body></html>'

@app.route('/average/')
def average():
    return '<html><body align="center"><br><br><br><br><h1>!!! AVERAGE !!!</h1></body></html>'

@app.route('/flop/')
def flop():
    return '<html><body align="center"><br><br><br><br><h1>!!! FLOP !!!</h1></body></html>'

@app.route('/disaster/')
def disaster():
    return '<html><body align="center"><br><br><br><br><h1>!!! DISASTER !!!</h1></body></html>'

@app.route('/error/')
def error():
    return 'Entered title might not be present in the dataset.Enter a proper title.'

@app.route('/login1',methods=['POST','GET'])
def login1():
    Y=pd.read_csv('tmdb_5000_movies.csv')
    a=Y.title
    o=Y.original_title
    b=Y.vote_count
    v=Y.vote_average
    v1=v.mean()
    x=0
    c=0
    d=0
    e=0
    f=0
    for i in range(b.count()):
        if(b[i]<b.mean()):
            c=c+b[i]
            e=e+1
        elif(b[i]>b.mean()):
            d=d+b[i]
            f=f+1

    g=0
    h=0
    j=0
    k=0
    for i in range(b.count()):
        if(b[i]<c/e):
            g=g+b[i]
            j=j+1
        elif(b[i]>d/e):
            h=h+b[i]
            k=k+1
    if request.method=='POST':
        n=request.form['movie']
        for z in (a):
            if (z==n):
                if (b[x]>h/k):
                    return redirect(url_for('superhit'))
                elif(b[x]>d/f and b[x]<h/k):
                    return redirect(url_for('hit'))
                elif(b[x]>b.mean() and b[x]<d/f):
                    return redirect(url_for('average'))
                elif(b[x]>c/e and b[x]<b.mean()):
                    return redirect(url_for('flop'))
                elif(b[x]<g/j):
                    return redirect(url_for('disaster'))        
                
            x=x+1
        x=0
        for z in (o):
            if(z==n):
                if (v[x]>=v1):
                    return redirect(url_for('hit'))
                elif (v[x]<v1):
                    return redirect(url_for('flop'))
            x=x+1
        for z in (a):
            if (z!=n):
                for z1 in (o):
                    if (z1!=n):
                        return redirect(url_for('error'))
        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)
