from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

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
    