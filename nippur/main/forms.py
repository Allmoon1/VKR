from dataclasses import fields
from xml.dom.minidom import Attr
from .models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','username', 'password', 'r_password']
        widgets = { 
            'email': EmailInput(attrs = {"class": "myfield", 'placeholder':'Email'}),
            'username': TextInput(attrs = {'class': 'myfield', 'placeholder':'Username'}),
            'password': PasswordInput(attrs = {'class': 'myfield', 'placeholder':'Password'}),
            'r_password': PasswordInput(attrs = {'class': 'myfield', 'placeholder':'Repeat password'}),
            }
