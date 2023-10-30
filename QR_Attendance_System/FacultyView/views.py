from django.shortcuts import render

# Create your views here.

students = [
    {"id": 1, "name": "Mohd Azeem"},
    {"id": 2, "name": "Dheeraj Jha"},
    {"id": 3, "name": "Shantanu Pant"},
    {"id": 4, "name": "Student 1"},
    {"id": 5, "name": "Student 2"},
    {"id": 6, "name": "Student 3"},
]


def faculty_view(request):
    return render(
        request,
        "FacultyView/FacultyViewIndex.html",
        {
            "students": students,
        },
    )


def add_manually(request):
    return render(request, "StudentView/StudentViewIndex.html")
