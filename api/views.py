from .models import Producto
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import ProductoSerializer

#Conjunto de vistas para el CRUD del modelo ejemplo
class ProductoViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo producto, admite
    GET,POST, PUT, PATCH, DELETE
    """
    queryset = Producto.objects.all().order_by('-nombre')
    serializer_class = ProductoSerializer