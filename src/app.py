from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_grade = request.form.get("grade")
    return render_template("hello.html", name=input_name, grade=input_grade)


@app.route("/getrepos")
def getrepos():
    return render_template("getrepos.html")


@app.route("/githubrepos", methods=["POST"])
def display_username():
    username = request.form.get("username")
    p = requests.get("https://api.github.com/users/{username}/repos")
    repos = [r["full_name"] for r in p.json()] if p.status_code == 200 else []
    return render_template("githubrepos.html", name=username, repos=repos)


@app.route("/query", methods=["GET"])
def query():
    return process_query(request.args.get("q"))


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif q == "What is your name?":
        return "The Scottish Swiss German"
    elif "plus" in q:
        return math_addition(q)
    elif "multiplied" in q:
        return math_multiplication(q)
    elif "largest" in q:
        return maximum_of(q)
    elif "square" in q:
        return square_and_cube(q)
    elif "minus" in q:
        return math_subtraction(q)
    else:
        return "Unknown"


def math_addition(q):
    coord = q.split(" ")
    coord[-1] = coord[-1].replace("?", "")
    num1 = int(coord[2])
    num2 = int(coord[-1])
    return str(num1 + num2)


def math_subtraction(q):
    coord = q.split(" ")
    coord[-1] = coord[-1].replace("?", "")
    num1 = int(coord[2])
    num2 = int(coord[-1])
    return str(num1 - num2)


def math_multiplication(q):
    coord = q.split(" ")
    coord[-1] = coord[-1].replace("?", "")
    num1 = int(coord[2])
    num2 = int(coord[-1])
    return str(num1 * num2)


def maximum_of(q):
    question = q.split(":")
    question = question[1]
    question = question.split(",")
    question[-1] = question[-1].replace("?", "")
    question[0] = int(question[0].replace(" ", ""))
    question[1] = int(question[1].replace(" ", ""))
    question[2] = int(question[2].replace(" ", ""))
    return str(max(question[0], question[1], question[2]))


def square_and_cube(q):
    question = q.split(":")
    question = question[1].split(",")
    question[-1] = question[-1].replace("?", "")
    for i in range(0, len(question)):
        question[i] = int(question[i].replace(" ", ""))
    for num in question:
        print(num)
        if num in [1, 64, 729, 4096]:
            return str(num)
        else:
            continue
    return ""
