from django.db import models

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class mecanica(models.Model):
    Automovil = models.CharField(max_length=100)
    Servicios = models.TextField(blank=True)
    Mantenimiento = models.TextField(blank=True)
    diagnostico_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Meca