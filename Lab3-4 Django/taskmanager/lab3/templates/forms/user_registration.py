from django.forms import ModelForm
from taskmanager.lab3.models import User

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"