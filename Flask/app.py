from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database of students (you can replace this with a real database)
students = [
    {"id": 1, "name": "Mohd Azeem"},
    {"id": 2, "name": "Dheeraj Jha"},
    {"id": 3, "name": "Shantanu Pant"},
    {"id": 4, "name": "Student 1"},
    {"id": 5, "name": "Student 2"},
    {"id": 6, "name": "Student 3"},
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

# Route to render the "Add Manually" page (GET request)
@app.route("/add_manually", methods=["GET"])
def add_manually():
    return render_template("index1.html")

# Route to handle form submissions (POST request)
@app.route("/add_manually_post", methods=["POST"])
def add_manually_post():
    # Get the selected student from the form
    selected_student = request.form.get("student")

    # Add the selected student to the list of students
    if selected_student:
        students.append({"id": len(students) + 1, "name": selected_student})

    return redirect("/add_manually")  # Redirect back to the "Add Manually" page after submission


if __name__ == "__main__":
    app.run(debug=True)
