from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

# Create your views here.
def index(response, name):
    ls = ToDoList.objects.get(name = name)
    item = ls.item_set.get(id = 1)
    return HttpResponse("<h1> %s </h1> <br> <p> %s </p>" % (ls.name, str(item.text)))


# >>> del_object = t.get(id=1)
# >>> del_object.delete()
# (2, {'main.Item': 1, 'main.ToDoList': 1})
# >>> t.filter(id=2)
# <QuerySet []>
# >>> t.all()
# <QuerySet []>
# >>> t1 = ToDoList(name="First List")
# >>> t1.save()
# >>> t2 = ToDoList(name="Second List")
# >>> t2.save()