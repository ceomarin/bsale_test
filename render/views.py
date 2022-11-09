from django.shortcuts import render
from .models import Product, Category
from rest_framework import viewsets,permissions
from .serializers import ProductoSerializer,CategoriaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', ]

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', ]

    def get_queryset(self):
        # productos = Product.objects.select_related()
        productos = Product.objects.all()

        nombre = self.request.GET.get('name')
        categoria_id = self.request.GET.get('category')

        # if nombre:
        #     # productos = productos.filter(nombre__contains=nombre)
        if categoria_id:
            productos = productos.filter(category=categoria_id)
            return productos
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
            return productos
            
        return productos
