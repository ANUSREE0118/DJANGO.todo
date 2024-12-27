from django.shortcuts import render,redirect
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
   
    
    
    
    all_todos=todo.objects.filter(user=request.user)
    context={
            'todos':all_todos
        }
    if request.method=='POST':
        task=request.POST.get('task')
        new_todo=todo(user=request.user,todo_name=task)
        new_todo.save()
        
        #to get every todo item created by this user currently logged in
        
        
        context ['todos']=all_todos
        
      
    return render( request,'todoapp/todo.html',context )

    

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username)
        if len(password) <5:
            messages.error(request,'password is too short! ')
           
            return redirect('register')
        #create  a new user with username email and new password and save it in backened
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfully created')
        
        #to check if the user is entering already registered name
        #if User.objects.filter(username = username).first():
           # messages.error(request, "This username is already taken")
        #return redirect('regiter')
        #get_all_users_by_username=User.object.filter(username=username)
        #if get_all_users_by_username:
           # messages.error(request,'username is already exist.Try another username')
           # return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'user successfully created')
        return redirect('loginpage')
            
    return render(request, 'todoapp/register.html',{})
def logoutview(request):
    logout(request)
    return redirect('loginpage')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        #check database if user exist or not if not then login
        validate_user=authenticate(username=username,password=password) #type the superuser name and password 
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
             messages.error(request,'username doesnot exist.wrong detail')
             return redirect('loginpage')
            
            
    return render(request,'todoapp/login.html',{})
@login_required
def DeleteTask(request,name):
    get_todo=todo.objects.get(user=request.user, todo_name=name)
    
    get_todo.delete()
    if(name==""):
         get_todo=todo.objects.get(user=request.user, todo_name=name)
    
        
         get_todo.delete()
        
        
    
    
    
    return redirect('home-page')
@login_required   
def Update( request, name):
    get_todo=todo.objects.get(user=request.user,todo_name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('home-page')
def notask(request,mane):
    get_to=todo.objects.get(user=request.user,todo_name="nj")
    
        
    get_to.delete()

    
    
    