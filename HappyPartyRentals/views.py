# En main/views.py
from django.shortcuts import render
from .models import Producto

def catalogo_productos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})


def index(request):
    # Otras operaciones de la vista...
    banner_image_url = '/static/_0a85ff57-75bc-4b34-9810-9c1440e08afc.jpg'
    return render(request, 'index.html', {'banner_image_url': banner_image_url})


def galeria(request):
    # Lógica para obtener las imágenes y videos de la galería
    # Puedes usar modelos de Django o simplemente pasar las rutas de los archivos como contexto.
    context = {
        'imagenes': ['ruta_imagen_1', 'ruta_imagen_2', ...],
        'videos': ['ruta_video_1', 'ruta_video_2', ...],
    }
    return render(request, 'galeria.html', context)
