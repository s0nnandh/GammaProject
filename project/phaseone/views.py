from django.shortcuts import render,redirect
from pyfcm import FCMNotification

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    
    return render(request,"phaseone/home.html",{'form' : 1})

'''def notify(form):
    print('a')
    push_service = FCMNotification(api_key="AAAAvHIUUss:APA91bElas2wl0uWdjmnQimvMQBgYX2XpFr75ilust04cMLFzbe04eoNSPMK-3wV8DAMhgX8hvQ0LGyEhw4sCzSFY0D3abUEVZM8BBy6yhPTViO_f35LJaBwgdjFCio0Y9bOq-sSnNfI")
    registeration_ids = [
        "euqOvvdDSKI:APA91bEKoIfxoqhWs6lQ_1FvlGFt6f5JcoPanu7oV2YI9RrEH9IbqScEIdjfC091TKsgIu73afyDaSsN8gzv_aylzb5rOZcekN3j9e_SYJU52O02bmvFxMfnlRLTFmOA6KJdeAzjkyrW",
        "euqOvvdDSKI:APA91bEKoIfxoqhWs6lQ_1FvlGFt6f5JcoPanu7oV2YI9RrEH9IbqScEIdjfC091TKsgIu73afyDaSsN8gzv_aylzb5rOZcekN3j9e_SYJU52O02bmvFxMfnlRLTFmOA6KJdeAzjkyrW"]  
    message_title = form['header']
    print(message_title)
    message_body = form['text']
    result = push_service.notify_multiple_devices(registration_ids=registeration_ids, message_title=message_title, message_body=message_body)
    print(result)'''
def null(request):
    return redirect("blog/")
