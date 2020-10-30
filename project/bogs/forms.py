from django import forms
from .models import Person
a=Person.objects.all()
l = []
for x in a:
    l.append((x.userid,x.name))

class SimpleForm(forms.Form):
    student = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=l,
    )
