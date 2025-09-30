from django.urls import path
from main.views import show_main, create_product, show_product, show_json, show_xml, show_json_by_id, show_xml_by_id, register, login_user, logout_user
from main.views import edit_product, delete_product
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
    path('product/<int:id>/edit', edit_product, name='edit_product'),
    path('news/<int:id>/delete', delete_product, name='delete_product'),
]