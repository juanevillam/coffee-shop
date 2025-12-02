from django.urls import path
from .views import ProductListView, ProductListAPI, ProductFormView

urlpatterns = [
    path("", ProductListView.as_view(), name="list_products"),
    path("api/", ProductListAPI.as_view(), name="list_products_api"),
    path("add/", ProductFormView.as_view(), name="add_product"),
]
