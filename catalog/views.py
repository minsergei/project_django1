from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = "index.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"


def catalog_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Сообщение от {name}, телефон: {phone} - {message}")
    return render(request, "contacts.html")
