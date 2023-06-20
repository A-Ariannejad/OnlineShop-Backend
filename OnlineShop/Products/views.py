from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin
from Stores.models import Store
from .models import Product
from .serializer import ProductCreateSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsUser]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        store = Store.objects.get(id=id)
        serializer.save(store=store)

class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer