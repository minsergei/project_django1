from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_category")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name_product", "price", "id_category")
    list_filter = ("id_category",)
    search_fields = ("name_product", "description")
