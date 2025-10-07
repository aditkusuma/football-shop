from django.urls import path
from main.views import show_main, create_product, show_product, show_json, show_xml, show_json_by_id, show_xml_by_id, register, login_user, logout_user
from main.views import edit_product, delete_product, add_product_entry_ajax, get_products_ajax, update_product_entry_ajax, delete_product_entry_ajax
from main.views import login_user_ajax, register_user_ajax
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create/", create_product, name="create_product"),
    path("detail/<int:id>/", show_product, name="show_product"),
    path("json/", show_json, name="show_json"),
    path("xml/", show_xml, name="show_xml"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path("get-products-ajax/", get_products_ajax, name="get_products_ajax"),
    path("update-product-ajax/<int:id>/", update_product_entry_ajax, name="update_product_entry_ajax"),
    path("delete-product-ajax/<int:id>/", delete_product_entry_ajax, name="delete_product_entry_ajax"),
    path("login-ajax/", login_user_ajax, name="login_user_ajax"),
    path("register-ajax/", register_user_ajax, name="register_user_ajax"),
]