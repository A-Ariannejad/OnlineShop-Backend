from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin, LogicUser
from Products.serializer import ProductCreateSerializer
from Products.models import Product
from .models import RateProduct
from .serializer import RateProductCreateSerializer, RateProductSerializer
from decimal import Decimal

class RateProductViewSet(viewsets.ModelViewSet):
    queryset = RateProduct.objects.all()
    serializer_class = RateProductSerializer
    permission_classes = [IsAdmin]

class RateProductCreateView(generics.CreateAPIView):
    permission_classes = [IsUser]
    queryset = RateProduct.objects.all()
    serializer_class = RateProductCreateSerializer

    def perform_create(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        product = Product.objects.get(id=id)
        new_rate = product.rate_number * product.rate
        new_rate += Decimal(self.request.data["rate"])
        new_rate_num = product.rate_number + 1
        new_rate = new_rate / new_rate_num
        Product.objects.filter(id=id).update(rate=new_rate, rate_number=new_rate_num)
        product = Product.objects.get(id=id)
        user = LogicUser.get_user(request=self.request)
        serializer.save(product=product, user=user)

class RateProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = RateProduct.objects.all()
    serializer_class = RateProductSerializer

    def perform_destroy(self, instance, *args, **kwargs):
        id = self.kwargs.get('pk')
        rateProduct = RateProduct.objects.get(id=id)
        product = Product.objects.get(id=rateProduct.product.id)
        new_rate = product.rate_number * product.rate
        new_rate -= Decimal(instance.rate)
        new_rate_num = product.rate_number - 1
        if new_rate_num > 0:
            new_rate = new_rate / new_rate_num
        else:
            new_rate = 0.00
        Product.objects.filter(id=rateProduct.product.id).update(rate=new_rate, rate_number=new_rate_num)
        product = Product.objects.get(id=rateProduct.product.id)
        instance.delete()

class RateProductUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = RateProduct.objects.all()
    serializer_class = RateProductCreateSerializer

    def perform_update(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        rateProduct = RateProduct.objects.get(id=id)
        product = Product.objects.get(id=rateProduct.product.id)
        new_rate = product.rate_number * product.rate
        new_rate -= Decimal(rateProduct.rate)
        new_rate += Decimal(self.request.data["rate"])
        new_rate = new_rate / product.rate_number 
        Product.objects.filter(id=rateProduct.product.id).update(rate=new_rate)
        product = Product.objects.get(id=rateProduct.product.id)
        serializer.save()