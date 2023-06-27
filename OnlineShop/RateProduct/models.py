from django.db import models
from Products.models import Product
from Users.models import CustomUser

class RateProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    create_date = models.DateTimeField(auto_now_add=True)
