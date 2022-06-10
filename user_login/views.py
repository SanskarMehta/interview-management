from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser , user_details , interviewer_details
from django.contrib.auth.models import auth
from .forms import User_Details , Interviewer_Details

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['confirm_password']

        if password == confirm_pass:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username is already is taken.')
                return redirect('user-register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email is already exist.')
                return redirect('user-register')
            else:
                user = CustomUser.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.info(request, 'User is created')
        else:
            messages.info(request, "Your password's are not matching so you unable to create account.")
            return redirect('user-register')
        return redirect('user-login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.Is_interviewer:
                auth.login(request, user)
                if user.Is_first_time:
                    return redirect('interviewer-details-form')
                else:
                    return redirect("inter-home")
            else:
                auth.login(request, user)
                if user.Is_first_time:
                    return redirect("user-details-form")
                else:
                    return redirect("user-home")
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def interviewer_home(request):
    return render(request, "interviewer.html")


def user_home(request):
    return render(request, "user.html")


def user_application_form(request):
    if request.method == "POST":
        user_phone = request.POST['mobilenumber']
        user_technology = request.POST['technology']
        user_10th_marks = request.POST['marks_10th']
        user_12th_marks = request.POST['marks_12th']
        user_CPI = request.POST['cpi']
        user_CV = request.FILES['cvfile']

        if float(user_10th_marks) <= 100 and float(user_12th_marks) <= 100 and float(user_CPI) <=10 :
            if user_CV.content_type == 'application/pdf' or user_CV.content_type == 'application/msword' :
                userdetails = user_details.objects.create(user=request.user, user_phone=user_phone, user_technology=user_technology, user_10th_marks=user_10th_marks, user_12th_marks=user_12th_marks, user_CPI =user_CPI, user_CV=user_CV)
                userdetails.save()
                user = CustomUser.objects.get(id = request.user.id)
                user.Is_first_time = False
                user.save()
                return redirect('user-home')
            else:
                messages.info(request, "Please Upload .PDF or .DOC file")
                return render(request, 'user_details_form.html')
        else:
            messages.info(request, "Your result must be less than or equal to 100")
            return render(request, 'user_details_form.html')
    else:
        return render(request, 'user_details_form.html')


def interviewer_application_form(request):
    if request.method == "POST":
        interviewer_phone = request.POST['mobilenumber']
        interviewer_tech= request.POST['technology']
        interviewer_job_role= request.POST['job_role']
        interviewer_experience= request.POST['experience']

        inter = interviewer_details.objects.create(interviewer=request.user, interviewer_phone=interviewer_phone, interviewer_job_role=interviewer_job_role, interviewer_technology=interviewer_tech, interviewer_experience=interviewer_experience)
        inter.save()
        user = CustomUser.objects.get(id=request.user.id)
        user.Is_first_time = False
        user.save()
        return redirect('inter-home')
    else:
        return render(request, 'interviewer_details_form.html')

