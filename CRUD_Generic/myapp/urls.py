from django.urls import path
from . import views
from .views import StudentCreateView


urlpatterns = [
    path("", views.home, name="home"),
    path("student/add/", StudentCreateView.as_view(), name="student_add"),
]
