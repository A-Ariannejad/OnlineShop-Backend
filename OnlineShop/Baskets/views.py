from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin
from Users.models import LogicUser
from .models import Basket, BasketMTMProduct
from Products.models import Product
from Products.serializer import ProductSerializer
from .serializer import BasketSerializer, BasketAddProductSerializer, BasketRemoveProductSerializer, BasketMTMProductSerializer
from rest_framework import generics, permissions
from django.forms.models import model_to_dict


class Calculate:
    def price_calculate(bp):
        temp = 0.00
        for x in list(bp):
            for y in range(x.quantity):
                temp += (float)(x.product.price)
        return temp
    

class BasketShowView(generics.RetrieveAPIView):
    permission_classes = [IsUser]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    def get(self, request):
        user = LogicUser.get_user(request)
        basket = Basket.objects.get(user=user)
        s = BasketSerializer(basket)
        return Response(s.data, status=status.HTTP_200_OK)
    
class BasketView(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsUser]


class BasketAddProductView(APIView):
    serializer_class = BasketAddProductSerializer
    #permission_classes = [IsUser]

    def post(self, request):
        try:
            user = LogicUser.get_user(request)
            basket = Basket.objects.get(user=user)
        except Basket.DoesNotExist:
            return Response({'error': 'Basket does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasketAddProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = self.request.data['product_id']
            quantity = self.request.data['quantity']
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            basket_product, created = BasketMTMProduct.objects.get_or_create(basket=basket, product=product, defaults={'quantity': 0})
            basket_product.quantity = (int)(quantity) + (int)(basket_product.quantity)
            basket_product.save()
            new_price = Calculate.price_calculate(BasketMTMProduct.objects.filter(basket=basket).all())
            basket.total_price = new_price
            basket.save()
            
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BasketRemoveProductView(APIView):
    serializer_class = BasketAddProductSerializer
    permission_classes = [IsUser]
    def post(self, request):
        try:
            user = LogicUser.get_user(request)
            basket = Basket.objects.get(user=user)
        except Basket.DoesNotExist:
            return Response({'error': 'Basket does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasketRemoveProductSerializer(data=request.data)
        if serializer.is_valid():
            product_id = self.request.data['product_id']
            quantity = self.request.data['quantity']
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product does not exist.'}, status=status.HTTP_404_NOT_FOUND)

            try:
                basket_product = BasketMTMProduct.objects.get(basket=basket, product=product)
            except BasketMTMProduct.DoesNotExist:
                return Response({'error': 'Product is not in the basket.'}, status=status.HTTP_404_NOT_FOUND)

            basket_product.quantity = (int)(basket_product.quantity) - (int)(quantity) 
            basket_product.save()
            if basket_product.quantity <= 0:
                basket_product.delete()
            new_price = Calculate.price_calculate(BasketMTMProduct.objects.filter(basket=basket).all())
            basket.total_price = new_price
            basket.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)