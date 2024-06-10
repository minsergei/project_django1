from django.urls import path
from catalog.views import (
    catalog_contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_index"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="catalog_product"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", catalog_contacts, name="catalog_contacts"),
]
