from django.db import models
from Stores.models import Store

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    bio = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    sold_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    rate_number = models.IntegerField(default=0)

    PRODUCT_TYPES = (
        ('other', 'Other'),
        ('cloth', 'Cloth'),
        ('laptop', 'Laptop'),
        ('mobile', 'Mobile'),
        ('electronic', 'Electronic'),
        ('furniture', 'furniture')
    )
    type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='other')