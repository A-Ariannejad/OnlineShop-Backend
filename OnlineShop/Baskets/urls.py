from django.urls import path
from .views import *
urlpatterns = [
    path('list/', BasketView.as_view({'get': 'list'}), name='list'),
    path('delete/', BasketRemoveProductView.as_view(), name='delete'),
    path('update/', BasketAddProductView.as_view(), name='update'),
]