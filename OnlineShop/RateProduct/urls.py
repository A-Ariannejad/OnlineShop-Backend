from django.urls import path
from .views import RateProductCreateView, RateProductViewSet, RateProductDeleteView, RateProductUpdateView
urlpatterns = [
    path('list/', RateProductViewSet.as_view({'get': 'list'}), name='list'),
    path('create/<int:pk>/', RateProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', RateProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', RateProductUpdateView.as_view(), name='update'),
]