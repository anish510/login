from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('confirm_password')
        print(username,email,password,confirm_password)

        if password == confirm_password:
            if User.objects.filter(username = username,email = email).exists():
                messages.info(request, "Account already exists")
                return redirect('register')
            else:
                
                user = User.objects.create_user(username = email ,email=email, password=password)
                user.save()
                print("user created")
                return redirect('register')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    
    return render(request, 'register.html')
    
    