from rest_framework import serializers
from .models import Product,Category

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        # read_only_fields = ('__all__',)


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = ('__all__',)