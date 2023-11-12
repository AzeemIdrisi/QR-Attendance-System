from django.shortcuts import render
from FacultyView.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

present = set()


def add_manually_post(request):
    student_roll = request.POST["student-name"]
    student = Student.objects.get(s_roll=student_roll)
    present.add(student)
    return HttpResponseRedirect("/submitted")


def submitted(request):
    return render(request, "StudentView/Submitted.html")
