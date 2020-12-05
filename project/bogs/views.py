from django.shortcuts import render,redirect
from .models import Person,Group,Membership,MessageForm,TempForm,Messageship
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer,GroupSerializer,MessageSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .forms import SimpleForm
from django.utils import timezone
from phaseone.models import MessageForm 

def manage(request,ide):
    if not request.user.is_authenticated:
        return redirect('/login')
    profname=request.user
    form1 = SimpleForm()
    form2 = SimpleForm()
    l = []
    l2=[]
    grp=get_object_or_404(Group, name=ide,prof=request.user)


    
    if request.method =='POST': 
        dict=request.POST
        print(dict)
        a=dict.getlist('student')
        if 'add' in dict:
            for studentid in a:
                per=Person.objects.get(userid=studentid)
                Membership.objects.create(person=per,group=grp,invite_reason=0)
        if 'remove' in dict:
            for studentid in a:
                per=Person.objects.get(userid=studentid)
                grp.members.remove(per)

    a=Person.objects.all()
    members=grp.members.all()
    for x in a:
        if x not in members:
            l2.append((x.userid,x.name))
    form2.fields['student'].choices = l2
    for x in members:
        l.append((x.userid,x.name))
    form1.fields['student'].choices = l
    return render(request,'manage_students.html',{'form1':form1,'form2':form2,'course':ide})

def course(request,ide):
    
        grp=get_object_or_404(Group, name=ide,prof=request.user)
        b=request.POST
        form = TempForm(request.POST or None, request.FILES or None)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")

        if request.method =='POST':     
            if form.is_valid(): 
                time=timezone.now()
                MessageForm.objects.create(time=time,header=b['header'],text=b['text'],priority=b['priority'])
                print(timezone.now())
                message=MessageForm.objects.get(time=time)
                Messageship.objects.create(group=grp,form2=message)
                form = TempForm()      
        
        
        messages = grp.messages.all()
        
        return render(request,'courses.html',{ 'course' : ide , 'messages' : messages ,'form':form})

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    msg=""
    if request.method =='POST': 
        dict=request.POST
        grpname=dict['group_name']
        a=Group.objects.filter(prof=request.user).filter(name=grpname).exists()
        if a :
            msg="course name already exists"
        elif grpname!="":
            Group.objects.create(name=grpname,prof=request.user)
    a=Group.objects.filter(prof=request.user)
    print(a)
    
    return render(request,'home.html',{'courses':a,'msg':msg}) 

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