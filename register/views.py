from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm  #UserCreationForm-used to create new user

# Create your views here.
def register(response):
    form = UserCreationForm()
    return render(response, "register/base.html", {"form": form})
