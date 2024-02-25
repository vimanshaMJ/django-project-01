from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>", views.index, name="index"),
]

# <int:id> : we're gonna look for some integer in our path and we're gonna pass that to the function views.index