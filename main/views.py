from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import CreateNewList

from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id = id)

    # whenever you get a POST request from the server, all the information in the form in list.html will be passed to our view
    # we gonna get a dictionary like this: {"save": ["save"], "c1": ["clicked"]}  => c1 is the name of the input field, clicked is the value of the input field
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()


        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")
            
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
