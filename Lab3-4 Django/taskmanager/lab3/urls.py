from django.urls import path

from taskmanager.lab3.views import content, login, logout, registration

urlpatterns = [
    path("content/", content, name="content"),
    path("registration/", registration, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]