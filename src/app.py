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


@app.route("/query", methods=["GET"])
def query():
    return process_query(request.args.get('q'))


def process_query(q):
    if (q == "dinosaurs"):
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
