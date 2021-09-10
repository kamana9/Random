from django.shortcuts import render
from .models import Task,User

# Create your views here.
def index(request):
    context={'success':False} 
    if request.method=='POST':
        t=request.POST.get('title')
        description= request.POST.get('task_description')
        print(t,description)
        ins= Task(title=t, task_description=description)
        ins.save()
        context={'success':True}
    return render(request,'todo/index.html',context)

def task(request):
    abc = Task.objects.all()
    
    context={
        'tasks': abc
        }
    return render(request,'todo/tasks.html',context)

def user(request):
    abc = User.objects.all()
    
    context={
        'user': bcd
        }
    return render(request,'todo/index.html',context)

