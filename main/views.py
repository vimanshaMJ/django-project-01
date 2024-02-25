from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

# Create your views here.
def index(response, name):
    ls = ToDoList.objects.get(name = name)
    item = ls.item_set.get(id = 1)
    return HttpResponse("<h1> %s </h1> <br> <p> %s </p>" % (ls.name, str(item.text)))


# filter - check an specific element 

# >>> t.filter(name__startswith="Vi")
# <QuerySet [<ToDoList: Vimsnsha's List>]>
# >>> t.filter(name__startswith="tim")
# <QuerySet []>