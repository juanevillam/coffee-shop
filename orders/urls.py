from django.urls import path
from .views import MyOrderView

urlpatterns = [
    path("my-order", MyOrderView.as_view(), name="my_order"),
]
