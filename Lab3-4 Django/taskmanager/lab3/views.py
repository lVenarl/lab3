from django.shortcuts import redirect, render


from .taskmanager.lab3.templates.forms.user_login import LoginForm
from templates.forms.book_form import BookForm
from templates.forms import RegistrationForm
from models import Book, User



def content(request):
    """Content page."""
    if request.session.get("user") or request.COOKIES.get("user"):
        content = Book.objects.all()
        if not request.session.get("user") and request.COOKIES.get("user"):
            request.session["user"] = User
            request.session.modified = True
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                user = User.objects.get(username=request.session.get("user"))
                obj = Book.objects.create(content=form.cleaned_data["content"], author=user)
                obj.save()
                redirect("content")
        else:
            form = BookForm()
        return render(request, "core/content.html",
                      context={"user": request.session.get("user"), "content": content, "form": form})
    else:
        return redirect("login")


def logout(request):
    """LogOut view."""

    del request.session["user"]
    request.session.modified = True
    response = redirect("login")
    response.delete_cookie("user")
    return response


def registration(request):
    """Registration page."""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    return render(request, "core/registration.html", {"form": form})


def login(request):
    """Login page."""
    if request.session.get("user"):
        return redirect("content")
    else:
        if user := request.COOKIES.get("user"):
            request.session["user"] = user
            request.session.modified = True
            response = redirect("content")
            return response

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data["username"])
            if user:
                if user[0].password == form.cleaned_data["password"]:
                    request.session["user"] = form.cleaned_data["username"]
                    request.session.modified = True
                    response = redirect("content")

                    if form.cleaned_data["save_me"]:
                        response.set_cookie("user", form.cleaned_data["username"])
                    return response
                else:
                    form.add_error("password", "Пароль неверный")
            else:
                form.add_error("username", "Пользователя с таким именем не существует")
    else:
        form = LoginForm()
    return render(request, "core/login.html", {"form": form, "user": request.session.get("user")})