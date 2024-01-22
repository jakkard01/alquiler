# En main/models.py
from django.db import models
from django.utils.text import slugify


class Producto(models.Model):
    categoria = models.CharField(max_length=255, default='Sin categoría')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    disponibilidad = models.BooleanField(default=True)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)

class Solicitud(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_evento = models.DateTimeField()
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)


# main/models.py

class Galeria(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # Otros campos...

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre