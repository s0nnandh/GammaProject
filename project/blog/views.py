from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from blog.models import Login
def home(request):
    return render(request,'home.html')

def signup(request):   
    return render(request,'result.html',{"warning":"null"})
def signin(request):   
    if request.method =='POST':  
         try:
            val1= request.POST['num1']
            val2= request.POST['num2']
            val = Login.objects.all() 
            for x in val:
                if (x.name == val1) :
                    return render(request,'result.html',{"warning":"username not available"})
            a=Login()
            a.name=val1
            a.password=val2
            a.save()
         except:
             print("not good")
    return render(request,'signin.html')
