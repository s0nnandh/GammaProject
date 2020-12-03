from django import forms
from .models import Person
a=Person.objects.all()
l = [1,2]


class SimpleForm(forms.Form):
    student = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        choices=l,
    )