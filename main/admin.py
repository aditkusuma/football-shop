from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_featured")
    list_filter = ("category", "is_featured")
    search_fields = ("name", "category", "description")
