# main/views.py
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

# Required page: shows app name, your name, your class (and the catalog)
def show_main(request):
    products = Product.objects.order_by("-is_featured", "name")
    ctx = {
        "app_name": getattr(settings, "APP_NAME", "Football Shop"),
        "student_name": getattr(settings, "STUDENT_NAME", "Your Name"),
        "student_class": getattr(settings, "STUDENT_CLASS", "Your Class"),
        "products": products,
    }
    return render(request, "main.html", ctx)

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")
    else:
        form = ProductForm()
    return render(request, "create_product.html", {"form": form})

def show_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "detail.html", {"product": product})

# ---- Data delivery (4 endpoints) ----
def show_xml(request):
    return HttpResponse(
        serializers.serialize("xml", Product.objects.all()),
        content_type="application/xml",
    )

def show_json(request):
    return HttpResponse(
        serializers.serialize("json", Product.objects.all()),
        content_type="application/json",
    )

def show_xml_by_id(request, id):
    return HttpResponse(
        serializers.serialize("xml", Product.objects.filter(pk=id)),
        content_type="application/xml",
    )

def show_json_by_id(request, id):
    return HttpResponse(
        serializers.serialize("json", Product.objects.filter(pk=id)),
        content_type="application/json",
    )
