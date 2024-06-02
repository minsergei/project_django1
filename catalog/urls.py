from django.urls import path
from catalog.views import catalog_contacts, ProductListView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_index"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="catalog_product"),
    path("contacts/", catalog_contacts, name="catalog_contacts"),
]
