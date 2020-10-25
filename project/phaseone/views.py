from django.shortcuts import render
from pyfcm import FCMNotification

from .forms import TempForm
from .models import MessageForm
from django.contrib import messages

# Create your views here.

proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }

def home_view(request):
    form = TempForm(request.POST or None, request.FILES or None)
    if request.method =='POST':         
        if form.is_valid():
            notify(form)
            form.save()              
            form = TempForm() 
            messages.success(request, "Successfully created") 
    
    return render(request,"phaseone/home.html",{'form' : form})

def notify(form):
    push_service = FCMNotification(api_key="AAAAvHIUUss:APA91bElas2wl0uWdjmnQimvMQBgYX2XpFr75ilust04cMLFzbe04eoNSPMK-3wV8DAMhgX8hvQ0LGyEhw4sCzSFY0D3abUEVZM8BBy6yhPTViO_f35LJaBwgdjFCio0Y9bOq-sSnNfI")
    registeration_id = "euqOvvdDSKI:APA91bEKoIfxoqhWs6lQ_1FvlGFt6f5JcoPanu7oV2YI9RrEH9IbqScEIdjfC091TKsgIu73afyDaSsN8gzv_aylzb5rOZcekN3j9e_SYJU52O02bmvFxMfnlRLTFmOA6KJdeAzjkyrW"
    message_title = "Hi"
    message_body = "Hello"
    result = push_service.notify_single_device(registration_id=registeration_id, message_title=message_title, message_body=message_body)
    print(result)

