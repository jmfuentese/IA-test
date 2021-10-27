from django.db import models


class Product(models.Model):
    sku = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.description
