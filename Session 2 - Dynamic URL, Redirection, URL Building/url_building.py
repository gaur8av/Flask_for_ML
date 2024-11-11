from flask import Flask,redirect,url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> welcome to home page</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>congrates {sname},you have passed with score is {marks}</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>sorry {sname},you have failed with score {marks}</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num < 30:
        time.sleep(1)
        # redirect user to fail page
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        # redirect user to pass page
        return redirect(url_for("passed",sname=name,marks=num))


if __name__=="__main__":
    app.run(debug=True)