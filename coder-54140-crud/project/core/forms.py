from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Name'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Password'  # Cambié esto a 'Password' en lugar de 'Email'
        })
    )
   
   # class Meta:
   #     model = User
   #     fields = ["username", "password"]

      

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2","email","first_name","last_name"]
    