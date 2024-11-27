from django.db import models

# Create your models here.
class Producto(models.Model):
    """
    Modelo que representa la estructura de datos de un 
    registro correspondiente a un producto en base de datos
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=50)