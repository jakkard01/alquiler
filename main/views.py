# main/views.py
from django.shortcuts import render
from .models import Producto

# main/views.py
def index(request):
    productos_destacados = Producto.objects.filter(disponibilidad=True)[:3]
    print(productos_destacados)  # Añade esta línea
    return render(request, 'index.html', {'productos_destacados': productos_destacados})


def catalogo_productos(request):
    productos = Producto.objects.filter(disponibilidad=True)
    return render(request, 'catalogo.html', {'productos': productos})

# En main/views.py

def solicitud_alquiler(request):
    if request.method == 'POST':
        # Procesar el formulario de solicitud
        # Crear la instancia de Solicitud y guardarla en la base de datos
        pass  # Añade aquí el código necesario

    return render(request, 'solicitud.html')


# Nueva vista para la página de inicio
def inicio(request):
    # Añade aquí el código necesario para la página de inicio
    return render(request, 'inicio.html')


def galeria(request):
    context = {
        'imagenes': ['ruta_imagen_1', 'ruta_imagen_2', ...],
        'videos': ['ruta_video_1', 'ruta_video_2', ...],
    }
    return render(request, 'galeria.html', context)

