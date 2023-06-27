from rest_framework import generics, viewsets, filters, status
from Users.views import IsUser, IsAdmin
from Stores.models import Store
from .models import Product
from .serializer import ProductCreateSerializer, ProductSerializer
from rest_framework.response import Response


class ProductShowView(generics.RetrieveAPIView):
    permission_classes = [IsUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsUser]

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

class ProductSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'type', 'bio']

class ProductCategoriesView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        L_price_input = self.request.query_params.get('lower_price', 0)
        U_price_input = self.request.query_params.get('upper_price', 99999999999999999)
        type_input = self.request.query_params.get('type', None)
        if type_input:
            queryset = queryset.filter(type__icontains=type_input)
        queryset = queryset.filter(price__range=(L_price_input, U_price_input))
        return queryset


class ShowProductByStoreViewSet(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsUser]

    def get(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        store = Store.objects.get(id=id)
        products = Product.objects.filter(store=store).all()
        serializers = ProductSerializer(products, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)