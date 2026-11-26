# tasks/urls.py
from django.urls import path
from . import views

app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("my-first-template",     
          views.my_first_template, name="my-first-template.html"),
    path("leads-like",
          views.leads_like,name="leads-like.html"),
    path("tasks/lista",
          views.listas,
          name="task-lista"),
    path("tasks/new/", views.task_create, name="task-create"),
     ]