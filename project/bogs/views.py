from django.shortcuts import render,redirect
from .models import Person,Group,Membership
# Create your views here.
from .forms import SimpleForm
def course(request,ide):
    if not request.user.is_authenticated:
        return redirect('/login')
    profname=request.user
    form1 = SimpleForm()
    form2 = SimpleForm()
    l = []
    l2=[]
    grp=Group.objects.get(name=ide)


    
    if request.method =='POST': 
        dict=request.POST
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
    return render(request,'courses.html',{'form1':form1,'form2':form2,'course':ide})

def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    msg=""
    if request.method =='POST': 
        dict=request.POST
        grpname=dict['group_name']
        a=Group.objects.filter(prof=request.user).filter(name=grpname).exists()
        
        if (a)|(grpname==""):
            msg="course name already exists"
        else:
            Group.objects.create(name=grpname,prof=request.user)
        if (grpname==""):
            msg=""
    a=Group.objects.filter(prof=request.user)
    
    return render(request,'home.html',{'courses':a,'msg':msg}) 