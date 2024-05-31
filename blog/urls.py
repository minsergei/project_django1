from django.urls import path

from blog.views import BlogListView, BlogDetailView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("/", BlogListView.as_view(), name="catalog_index"),
    path("products/<int:pk>/", BlogDetailView.as_view(), name="catalog_product"),
]
