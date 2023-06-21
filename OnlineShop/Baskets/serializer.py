from rest_framework import serializers
from .models import Basket, BasketMTMProduct
from Products.serializer import ProductSerializer
from Users.serializer import CustomUserSerializer
from Products.models import Product

class BasketMTMProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = BasketMTMProduct
        fields = ['id', 'basket', 'product', 'quantity']
        read_only_fields = ['id', 'basket']


class BasketSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    products = BasketMTMProductSerializer(source='ps', many=True)
    class Meta:
        model = Basket
        fields = ['id', 'user', 'products', 'total_price', 'order_address']
        read_only_fields = ['id', 'total_price']


class BasketAddProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class BasketViewProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class BasketRemoveProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()