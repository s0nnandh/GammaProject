from django.db import models
from django.forms import Textarea

class MessageForm(models.Model):
    Choices =(
        ("1","Very Important"),
        ("2","Important"),
        ("3","Okay"),
    )   
    priority = models.CharField(max_length = 2,choices=Choices)
    header = models.CharField(max_length = 100)
    text = models.TextField()
    time = models.DateTimeField(auto_now=False,primary_key=True)
    def __str__(self):
        return self.header

