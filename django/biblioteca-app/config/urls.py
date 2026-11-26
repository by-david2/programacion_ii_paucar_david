from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',
         include('catalogo.urls.authentication_urls')),
    path('catalogo/',
         include('catalogo.urls.categoria_urls')),
     path('catalogo/',
              include('catalogo.urls.libro_urls')),
    path('catalogo/',
         include('catalogo.urls.autor_urls')),
     path('', include('catalogo.urls.home_urls')),
     
]