from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('football_shirt', 'Football Shirt'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.category})"

class News(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)