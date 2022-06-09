from django.contrib.auth.forms import UserCreationForm,forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class User_Details(forms.ModelForm):
    class Meta:
        model = user_details
        fields = "__all__"