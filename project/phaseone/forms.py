from django.forms import ModelForm 
from .models import MessageForm


class TempForm(ModelForm):
    class Meta:
        model = MessageForm
        fields = ['header','priority','text']
