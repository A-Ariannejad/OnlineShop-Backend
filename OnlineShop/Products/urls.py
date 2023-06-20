from django.urls import path
from .views import ProductCreateView, ProductViewSet, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='list'),
    path('create/<int:pk>/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
]