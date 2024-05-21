from django.shortcuts import render


def catalog_index(request):

    return render(request, "index.html")


def catalog_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Сообщение от {name}, телефон: {phone} - {message}")
    return render(request, "contacts.html")
