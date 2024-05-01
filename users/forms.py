from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUserModel
from django import forms
from django.forms.widgets import EmailInput, TextInput, PasswordInput, NumberInput


# - Registeration form
class CreateUserForm(UserCreationForm):
    email = forms.CharField(widget=EmailInput(attrs={'placeholder': 'Your email',  'class': 'w-full p-3 outline-none border border-primaryGray rounded-md'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Your Password',  'class': 'w-full p-3 outline-none border border-primaryGray rounded-md'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm Password',  'class': 'w-full p-3 outline-none border border-primaryGray rounded-md'}))

    class Meta:
        model = CustomUserModel
        fields = ['email', 'password1', 'password2']


# - Login form
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email',  'class': 'w-full p-3 outline-none border border-primaryGray rounded-md', 'value': 'eseoseordia@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',  'class': 'w-full p-3 outline-none border border-primaryGray rounded-md'}))

    class Meta:
        model = CustomUserModel
        fields = ['email', 'password']

