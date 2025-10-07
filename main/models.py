from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('football_shirt', 'Football Shirt'),
        ('football_shoe', 'Football Shoe'),
        ('football_hat', 'Football Hat'),
        ('football_accessories', 'Football Accessories'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, default="")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='football_shirt')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.category})"
