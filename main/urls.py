# main/urls.py

from django.urls import path
from .views import index, catalogo_productos, solicitud_alquiler, inicio
from .views import galeria


urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('catalogo/', catalogo_productos, name='catalogo'),
    path('solicitud/', solicitud_alquiler, name='solicitud_alquiler'),
    path('inicio/', inicio, name='inicio'),
    path('galeria/', galeria, name='galeria'),

    # Puedes agregar más rutas según sea necesario
]

