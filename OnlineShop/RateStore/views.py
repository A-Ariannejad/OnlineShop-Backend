from rest_framework import generics, viewsets
from Users.views import IsUser, IsAdmin, LogicUser
from Stores.serializer import StoreCreateSerializer
from Stores.models import Store
from .models import RateStore
from .serializer import RateStoreCreateSerializer, RateStoreSerializer
from decimal import Decimal

class RateStoreViewSet(viewsets.ModelViewSet):
    queryset = RateStore.objects.all()
    serializer_class = RateStoreSerializer
    permission_classes = [IsAdmin]

class RateStoreCreateView(generics.CreateAPIView):
    permission_classes = [IsUser]
    queryset = RateStore.objects.all()
    serializer_class = RateStoreCreateSerializer

    def perform_create(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        store = Store.objects.get(id=id)
        new_rate = store.rate_number * store.rate
        new_rate += Decimal(self.request.data["rate"])
        new_rate_num = store.rate_number + 1
        new_rate = new_rate / new_rate_num
        Store.objects.filter(id=id).update(rate=new_rate, rate_number=new_rate_num)
        store = Store.objects.get(id=id)
        user = LogicUser.get_user(request=self.request)
        serializer.save(store=store, user=user)

class RateStoreDeleteView(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = RateStore.objects.all()
    serializer_class = RateStoreSerializer

    def perform_destroy(self, instance, *args, **kwargs):
        id = self.kwargs.get('pk')
        rateStore = RateStore.objects.get(id=id)
        store = Store.objects.get(id=rateStore.store.id)
        new_rate = store.rate_number * store.rate
        new_rate -= Decimal(instance.rate)
        new_rate_num = store.rate_number - 1
        if new_rate_num > 0:
            new_rate = new_rate / new_rate_num
        else:
            new_rate = 0.00
        Store.objects.filter(id=rateStore.store.id).update(rate=new_rate, rate_number=new_rate_num)
        store = Store.objects.get(id=rateStore.store.id)
        instance.delete()

class RateStoreUpdateView(generics.UpdateAPIView):
    permission_classes = [IsUser]
    queryset = RateStore.objects.all()
    serializer_class = RateStoreCreateSerializer

    def perform_update(self, serializer, *args, **kwargs):
        id = self.kwargs.get('pk')
        rateStore = RateStore.objects.get(id=id)
        store = Store.objects.get(id=rateStore.store.id)
        new_rate = store.rate_number * store.rate
        new_rate -= Decimal(rateStore.rate)
        new_rate += Decimal(self.request.data["rate"])
        new_rate = new_rate / store.rate_number 
        Store.objects.filter(id=rateStore.store.id).update(rate=new_rate)
        store = Store.objects.get(id=rateStore.store.id)
        serializer.save()