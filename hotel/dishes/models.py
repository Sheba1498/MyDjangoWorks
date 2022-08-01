from django.db import models

# Create your models here.
class Menus(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    rating=models.FloatField()
    def __str__(self):
        return self.name
