from django.urls import path
from ..views import libro_views
from catalogo.views import create_libro, libro_list, delete_libro, update_libro

from catalogo.views import libro_views


urlpatterns = [
    path('', libro_views.libro_list, name='libro_list'),
    path('crear/', libro_views.create_libro, name='libro_create'),
    path('<int:pk>/editar/', libro_views.update_libro, name='libro_update'),
    path('<int:pk>/eliminar/', libro_views.delete_libro, name='libro_delete'),
]   