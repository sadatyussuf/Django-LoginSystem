
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                "type":"password",
                'placeholder': 'Password',
                "class":"form-control form-control-lg",
            }),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                "type":"password",
                'placeholder': 'Confirm Password',
                "class":"form-control form-control-lg",
            }),

        strip=False,
    )
    class Meta:
        model = User
        fields = ['username', "password1",'password2']
        widgets = {
            "username": TextInput(attrs={
                "type":"text",
                'placeholder': 'Username',
                "class":"form-control form-control-lg",
            }),

        }
        labels = {
            "username":"Username",
        }

class AuthenticateUserForm(AuthenticationForm):
    username = forms.CharField(
        label=("Username"),
        widget=forms.TextInput(attrs={
                "type":"text",
                'placeholder': 'Username',
                "class":"form-control form-control-lg",
            }),

        strip=False,
    )
    password = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                "type":"password",
                'placeholder': 'Password',
                "class":"form-control form-control-lg",
            }),

        strip=False,
    )
    class Meta:
        model = User
        fields = ['username','password']
