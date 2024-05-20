from django.urls import path
from catalog.views import catalog_index, catalog_contacts

app_name = "catalog"

urlpatterns = [
    path("", catalog_index, name="catalog_index"),
    path("contacts/", catalog_contacts, name="catalog_contacts"),
]
