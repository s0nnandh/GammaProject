from django.db import models
from phaseone.models import MessageForm
from phaseone.forms import TempForm

class Person(models.Model):
    userid = models.CharField(max_length=128,primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128,primary_key=True)
    members = models.ManyToManyField(Person, through='Membership')
    messages = models.ManyToManyField(MessageForm,through='Messageship')
    prof = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    invite_reason = models.IntegerField(default=0)


class Messageship(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    form2 = models.ForeignKey(MessageForm, on_delete=models.CASCADE)


'''
Student and prof - same class extended from django user
user_type = ['prof', 'stud']

login API endpoint takes 'username', 'password', 'platform'
'''