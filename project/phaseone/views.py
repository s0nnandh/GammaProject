from django.shortcuts import render

from .forms import TempForm
from .models import MessageForm
from django.contrib import messages

# Create your views here.

def home_view(request):
    form = TempForm(request.POST or None, request.FILES or None)
    if request.method =='POST':         
        if form.is_valid():
            form.save()              
            form = TempForm() 
            messages.success(request, "Successfully created") 
    
    return render(request,"phaseone/home.html",{'form' : form})
