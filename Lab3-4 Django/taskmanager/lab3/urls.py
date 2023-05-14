from django.urls import path

from .views import content, login, logout, registration

urlpatterns = [
    path("content/", content, name="content"),
    path("registration/", registration, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
