from django.shortcuts import render
from django.http import HttpResponse


def about_screen(request):
    return render(request,'home/base.html')
    # return render(request,'index.html')
