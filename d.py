'''from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, Flask!"
if __name__ == "__main__":
    app.run()'''
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello():
    return render_template("login.html")
if __name__ == "__main__":
    app.run()


