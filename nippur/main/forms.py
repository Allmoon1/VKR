from dataclasses import fields
from msilib.schema import ListView
from xml.dom.minidom import Attr
from .models import User, Song
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','username', 'password', 'r_password']
        widgets = { 
            'email': EmailInput(attrs = {"class": "myfield", 'placeholder':'Email'}),
            'username': TextInput(attrs = {'class': 'myfield', 'placeholder':'Username'}),
            'password': PasswordInput(attrs = {'class': 'myfield', 'placeholder':'Password'}),
            'r_password': PasswordInput(attrs = {'class': 'myfield', 'placeholder':'Repeat password'}),
            }
class UserAuthorizationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = { 
            'username': TextInput(attrs = {'class': 'myfield', 'placeholder':'Username'}),
            'password': PasswordInput(attrs = {'class': 'myfield', 'placeholder':'Password'})
            }
