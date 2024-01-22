# main/admin.py

from django.contrib import admin
from .models import Galeria

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_descripcion')  # Agrega los campos que quieras mostrar en la lista

    def mostrar_descripcion(self, obj):
        return obj.descripcion  # Reemplaza 'descripcion' con el nombre real del campo en tu modelo

    mostrar_descripcion.short_description = 'Descripción'  # Puedes personalizar el encabezado en la lista

admin.site.register(Galeria, GaleriaAdmin)
