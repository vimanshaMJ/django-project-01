from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import CreateNewList

from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id = id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)  # take all the data from the form and put it in the form variable

        if form.is_valid():
            n = form.cleaned_data["name"]  # access that data by using it like a dictionary, "name" is related to the name of the input field
            t = ToDoList(name = n) 
            t.save()
            # cleaned_data - cleanup the data un-encrypted

        return HttpResponseRedirect("/%i" %t.id)

    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
