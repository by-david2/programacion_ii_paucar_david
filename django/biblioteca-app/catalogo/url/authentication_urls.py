from django.urls import path
from django.views.generic.base import RedirectView
from catalogo.views.authentication_views import BibliotecaLoginView, BibliotecaLogoutView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', BibliotecaLoginView.as_view(), name='login'),
    path('logout/', BibliotecaLogoutView.as_view(), name='logout'),
]