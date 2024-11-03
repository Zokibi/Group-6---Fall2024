from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Restaurant, Item

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                 'placeholder': ' Enter Username',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['email'].widget.attrs.update({
                 'placeholder': ' Enter Email',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['first_name'].widget.attrs.update({
                 'placeholder': ' Enter First Name',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white',
                 'class': 'name-input',
            })
            self.fields['last_name'].widget.attrs.update({
                 'placeholder': ' Enter Last Name',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white',
                 'class': 'name-input',
            })
            self.fields['password1'].widget.attrs.update({
                 'placeholder': ' Enter Password',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['password2'].widget.attrs.update({
                 'placeholder': ' Confirm Password',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']

class CreateLoginForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                 'placeholder': ' Enter Username',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['password'].widget.attrs.update({
                 'placeholder': ' Enter Password',
                 'class': 'form-input',
                 'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
     class Meta:
           model = User
           fields = ['username' , 'password']

class SaveRestaurantProfile(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({
                  'placeholder': ' Restaurant Name',
                  'class': 'form-input',
                  'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
            self.fields['numTables'].widget.attrs.update({
                  'placeholder': ' Number of Tables',
                  'class': 'form-input',
                  'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
            })
      class Meta:
            model = Restaurant
            fields = ['name', 'numTables']

class AddMenuItem(forms.ModelForm):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['itemName'].widget.attrs.update({
               'placeholder': ' Item Name',
               'class': 'form-input',
               'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
          })
          self.fields['price'].widget.attrs.update({
               'placeholder': ' Item Price',
               'class': 'form-input',
               'style': 'background-color: transparent; border: 1px white solid; border-radius: 5px; font-size: 20px; color: white'
          })
     class Meta:
           model = Item
           fields = ['itemName', 'price']