from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # allow us to change some of the parent properties on this class
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] 
        # fields:layout where I want my fields to be 
        # "username", "password1", "password2" : already built into the UserCreationForm

        