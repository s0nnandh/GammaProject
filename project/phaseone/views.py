from django.shortcuts import render
from pyfcm import FCMNotification
from blog.models import Login
from .forms import TempForm
from .models import MessageForm
from django.contrib import messages


def home_view(request):
    form = TempForm(request.POST or None, request.FILES or None)
    if request.method =='POST':  
        val1= request.POST['num1']
        val2= request.POST['num2']
        val = Login.objects.all()
        print(val)
        idd=0
        ids=val.__len__()
        for x in val:
            idd=idd+1
            if(x.name == val1):
                if(x.password != val2):
                        return render(request,'signin.html')
                else:
                    idd=idd-1
                
        if(idd==ids):
            return render(request,'signin.html')

        if form.is_valid():            
            notify(form.cleaned_data)
            form.save()              
            form = TempForm() 
            messages.success(request, "Successfully created") 
    
    return render(request,"phaseone/home.html",{'form' : form})

def notify(form):
    print('a')
    push_service = FCMNotification(api_key="AAAAvHIUUss:APA91bElas2wl0uWdjmnQimvMQBgYX2XpFr75ilust04cMLFzbe04eoNSPMK-3wV8DAMhgX8hvQ0LGyEhw4sCzSFY0D3abUEVZM8BBy6yhPTViO_f35LJaBwgdjFCio0Y9bOq-sSnNfI")
    registeration_id = "euqOvvdDSKI:APA91bEKoIfxoqhWs6lQ_1FvlGFt6f5JcoPanu7oV2YI9RrEH9IbqScEIdjfC091TKsgIu73afyDaSsN8gzv_aylzb5rOZcekN3j9e_SYJU52O02bmvFxMfnlRLTFmOA6KJdeAzjkyrW"    
    message_title = form['header']
    print(message_title)
    message_body = form['text']
    result = push_service.notify_single_device(registration_id=registeration_id, message_title=message_title, message_body=message_body)
    print(result)

