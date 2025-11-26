from django.views.generic import FormView
from .forms import ProductForm
from django.urls import reverse_lazy


# Create your views here.
class ProductFormView(FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)