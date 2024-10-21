from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_grade = request.form.get("grade")
    return render_template("hello.html", name=input_name, grade=input_grade)
