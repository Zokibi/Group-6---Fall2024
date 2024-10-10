from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                 'placeholder': ' Enter Username',
                 'class': 'form-input',
                 'style': 'height: 60px; width: 600px; background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['email'].widget.attrs.update({
                 'placeholder': ' Enter Email',
                 'class': 'form-input',
                 'style': 'height: 60px; width: 600px; background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['password1'].widget.attrs.update({
                 'placeholder': ' Enter Password',
                 'class': 'form-input',
                 'style': 'height: 60px; width: 600px; background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['password2'].widget.attrs.update({
                 'placeholder': ' Confirm Password',
                 'class': 'form-input',
                 'style': 'height: 60px; width: 600px; background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        

        