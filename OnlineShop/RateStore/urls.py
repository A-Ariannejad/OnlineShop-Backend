from django.urls import path
from .views import RateStoreCreateView, RateStoreViewSet, RateStoreDeleteView, RateStoreUpdateView
urlpatterns = [
    path('list/', RateStoreViewSet.as_view({'get': 'list'}), name='list'),
    path('create/<int:pk>/', RateStoreCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', RateStoreDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', RateStoreUpdateView.as_view(), name='update'),
]