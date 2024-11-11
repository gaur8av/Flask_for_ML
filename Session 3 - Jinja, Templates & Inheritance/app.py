from flask import Flask,render_template,url_for

from employee import employee_data

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home Page")


#about page
@app.route("/about")
def about():
    return render_template("about.html", title="About Page")

 
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template(
        "evaluate.html",
        title = "Evaluate",
        number = num

    )

@app.route("/employees")
def employee():
    return render_template(
        "employees.html",
        title="Employees",
        employees=employee_data
    )


if __name__=="__main__":
    app.run(debug=True)