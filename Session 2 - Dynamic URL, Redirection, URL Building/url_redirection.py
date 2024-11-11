from flask import Flask,redirect,url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> welcome to home page</h1>"

@app.route("/pass")
def passed():
    return "<h1>congrates,you have passed</h1>"

@app.route("/fail")
def failed():
    return "<h1>sorry,you have failed</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        # redirect user to fail page
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        # redirect user to pass page
        return redirect(url_for("passed"))


if __name__=="__main__":
    app.run(debug=True)