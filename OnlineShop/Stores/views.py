from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin
from Users.models import LogicUser
from .models import Store
from .serializer import StoreCreateSerializer, StoreSerializer


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