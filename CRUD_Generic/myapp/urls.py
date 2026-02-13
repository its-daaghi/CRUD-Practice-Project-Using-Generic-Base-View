from django.urls import path
from .views import StudentCreateView, StudentListView


urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("student/add/", StudentCreateView.as_view(), name="student_add"),
]
