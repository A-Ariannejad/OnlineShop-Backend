from rest_framework import serializers
from .models import Product
from Stores.serializer import StoreSerializer

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'bio', 'create_date', 'amount', 'price', 'type']
        read_only_fields = ['id', 'create_date']


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'image', 'bio', 'create_date', 'amount', 'sold_amount', 'price', 'rate', 'rate_number', 'type']
        
        