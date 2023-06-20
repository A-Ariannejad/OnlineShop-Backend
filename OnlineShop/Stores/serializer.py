from rest_framework import serializers
from .models import Store
from Users.serializer import CustomUserSerializer

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'image', 'bio', 'create_date', 'address']
        read_only_fields = ['id', 'create_date']


class StoreSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = Store
        fields = ['id', 'owner', 'name', 'image', 'bio', 'create_date', 'address', 'rate', 'rate_number']
        