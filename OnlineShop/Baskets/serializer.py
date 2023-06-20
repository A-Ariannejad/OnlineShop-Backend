from rest_framework import serializers
from .models import Basket, BasketMTMProduct
from Products.serializer import ProductSerializer
from Users.serializer import CustomUserSerializer


class BasketMTMProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketMTMProduct
        fields = ['id', 'basket', 'product', 'quantity']
        read_only_fields = ['id', 'basket']


class BasketMTMProductShowSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = BasketMTMProduct
        fields = ['id', 'basket', 'product', 'quantity']
        read_only_fields = ['id', 'basket']

class BasketSerializer(serializers.ModelSerializer):
    products = BasketMTMProductShowSerializer(many=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'products', 'total_price', 'order_address']
        read_only_fields = ['id', 'basket']