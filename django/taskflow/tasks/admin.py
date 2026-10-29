from django.contrib import admin
from .models import Project, mecanica


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(mecanica)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("Automovil", 
                    "Servicios", 
                    "Mantenimiento",
                    "diagnostico_date")
    search_fields = ("Automovil",)
