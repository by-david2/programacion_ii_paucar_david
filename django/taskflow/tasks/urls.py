from django.urls import path
from . import views

app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("me", views.me, name="me"),
    path("saludo/<str:nombre>/",
         views.greeting, name= "saludo"),
    path("my-first-template",
         views.my_firts_template, name="my-firts-template.html"),
    path("leads-like",
         views.leads_like, name="leads-like.html"),
]