from django.urls import path
from main.views import show_main, create_product, show_product, register_user_ajax, login_user_ajax
from main.views import edit_product, delete_product, get_products_ajax, update_product_entry_ajax, delete_product_entry_ajax

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create/", create_product, name="create_product"),
    path("detail/<int:id>/", show_product, name="show_product"),
    path("register-ajax/", register_user_ajax, name="register_user_ajax"),
    path("login-ajax/", login_user_ajax, name="login_user_ajax"),
    path("product/<int:id>/edit/", edit_product, name="edit_product"),
    path("product/<int:id>/delete/", delete_product, name="delete_product"),
    path("get-products-ajax/", get_products_ajax, name="get_products_ajax"),
    path("update-product-ajax/<int:id>/", update_product_entry_ajax, name="update_product_entry_ajax"),
    path("delete-product-ajax/<int:id>/", delete_product_entry_ajax, name="delete_product_entry_ajax"),
]