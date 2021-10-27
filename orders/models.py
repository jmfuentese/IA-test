from django.db import models
from products.models import Product


class Order(models.Model):
    status = models.CharField(max_length=20, null=False, default="Pending")
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return f"Order id: {self.id} status: {self.status}"
