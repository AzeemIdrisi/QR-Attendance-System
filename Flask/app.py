from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database of students (you can replace this with a real database)
students = [
    {"id": 1, "name": "Student 1"},
    {"id": 2, "name": "Student 2"},
    {"id": 3, "name": "Student 3"},
]

# Route to render the main HTML template
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_id_to_delete = int(request.form["student_id"])
        for student in students:
            if student["id"] == student_id_to_delete:
                students.remove(student)
                break

    return render_template("index.html", students=students)

# Route to render the "Add Manually" page
@app.route("/add_manually")
def add_manually():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)
