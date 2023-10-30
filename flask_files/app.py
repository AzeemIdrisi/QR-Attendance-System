from flask import Flask, render_template, request, redirect, url_for
import qrcode
import socket

def qrgenerator():

    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    ip = get_ip_address()
    link = f"http://{ip}:5000/add_manually"

    # Function to generate and display a QR code
    def generate_qr_code(link):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code image
        img.save("static/qrcode.png")

    # Generate and display QR codes every 5 seconds

    generate_qr_code(link)


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

@app.route("/submitted", methods=["GET"])
def submitted():
    return render_template("submitted.html")

# Route to handle form submissions (POST request)
@app.route("/add_manually_post", methods=["POST"])
def add_manually_post():
    # Get the selected student from the form
    selected_student = request.form.get("student")

    # Add the selected student to the list of students
    if selected_student:
        students.append({"id": len(students) + 1, "name": selected_student})

    return redirect("/submitted")  # Redirect back to the "Home page after submission

if __name__ == "__main__":
    qrgenerator()
    app.run(host='0.0.0.0',port=5000,debug=True)
