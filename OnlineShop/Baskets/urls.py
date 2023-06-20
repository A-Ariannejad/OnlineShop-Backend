from django.urls import path
from .views import BasketViewSet, DeleteFromBasketView, UpdateBasketView
urlpatterns = [
    path('list/', BasketViewSet.as_view({'get': 'list'}), name='list'),
    path('delete/<int:pk>/', DeleteFromBasketView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateBasketView.as_view(), name='update'),
]