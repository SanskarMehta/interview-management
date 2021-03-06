from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.models import auth

def register(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_pass=request.POST['confirm_password']

        if password==confirm_pass:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,'Usename is already is taken.')
                return redirect('user-register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Email is already exist.')
                return redirect('user-register')
            else:
                user=CustomUser.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.info(request,'User is created')
        else:
            print("Your password's are not matching so you unable to create account.")
            return redirect('user-register')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        # print(user.Is_interviewer)
        # user_id=user.id
        # print(type(user_id))

        if user is not None:
            if user.Is_interviewer:
                print('interviewer')
                auth.login(request,user)
                return redirect('inter-home')
            else:
                return redirect("user-home")
        else:
            messages.info(request,'invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def interviewer_home(request):
    return render(request,"interviewer.html")

def user_home(request):
    return render(request,"user.html")