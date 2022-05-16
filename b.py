import pandas as pd
from flask import Flask,redirect,url_for,request

X=pd.read_csv('movie_metadata.csv')
a=X.actor_1_name
likes=X.actor_1_facebook_likes
y=likes.mean()
b=X.actor_2_name
likes1=X.actor_2_facebook_likes
z=likes1.mean()
c=X.actor_3_name
likes2=X.actor_3_facebook_likes
w=likes2.mean()
d=len(a)
e=len(b)
f=len(c)

app = Flask(__name__)
            

@app.route('/success/')
def success():
    return '<html><body align="center"><br><br><br><br><h1>!!! HIT !!!</h1></body></html>'

@app.route('/average/')
def average():
    return '<html><body align="center"><br><br><br><br><h1>!!! AVERAGE !!!</h1></body></html>'

@app.route('/unsuccess/')
def unsuccess():
    return '<html><body align="center"><br><br><br><br><h1>!!! FLOP !!!</h1></body></html>'

@app.route('/error/')
def error():
    return 'Entered title might not be present in the dataset.Enter a proper title.'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        actor1=request.form['actor1']
        actor2=request.form['actor2']
        for i in range(d):
            if (actor1==a[i]):
                for j in range(e):
                    if (actor2==b[j]):
                        if(likes[i]>y and likes1[j]>z):
                            return redirect(url_for('success'))
                            break
                        elif((likes[i]>y and likes1[j]<z) or (likes[i]<y and likes1[j]>z)):
                            return redirect(url_for('average'))
                            break
                        elif(likes[i]<y and likes1[j]<z):
                            return redirect(url_for('unsuccess'))
                            break
        for i in range(d):
            if(actor1==a[i]):
                for j in range(d):
                    if(actor2==a[j]):
                        if(likes[i]>y and likes[j]>y):
                            return redirect(url_for('success'))
                            break
                        elif((likes[i]>y and likes[j]<y) or (likes[i]<y and likes[j]>y)):
                            return redirect(url_for('average'))
                            break
                        elif(likes[i]<y and likes[j]<y):
                            return redirect(url_for('unsuccess'))
                            break
        for i in range(e):
            if(actor1==b[i]):
                for j in range(e):
                    if(actor2==b[j]):
                        if(likes1[i]>z and likes1[j]>z):
                            return redirect(url_for('success'))
                            break
                        elif((likes1[i]>z and likes1[j]<z) or (likes1[i]<z and likes1[j]>z)):
                            return redirect(url_for('average'))
                            break
                        elif(likes1[i]<z and likes1[j]<z):
                            return redirect(url_for('unsuccess'))
                            break
        for i in range(e):
            if(actor1==b[i]):
                for j in range(d):
                    if(actor2==a[j]):
                        if(likes1[i]>z and likes[j]>y):
                            return redirect(url_for('success'))
                            break
                        elif((likes1[i]>z and likes[j]<y) or (likes1[i]<z and likes[j]>y)):
                            return redirect(url_for('average'))
                            break
                        elif(likes1[i]<z and likes[j]<y):
                            return redirect(url_for('unsuccess'))
                            break
                        
                     
        
                        
      
                        
                        
                        
                        
                        
        for i in range(d):
            if (actor1==a[i]):
                for j in range(f):
                    if (actor2==c[j]):
                        if(likes[i]>y and likes2[j]>w):
                            return redirect(url_for('success'))
                            break
                        elif((likes[i]>y and likes2[j]<w) or (likes[i]<y and likes2[j]>w)):
                            return redirect(url_for('average'))
                            break
                        elif(likes[i]<y and likes2[j]<w):
                            return redirect(url_for('unsuccess'))
                            break
        
        for i in range(f):
            if(actor1==c[i]):
                for j in range(f):
                    if(actor2==c[j]):
                        if(likes2[i]>w and likes2[j]>w):
                            return redirect(url_for('success'))
                            break
                        elif((likes2[i]>w and likes2[j]<w) or (likes2[i]<w and likes2[j]>w)):
                            return redirect(url_for('average'))
                            break
                        elif(likes2[i]<w and likes2[j]<w):
                            return redirect(url_for('unsuccess'))
                            break
        for i in range(f):
            if(actor1==c[i]):
                for j in range(d):
                    if(actor2==a[j]):
                        if(likes2[i]>w and likes[j]>y):
                            return redirect(url_for('success'))
                            break
                        elif((likes2[i]>w and likes[j]<y) or (likes2[i]<w and likes[j]>y)):
                            return redirect(url_for('average'))
                            break
                        elif(likes2[i]<w and likes[j]<y):
                            return redirect(url_for('unsuccess'))
                            break 
                        
                        
                     
        
                        
                        
                        
                        
        
                        
                        
                        
        for i in range(e):
            if (actor1==b[i]):
                for j in range(f):
                    if (actor2==c[j]):
                        if(likes1[i]>z and likes2[j]>w):
                            return redirect(url_for('success'))
                            break
                        elif((likes1[i]>z and likes2[j]<w) or (likes1[i]<z and likes2[j]>w)):
                            return redirect(url_for('average'))
                            break
                        elif(likes1[i]<z and likes2[j]<w):
                            return redirect(url_for('unsuccess'))
                            break
        
        for i in range(f):
            if(actor1==c[i]):
                for j in range(e):
                    if(actor2==b[j]):
                        if(likes2[i]>w and likes1[j]>z):
                            return redirect(url_for('success'))
                            break
                        elif((likes2[i]>w and likes1[j]<z) or (likes2[i]<w and likes1[j]>z)):
                            return redirect(url_for('average'))
                            break
                        elif(likes2[i]<w and likes1[j]<z):
                            return redirect(url_for('unsuccess'))
                            break 
                        
                     
       
                        
                        
    
            
            
if __name__ == "__main__":
    app.run()