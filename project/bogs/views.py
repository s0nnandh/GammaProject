from django.shortcuts import render,redirect
from .models import Person,Group,Membership
# Create your views here.
from .forms import SimpleForm
def course(request,ide):
    if not request.user.is_authenticated:
        return redirect('/login')
    print(ide)
    profname=request.user
    form = SimpleForm()
    form.ide=ide
    if request.method =='POST': 
        dict=request.POST
        a=dict.getlist('student')
        print(dict)
        grp=Group.objects.get(name=ide)
        print(grp.members.all())
        if 'add' in dict:
            for studentid in a:
                per=Person.objects.get(userid=studentid)
                Membership.objects.create(person=per,group=grp,invite_reason=0)
        if 'remove' in dict:
            for studentid in a:
                per=Person.objects.get(userid=studentid)
                grp.members.remove(per)

    return render(request,'courses.html',{'form':form,'course':ide})

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
        else:
            Group.objects.create(name=grpname,prof=request.user)
    a=Group.objects.filter(prof=request.user)
    print(a)
    return render(request,'home.html',{'courses':a,'msg':msg}) 