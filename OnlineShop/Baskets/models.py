from django.db import models
from Products.models import Product
from Users.models import CustomUser



class Basket(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True, through='BasketMTMProduct')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_address = models.TextField(max_length=100, default="Post Office")

class BasketMTMProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_products')
    quantity = models.IntegerField(default=1)





