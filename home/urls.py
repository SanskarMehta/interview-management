from django.urls import path
from home import views

urlpatterns = [
    path('', views.about_screen, name='main-home')
]
