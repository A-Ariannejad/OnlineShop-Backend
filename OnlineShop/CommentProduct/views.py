from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin, LogicUser
from Products.serializer import ProductCreateSerializer
from Products.models import Product
from .models import CommentProduct
from .serializer import CommentProductCreateSerializer, CommentProductSerializer

class CommentProductViewSet(viewsets.ModelViewSet):
    queryset = CommentProduct.objects.all()
    serializer_class = CommentProductSerializer
    permission_classes = [IsAdmin]

class CommentProductCreateView(generics.CreateAPIView):
    permission_classes = [IsUser]
    queryset = CommentProduct.objects.all()
    serializer_class = CommentProductCreateSerializer

    def perform_create(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        product = Product.objects.get(id=id)
        user = LogicUser.get_user(request=self.request)
        serializer.save(product=product, user=user)

class CommentProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = CommentProduct.objects.all()
    serializer_class = CommentProductSerializer

class CommentProductUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = CommentProduct.objects.all()
    serializer_class = CommentProductCreateSerializer