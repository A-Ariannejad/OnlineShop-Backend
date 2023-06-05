from django.urls import path
from .views import StoreCreateView, StoreViewSet, StoreDeleteView, StoreUpdateView

urlpatterns = [
    path('list/', StoreViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', StoreCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', StoreDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', StoreUpdateView.as_view(), name='update'),
]