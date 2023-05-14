from django.forms import BooleanField, CharField, Form


class LoginForm(Form):
    username = CharField(max_length=150)
    password = CharField(max_length=150)
    save_me = BooleanField(required=False)