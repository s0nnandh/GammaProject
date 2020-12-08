from django.shortcuts import render,redirect
from .models import Person,Group,Membership,MessageForm,Messageship,Message_seen
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer,GroupSerializer,MessageSerializer,Mess
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .forms import SimpleForm
from django.utils import timezone
from phaseone.forms import TempForm
from django.http import Http404
from rest_framework.views import APIView
from pyfcm import FCMNotification
from datetime import datetime
from django.contrib.auth.models import User

def manage(request,ide):
    if not request.user.is_authenticated:
        return redirect('/login')
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    profname=request.user
    form1 = SimpleForm()
    form2 = SimpleForm()
    l = []
    l2=[]
    grp1=Group.objects.filter(grp_name=ide,prof=request.user).exists()
    if grp1:
        grp=Group.objects.get(grp_name=ide,prof=request.user)
    else:
        return redirect('/blog')
    if grp.bool == 1 :
        if request.method =='POST': 
            dict=request.POST
            print(dict)
            a=dict.getlist('student')
            if 'add' in dict:
                for studentid in a:
                    per=Person.objects.get(userid=studentid)
                    if grp.members.all().filter(userid=studentid).exists() :
                        print("exists")
                    else :
                        Membership.objects.create(person=per,group=grp)
            if 'remove' in dict:
                for studentid in a:
                    per=Person.objects.get(userid=studentid)
                    grp.members.remove(per)

        a=Person.objects.all()
        members=grp.members.all()
        for x in a:
            if x not in members:
                l2.append((x.userid,str(x.userid)+"         "+str(x.name)))
        form2.fields['student'].choices = l2
        for x in members:
                l.append((x.userid,str(x.userid)+"     "+str(x.name)))
        form1.fields['student'].choices = l
        return render(request,'manage_students.html',{'form1':form1,'form2':form2,'course':ide})
    else :
        return render(request,'manager.html')
def ta(request,ide):
    if not request.user.is_authenticated:
        return redirect('/login')
    print("********************************************")
    profname=request.user
    form1 = SimpleForm()
    form2 = SimpleForm()
    l = []
    l2=[]
    grp1=Group.objects.filter(grp_name=ide,prof=request.user).exists()
    if grp1:
        grp=Group.objects.get(grp_name=ide,prof=request.user)
    else:
        return redirect('/blog')
    if grp.bool == 1 :
        if request.method =='POST': 
            dict=request.POST
            print(dict)
            a=dict.getlist('student')
            if 'add' in dict:
                for studentid in a:
                    per=Person.objects.get(userid=studentid)
                    name=str(ide)+str(per.userid)
                    if Group.objects.filter(grp_name=ide,prof=per.userid).exists() :
                        print("exists")
                    else:
                         Group.objects.create(bool=0,prof=studentid,grp_name=ide,name=name)
                    if User.objects.filter(username=studentid).exists():
                        print("exists1")
                    else :
                        User.objects.create_user(studentid, per.email, per.password)
            if 'remove' in dict:
                for studentid in a:
                    Group.objects.filter(grp_name=ide,prof=studentid).delete()
                    

        a=Person.objects.all()
        l=[]
        l2=[]
        
        for x in a:
            l2.append((x.userid,str(x.userid)+"         "+str(x.name)))
        form2.fields['student'].choices = l2

        for x in Group.objects.filter(grp_name=ide):
            if Person.objects.filter(userid=x.prof).exists():
                per=Person.objects.get(userid=x.prof)
                print(per)
                l.append((per.userid,str(per.userid)+"         "+str(per.name)))

        form1.fields['student'].choices = l

        return render(request,'manage_ta.html',{'form1':form1,'form2':form2,'course':ide})
    else :
        return render(request,'manager.html')

def course(request,ide):
        if not request.user.is_authenticated:
            return redirect('/login')
       

        grp1=Group.objects.filter(grp_name=ide,prof=request.user).exists()
        if grp1:
            grp=Group.objects.get(grp_name=ide,prof=request.user)
        else:
          return redirect('/blog')
        
        b=request.POST
        print(b)
        form = TempForm(request.POST or None, request.FILES or None)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")

        if request.method =='POST': 
            if "delete" in b:
                MessageForm.objects.get(printer=b['delete']).delete()
            else:
                if form.is_valid(): 
                    timezone.activate('Asia/Kolkata')
                    time=datetime.utcnow()
                    messenger = request.user
                    print(messenger)
                    printer=str(messenger)+"         "+str(time)
                    MessageForm.objects.create(time=time,header=b['header'],text=b['text'],priority=b['priority'],printer=printer)
                    print(timezone.now())

                    message=MessageForm.objects.get(printer=printer)
                    x = Group.objects.get(name=ide)
                    Messageship.objects.create(group=x,form2=message)

                    push_service = FCMNotification(api_key="AAAAff-npZk:APA91bEYHRssroImVg-vG_RlUrRyn-bSps85URjpiNBNcYpJ4ijjSlnsc1NmmftqO1G0pp_TbCS07PGXL5Fx7vDC2uttICAUeCE_bwB_r5aHuH3wwWcmZQxgoekbbX9JPO3hXlnWKW_X")
                    registration_ids = []
                    for x in grp.members.all():
                        if x.Token_key != '0' :
                            registration_ids.append(x.Token_key)
                    print(registration_ids)
                    message_title = b['header']
                    print(message_title)
                    message_body = b['text']
                    priority = b['priority']
                    if (priority == '1' or priority == '2'):
                        print(priority)
                        result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body,sound="Default",content_available=True)
                    else:
                        result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body,sound="Default",low_priority=True)
                    print(result)
                    form = TempForm()      
        
        bool = grp.bool
        if bool :
            messages= grp.messages.all()
        else :
            grp = Group.objects.get(name=ide)
            messages=grp.messages.all()
        return render(request,'courses.html',{ 'course' : ide , 'messages' : messages ,'form':form,'bool':bool})
def seen(request,ide,msg):
    if not request.user.is_authenticated:
        return redirect('/login')
    grp1=Group.objects.filter(grp_name=ide,prof=request.user).exists()
    if grp1:
        a1=Group.objects.get(name=ide).messages.filter(printer=msg).exists()
        if a1 :
             a=MessageForm.objects.get(printer=msg)
        else :
            return redirect('/blog')      
    else:
        return redirect('/blog')
    a=MessageForm.objects.get(printer=msg)
    seen = a.seen.all()
    print(seen)
    return render(request,'seen.html',{'seen':seen})

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    msg=""
    if request.method =='POST': 
        dict=request.POST
        grpname=dict['group_name']
        grpname=str(grpname)+" "+str(request.user)
        a=Group.objects.filter(prof=request.user).filter(name=grpname).exists()
        if a :
            msg="course name already exists"
        elif grpname!="":
            Group.objects.create(name=grpname,prof=request.user,grp_name=grpname)
    a=Group.objects.filter(prof=request.user)
    print(a)
    bool=0
    for x in a:
        bool=x.bool

    return render(request,'home.html',{'courses':a,'msg':msg,'bool' : bool}) 

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = MessageForm.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageForm.objects.all()
    serializer_class = MessageSerializer


class MessList(generics.ListCreateAPIView):
    queryset = Message_seen.objects.all()
    serializer_class = Mess

class MessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message_seen.objects.all()
    serializer_class = Mess