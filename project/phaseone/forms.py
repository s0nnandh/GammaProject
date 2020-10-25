from django.forms import ModelForm 
from .models import MessageForm

# creating a form 


class TempForm(ModelForm):
    class Meta:
        model = MessageForm
        fields = '__all__'
