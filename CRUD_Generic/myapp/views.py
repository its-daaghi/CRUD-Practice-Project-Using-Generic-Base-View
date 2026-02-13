from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Student
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, "myapp/student.html")


class StudentCreateView(CreateView):
    model = Student
    fields = ["name", "roll", "marks"]
    template_name = "myapp/student_form.html"
    success_url = reverse_lazy("student_list")  # redirect after save
