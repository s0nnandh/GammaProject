from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from blog.models import Login
def home(request):
    return redirect('home/')
