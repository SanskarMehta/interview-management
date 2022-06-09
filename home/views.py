from django.shortcuts import render
from django.http import HttpResponse

def about_screen(request):
    return HttpResponse('Hello World')
    # return render(request,'index.html')
