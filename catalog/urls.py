from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog_index, catalog_contacts, catalog_product

app_name = "catalog"

urlpatterns = [
    path("", catalog_index, name="catalog_index"),
    path("contacts/", catalog_contacts, name="catalog_contacts"),
    path("products/<int:pk>/", catalog_product, name="catalog_product"),
]
