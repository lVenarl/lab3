from django.forms import CharField, TextInput, Form, Textarea


class BookForm(Form):
    content = CharField(widget=Textarea)