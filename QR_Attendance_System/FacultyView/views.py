from django.shortcuts import render
from .models import Student

# Create your views here.


def faculty_view(request):
    students = Student.objects.all().order_by("s_roll")
    return render(
        request,
        "FacultyView/FacultyViewIndex.html",
        {
            "students": students,
        },
    )


def add_manually(request):
    return render(request, "StudentView/StudentViewIndex.html")
