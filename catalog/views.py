from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def catalog_index(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, "index.html", context)


def catalog_product(request, pk):
    product1 = get_object_or_404(Product, pk=pk)
    context = {'product': product1}
    return render(request, "product.html", context)


def catalog_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Сообщение от {name}, телефон: {phone} - {message}")
    return render(request, "contacts.html")
