from django.urls import path
from .views import CommentProductCreateView, CommentProductViewSet, CommentProductDeleteView, CommentProductUpdateView
urlpatterns = [
    path('list/', CommentProductViewSet.as_view({'get': 'list'}), name='list'),
    path('create/<int:pk>/', CommentProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', CommentProductDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', CommentProductUpdateView.as_view(), name='update'),
]