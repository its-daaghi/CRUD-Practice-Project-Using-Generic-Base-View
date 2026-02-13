from django.urls import path
from .views import StudentCreateView, StudentListView, StudentDetailView


urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("student/add/", StudentCreateView.as_view(), name="student_add"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
]
