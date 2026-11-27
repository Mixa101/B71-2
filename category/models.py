from django.db import models


# Create your models here.
class Product(models.Model):
    size = models.IntegerField()
    name = models.CharField()
    price = models.FloatField(null=True)
    minimal_requirements = models.JSONField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField()
