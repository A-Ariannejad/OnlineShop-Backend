from rest_framework import serializers
from .models import CommentProduct
from Products.serializer import ProductSerializer
from Users.serializer import CustomUserSerializer

class CommentProductCreateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = CommentProduct
        fields = ['id', 'product', 'user', 'comment', 'create_date']
        read_only_fields = ['id', 'create_date']


class CommentProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = CommentProduct
        fields = ['id', 'product', 'user', 'comment', 'create_date']
        
        
        