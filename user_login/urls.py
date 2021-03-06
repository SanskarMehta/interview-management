from django.contrib import admin
from django.urls import path,include
from user_login import views

urlpatterns = [
    path('register/',views.register,name='user-register'),
    path('login/',views.login,name='user-login'),
    path('interview_home/',views.interviewer_home,name="inter-home"),
    path('user_home/', views.user_home, name="user-home"),
]
