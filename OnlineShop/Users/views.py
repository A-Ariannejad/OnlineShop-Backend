from rest_framework.permissions import BasePermission
from .models import CustomUser
from .serializer import SignupCustomUserSerializer, LoginCustomUserSerializer, CustomUserSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser, LogicUser
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password, check_password
import jwt
from rest_framework.views import APIView

class IsUser(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.permission_level == 'user' or user.permission_level == 'moderator' or  user.permission_level == 'admin':
                return True
        return False

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.permission_level == 'moderator' or  user.permission_level == 'admin':
                return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.permission_level == 'admin':
                return True
        return False

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    
class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignupCustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(password = make_password(self.request.data.get('password')))

class LoginView(generics.GenericAPIView):
    serializer_class = LoginCustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email') 
        password = request.data.get('password') 
        user = CustomUser.objects.filter(email = email).first()
        
        if user and check_password(password, user.password):
            encoded_jwt = jwt.encode({"email": user.email}, "56s4fs8df4d8af4198h489r4hdy85k4du8l94k8g581d8f", algorithm="HS256")
            response = Response("Login Successful", status=200)
            response.set_cookie('Token', encoded_jwt)
            return response
        else:
            return Response("Login Failed", status=401)

class LogoutView(APIView):
    permission_classes = [IsUser]

    def get(self, request):
        response = Response("Logout Successful", status=204)
        response.delete_cookie('Token')
        return response


