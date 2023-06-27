from rest_framework import serializers
from .models import RateStore
from Stores.serializer import StoreSerializer
from Users.serializer import CustomUserSerializer

class RateStoreCreateSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = RateStore
        fields = ['id', 'store', 'user', 'rate', 'create_date']
        read_only_fields = ['id', 'create_date']


class RateStoreSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = RateStore
        fields = ['id', 'store', 'user', 'rate', 'create_date']
        
        
        