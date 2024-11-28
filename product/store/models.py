from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    procuct_desription = models.TextField(max_length=2083)
    price = models.IntegerField()
    
    def __str__(self):
        return self.product_name