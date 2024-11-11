from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>welcome to the home page!</h1>"

@app.route("/aboute")
def aboute():
    return "<h1>welcome to the aboute page!</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>hi {name},you are welcome to this page!</h1>"

@app.route("/addition/<int:num1>/<int:num2>")
def result(num1,num2):
    return f" {num1} + {num2} is {num1 + num2}"
 
if __name__=="__main__":
    app.run(debug=True)