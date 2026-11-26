from django.contrib import admin
from .models import Project
from .models import Veterinario


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Veterinario)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created_at")
    search_fields = ("nombre",)