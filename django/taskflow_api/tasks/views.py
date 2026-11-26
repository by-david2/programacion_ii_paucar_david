from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Project, Task



def listas(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "tasks/home.html", contexto)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def home(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)
# Create your views here.
def register(request):
    """Registro de usuatios"""
    return HttpResponse("Registro de Usuario en linea")

def admin(request):
    "Usuario supremo"
    return HttpResponse("Soy el admin supremo respeta")

def greeting(request, nombre):
    "registro de ususario"
    return HttpResponse(
        f"hola {nombre}, bienvenido a taskflow")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my_first_template.html", 
                  contexto)

def leads_like(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/leads_like.html", 
                  contexto)