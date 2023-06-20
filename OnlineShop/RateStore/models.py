from django.db import models
from Stores.models import Store
from Users.models import CustomUser

class RateStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    create_date = models.DateTimeField(auto_now_add=True)
