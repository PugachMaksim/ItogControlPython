from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        #
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     # 'password1': forms.PasswordInput(
        #     #     attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}),
        #     # 'password2': forms.PasswordInput(
        #     #     attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}),
        # }
