from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UploadImg

class ImageForm(forms.ModelForm):
    class Meta:
        model =UploadImg
        fields="__all__"

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

