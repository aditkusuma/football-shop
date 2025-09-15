from django.urls import path
from .views import show_main, add_product, show_detail, show_json, show_xml, show_json_by_id, show_xml_by_id

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create/", add_product, name="add_product"),
    path("detail/<int:id>/", show_detail, name="show_detail"),
    path("json/", show_json, name="show_json"),
    path("xml/", show_xml, name="show_xml"),
    path("json/<int:id>/", show_json_by_id, name="show_json_by_id"),
    path("xml/<int:id>/", show_xml_by_id, name="show_xml_by_id"),
]