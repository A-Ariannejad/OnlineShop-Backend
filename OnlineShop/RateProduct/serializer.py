from rest_framework import serializers
from .models import RateProduct
from Products.serializer import ProductSerializer
from Users.serializer import CustomUserSerializer

class RateProductCreateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = RateProduct
        fields = ['id', 'product', 'user', 'rate', 'create_date']
        read_only_fields = ['id', 'create_date']


class RateProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = RateProduct
        fields = ['id', 'product', 'user', 'rate', 'create_date']
        
        
        