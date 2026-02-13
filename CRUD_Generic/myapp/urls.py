from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
)


urlpatterns = [
    path("", StudentListView.as_view(), name="student_list"),
    path("student/add/", StudentCreateView.as_view(), name="student_add"),
    path("student/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path(
        "student/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"
    ),
    path(
        "student/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"
    ),
]
