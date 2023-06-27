from rest_framework import generics, viewsets, filters
from Users.views import IsUser, IsAdmin
from Users.models import LogicUser
from .models import Store
from .serializer import StoreCreateSerializer, StoreSerializer


class StoreShowView(generics.RetrieveAPIView):
    permission_classes = [IsUser]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'id'

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsUser]

class StoreCreateView(generics.CreateAPIView):
    permission_classes = [IsUser]
    queryset = Store.objects.all()
    serializer_class = StoreCreateSerializer

    def perform_create(self, serializer):
        user = LogicUser.get_user(request=self.request)
        serializer.save(owner=user)

class StoreDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = Store.objects.all()
    serializer_class = StoreCreateSerializer

class StoreSearchView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'bio']