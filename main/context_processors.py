from .models import Product

def categories(request):
    # [('football_shirt','Football Shirt'), ...]
    return {"CATEGORIES": Product.CATEGORY_CHOICES}
