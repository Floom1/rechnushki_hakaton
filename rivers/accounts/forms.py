from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput())
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(),)

    class Meta:
        model = User
        fields = ['username', 'email']
