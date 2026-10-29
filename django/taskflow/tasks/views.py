from django.shortcuts import redirect, render

from django.http import HttpResponse

from .forms import ProjectForm
from .models import Project


def home(request):
    projects = Project.objects.order_by("-created_at")
    return render(request, "tasks/home.html", {"projects": projects})


def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:home")
    else:
        form = ProjectForm()

    return render(request, "tasks/project_form.html", {"form": form})

def register(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Registro de usuarios en linea")

def me(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("El mas pro")

def greeting(request, nombre):
    "registro de usuario"
    return HttpResponse(
        f"hola {nombre}, bienvenido a taskflow"
    )

def my_firts_template(request):
    contexto = {
        "titulo": "Taskflow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar"
        }
    return render(request, "tasks/my-firts-template.html",
                  contexto)

def leads_like(request):
    contexto = {
        "titulo": "Taskflow",
        "mensaje": "Organiza tus tareas y proyectos en un solo lugar",
    }
    return render(request, "leads/leads-like.html",
                  contexto)
    