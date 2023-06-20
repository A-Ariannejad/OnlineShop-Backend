from django.db import models
from Users.models import CustomUser

class Store(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='store_images/')
    bio = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    rate_number = models.IntegerField(default=0)


