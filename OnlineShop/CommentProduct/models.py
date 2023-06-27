from django.db import models
from Products.models import Product
from Users.models import CustomUser

class CommentProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment =  models.TextField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
