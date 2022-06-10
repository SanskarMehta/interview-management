from django.urls import path
from user_login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='user-register'),
    path('login/',views.login,name='user-login'),
    path('interview_home/',views.interviewer_home,name="inter-home"),
    path('user_home/', views.user_home, name="user-home"),
    path('user_details_register/',views.user_application_form,name='user-details-form'),
    path('interviewer_details_register/',views.interviewer_application_form,name='interviewer-details-form'),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
