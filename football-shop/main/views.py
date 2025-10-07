from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.all().select_related("user")
    return render(request, "main.html", {'product_list': products})

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return JsonResponse({'ok': True, 'id': product_entry.id, 'name': product_entry.name})
    return JsonResponse({'ok': False, 'errors': form.errors})

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "detail.html", {'product': product})

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return JsonResponse({'ok': True})
    return JsonResponse({'ok': False, 'errors': form.errors})

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return JsonResponse({'ok': True})

def register_user_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'ok': True})
        return JsonResponse({'ok': False, 'errors': form.errors})
    return JsonResponse({'ok': False})

def login_user_ajax(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({'ok': True})
        return JsonResponse({'ok': False, 'errors': form.errors})
    return JsonResponse({'ok': False})