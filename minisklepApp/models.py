from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2)
    img = models.ImageField(upload_to="products/", null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")