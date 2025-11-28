from django.urls import path
from .views import ProductListView, ProductFormView

urlpatterns = [
    path('', ProductListView.as_view(), name='list_products'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]
