from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin, LogicUser
from Products.serializer import ProductCreateSerializer
from Products.models import Product
from .models import Basket, BasketMTMProduct
from .serializer import BasketMTMProductSerializer, BasketSerializer, BasketMTMProductShowSerializer

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAdmin]

class DeleteFromBasketView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def perform_destroy(self, instance):
        user = LogicUser.get_user(request=self.request)
        basket = Basket.objects.get(user=user)


class UpdateBasketView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = Basket.objects.all()
    serializer_class = BasketMTMProductSerializer

    def perform_update(self, serializer, *args, **kwargs):
        user = LogicUser.get_user(request=self.request)
        basket = Basket.objects.get(user=user)
        product = self.request.data.get("product")
        basket.products.add(product, through_defaults={'quantity': self.request.data.get('quantity')})
        sum = 0
        for x in basket.products.all():
            sum += x.price 
        basket.total_price = sum
        # basket.products.clear()
        # basket.total_price = 0
        basket.save()


class BasketMTMProductViewSet(viewsets.ModelViewSet):
    queryset = BasketMTMProduct.objects.all()
    serializer_class = BasketMTMProductShowSerializer
    permission_classes = [IsAdmin]
    
