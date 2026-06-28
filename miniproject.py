from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE = "students.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    students = load_data()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        students = load_data()

        student = {
            "id": len(students) + 1,
            "name": request.form["name"],
            "course": request.form["course"],
            "email": request.form["email"]
        }

        students.append(student)
        save_data(students)

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    students = load_data()
    students = [s for s in students if s["id"] != id]
    save_data(students)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)