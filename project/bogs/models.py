from django.db import models

class Person(models.Model):
    primary = models.CharField(max_length=256,primary_key=True)
    userid = models.CharField(max_length=128,unique=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)
    Token_key = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class MessageForm(models.Model):
    Choices =(
        ("1","Very Important"),
        ("2","Important"),
        ("3","Okay"),
    )   
    printer = models.CharField(max_length=300,primary_key=True)
    priority = models.CharField(max_length = 2,choices=Choices)
    header = models.CharField(max_length = 100)
    text = models.TextField()
    time = models.DateTimeField(auto_now=False)
    seen = models.ManyToManyField(Person,through='Message_seen')
    def __str__(self):
        return self.header

class Group(models.Model):
    name = models.CharField(max_length=128,primary_key=True)

    members = models.ManyToManyField(Person, through='Membership')
    messages = models.ManyToManyField(MessageForm,through='Messageship')
    prof = models.CharField(max_length=128)
    grp_name=models.CharField(max_length=128)
    bool = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person,to_field='userid', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
class Messageship(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    form2 = models.ForeignKey(MessageForm, on_delete=models.CASCADE)


class Message_seen(models.Model):
    person = models.ForeignKey(Person,to_field='userid', on_delete=models.CASCADE)
    form2 = models.ForeignKey(MessageForm, on_delete=models.CASCADE)
    class Meta:
       unique_together = ("person", "form2")
'''
Student and prof - same class extended from django user
user_type = ['prof', 'stud']

login API endpoint takes 'username', 'password', 'platform'
'''

