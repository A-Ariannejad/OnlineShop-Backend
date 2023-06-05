from django.urls import path
from .views import SignUpView, LoginView, CustomUserViewSet, LogoutView

urlpatterns = [
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]