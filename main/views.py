from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST, require_GET



def show_main(request):
    # existing "all" vs "mine" filter
    filter_type = request.GET.get("filter", "all")  # "all" or "mine"
    # new category filter (?category=football_shirt, etc.)
    category_key = request.GET.get("category")

    # start with all products
    qs = Product.objects.all().select_related("user")

    # apply "mine" filter if requested
    if filter_type != "all":
        if request.user.is_authenticated:
            qs = qs.filter(user=request.user)
        else:
            qs = qs.none()

    # apply category filter if valid key provided
    if category_key:
        valid_keys = {k for k, _ in Product.CATEGORY_CHOICES}
        if category_key in valid_keys:
            qs = qs.filter(category=category_key)

    context = {
        'npm': '2406365231',
        'name': 'Raditya Ikhlas Kusuma',
        'class': 'PBP KKI',
        'product_list': qs,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'filter_type': filter_type,          # optional: for UI toggles
        'active_category': category_key,     # for highlighting in navbar/menu
        'CATEGORY_CHOICES': Product.CATEGORY_CHOICES,
    }
    return render(request, "main.html", context)
    

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if product.user != request.user:
        messages.error(request, 'You are not authorized to edit this product.')
        return redirect('main:show_main')
        
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        messages.error(request, 'You are not authorized to delete this product.')
        return redirect('main:show_main')
    
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('main:show_main')

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'is_featured': product.is_featured,
            'user_id': product.user_id,     }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'is_featured': product.is_featured,
            'user_id': product.user_id,     
            }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_protect
@require_POST
def add_product_entry_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({"ok": False, "error": "Authentication required"}, status=401)

    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({
            "ok": True,
            "product": {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": str(product.price),
                "category": product.category,
                "thumbnail": product.thumbnail,
                "is_featured": product.is_featured,
                "user_id": product.user.id
            }
        }, status=201)
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)


@require_GET
def get_products_ajax(request):
    """
    Get products with filtering support
    """
    qs = Product.objects.all().select_related("user")
    
    # Filter by user's products if requested
    filter_type = request.GET.get("filter")
    if filter_type == "mine" and request.user.is_authenticated:
        qs = qs.filter(user=request.user)
        
    # Filter by category if provided
    category = request.GET.get("category")
    if category:
        qs = qs.filter(category=category)
        
    # Order by newest first
    qs = qs.order_by("-id")
    
    data = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "category": p.category,
            "thumbnail": p.thumbnail,
            "price": str(p.price),
            "is_featured": p.is_featured,
            "user_id": p.user.id if p.user else None,
        }
        for p in qs
    ]
    return JsonResponse(data, safe=False, status=200)

@csrf_protect
@require_POST
def update_product_entry_ajax(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({"ok": False, "error": "Authentication required"}, status=401)

    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST, request.FILES, instance=product)  # include FILES just in case

    if form.is_valid():
        product = form.save()
        return JsonResponse({
            "ok": True,
            "product": {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": str(product.price),
                "category": product.category,
                "thumbnail": product.thumbnail,
                "is_featured": product.is_featured,
                "user_id": product.user_id,
            }
        }, status=200)

    # TEMP: log errors to console during dev
    # print(form.errors.as_json())
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@csrf_protect
@require_POST
def delete_product_entry_ajax(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({"ok": False, "error": "Authentication required"}, status=401)
        
    try:
        product = Product.objects.get(pk=id, user=request.user)
        product.delete()
        return JsonResponse({"ok": True, "message": "Product deleted successfully"}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"ok": False, "error": "Product not found or unauthorized"}, status=404)
    
@csrf_protect
@require_POST
def login_user_ajax(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({
            "ok": True,
            "user": {
                "id": user.id,
                "username": user.username
            }
        })
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    return JsonResponse({
        "ok": False,
        "errors": form.errors
    }, status=400)

@csrf_protect
@require_POST
def register_user_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return JsonResponse({
            "ok": True,
            "user": {
                "id": user.id,
                "username": user.username
            }
        })
    return JsonResponse({
        "ok": False,
        "errors": form.errors
    }, status=400)
