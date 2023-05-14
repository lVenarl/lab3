from django.db import models
from django.db.models import CharField, Model


class User(Model):
    username = CharField(max_length=150, unique=True, blank=False, null=False)
    password = CharField(max_length=150, blank=False, null=False)


class Book(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

