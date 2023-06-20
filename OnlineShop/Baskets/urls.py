from django.urls import path
from .views import BasketViewSet, DeleteFromBasketView, UpdateBasketView, BasketMTMProductViewSet
urlpatterns = [
    path('list/', BasketViewSet.as_view({'get': 'list'}), name='list'),
    path('list1/', BasketMTMProductViewSet.as_view({'get': 'list'}), name='list1'),
    path('delete/<int:pk>/', DeleteFromBasketView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateBasketView.as_view(), name='update'),
]