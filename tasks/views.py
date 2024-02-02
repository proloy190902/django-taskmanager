from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime,timedelta
from django.utils import timezone

# Create your views here.
from rest_framework import generics

from tasks import models
from .serializers import TaskSerializer

# show all tasks
class ListTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

# show individual task
class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

# create individual task
class CreateTask(generics.CreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

# update individual task
class UpdateTask(generics.UpdateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    
# delete individual task
class DeleteTask(generics.DestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer    

@login_required(login_url='/login/')
def index(request):
    tasks = models.Task.objects.all().order_by('-createdAt')
    
    user=request.user
    if request.method == "POST": 
            #checking if the request method is a POST
            if "taskAdd" in request.POST: #checking if there is a request to add a todo
                title = request.POST["title"] #title
                description=request.POST["description"]
                dueDate = request.POST["dueDate"]
                priority = request.POST["priority"] 
                isComplete=bool(False)
                taskImage=request.FILES["taskImage"]
                dueDate = datetime.fromisoformat(dueDate)
                dueDate -= timedelta(hours=6)
                task = models.Task(title=title,description=description,taskImage=taskImage,dueDate=dueDate,user=user,priority=priority,isComplete=isComplete)
                task.save() 
                return redirect("/") 
     
                            
    return render(request, 'index.html',{"tasks":tasks})

@login_required(login_url='/login/')
def details(request,item_id):
    task=models.Task.objects.get(id=item_id)
    user=request.user
    if "taskUpdate" in request.POST: #checking if there is a request to add a todo
                title = request.POST["title"] #title
                description=request.POST["description"]
                dueDate = str(request.POST["dueDate"]) 
                priority = request.POST["priority"] 
                isComplete=request.POST.get('isComplete',False)
                dueDate = datetime.fromisoformat(dueDate)
                dueDate -= timedelta(hours=6)
                if isComplete=="on":
                      isComplete=bool(True)
                else:
                      isComplete=bool(False)

                taskImage=request.FILES["taskImage"] if 'taskImage' in request.FILES else None

                if(title):
                      task.title=title
                if(description):
                      task.description=description
                if(dueDate):
                      task.dueDate=dueDate
                if(priority):
                      task.priority=priority
                if(taskImage):
                      task.taskImage=taskImage  
                task.user=user 
                task.isComplete=isComplete
                task.updatedAt=timezone.localtime()
                task.save() 
                return redirect("/") 
    if "taskDelete" in request.POST: 
                    task = models.Task.objects.get(id=item_id) 
                    task.delete() 
                    return redirect("/")
    return render(request,"detail.html",{"task":task})

def login_page(request):
      if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            if  not User.objects.filter(username=username).exists():
                  messages.error(request,"Invalid username")
                  return redirect('/login/')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request,user)
                    return redirect('/')
                  
            else:
                messages.error(request,'Invalid password')
                return redirect('/login/')
              
            
      return render(request,"login.html")

def signup_page(request):
      if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            
            if  User.objects.filter(username=username).exists():
                  messages.success(request, "Username already taken.")
                  return redirect('/signup/')

            user=User.objects.create(
                    username=username,
                    email=email
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Account created successufully!")
            return redirect('/signup/')
      
      return render(request,"signup.html")

def logout_page(request):
      logout(request)
      return redirect('/login/')