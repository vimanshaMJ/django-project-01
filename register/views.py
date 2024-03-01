from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm  #UserCreationForm-used to create new user

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()  #saves the user in the user's database

        return redirect("/home")
    
    else:
        form = UserCreationForm()

    return render(response, "register/base.html", {"form": form})
