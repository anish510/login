from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth  
from django.http import HttpResponse  
 


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        print(username,email,password,confirm_password)

        if password == confirm_password:
            if User.objects.filter(username = username,email = email).exists():
                messages.error(request, "Account already exists",extra_tags='danger')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username = username,email=email)
                user.set_password(password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.error(request, "Password not matching")
            return redirect('register')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        print(username,password)

        user = auth.authenticate(request, username = username ,password = password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("Login successfully")
            messages.success(request,"login success ")
            return redirect('home')
        else:
             print("login failed")
             return HttpResponse("Failed")
             messages.error(request, "Invalid Credentials")
             return redirect('login')
       
    return render(request, 'login.html')
    
    