from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import jwt 


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user = CustomUser.objects.get(email=email)
        Basket.objects.create(user=user)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('permission_level', 'admin')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    username = models.CharField(max_length=30, unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    PERMISSION_CHOICES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )
    permission_level = models.CharField(max_length=20, choices=PERMISSION_CHOICES, default='user')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.email
    
from Baskets.models import Basket

class LogicUser:
    def get_user(request):
        if 'Token' in request.COOKIES:
            token = request.COOKIES['Token']
            dec = jwt.decode(token , key="56s4fs8df4d8af4198h489r4hdy85k4du8l94k8g581d8f", algorithms="HS256")
            if 'email' in dec:
                email = dec['email']
                user = CustomUser.objects.filter(email=email).first()
                if user:
                    return user