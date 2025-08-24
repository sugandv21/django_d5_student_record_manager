from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("student/", views.student_list, name="student_list"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/create/", views.student_create, name="student_create"),
    path("student/<int:pk>/edit/", views.student_update, name="student_update"),
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),
]
