from django.urls import path
from .views import SignUpView, LoginView, CustomUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]