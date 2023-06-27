from django.urls import path
from .views import ProductCreateView, ProductViewSet, ProductDeleteView, ProductUpdateView, ProductShowView, ProductSearchView, ProductCategoriesView, ShowProductByStoreViewSet

urlpatterns = [
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='list'),
    path('show/<int:id>/', ProductShowView.as_view(), name='show'),
    path('create/<int:pk>/', ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('bystore/<int:pk>/', ShowProductByStoreViewSet.as_view(), name='bystore'),
    path('search/', ProductSearchView.as_view(), name='search'),
    path('categories/', ProductCategoriesView.as_view(), name='categories-search'),
]