from django.urls import path
from .views import StoreCreateView, StoreViewSet, StoreDeleteView, StoreUpdateView, StoreShowView,StoreSearchView

urlpatterns = [
    path('list/', StoreViewSet.as_view({'get': 'list'}), name='list'),
    path('show/<int:id>/', StoreShowView.as_view(), name='show'),
    path('create/', StoreCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', StoreDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', StoreUpdateView.as_view(), name='update'),
    path('search/', StoreSearchView.as_view(), name='search'),
]