from django.core.management import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def load_categories():
        with open("category.json", "r") as file:
            data = file.read()
            category = json.loads(data)
            return category

    @staticmethod
    def load_products():
        with open("product.json", "r") as file:
            data = file.read()
            products = json.loads(data)
            return products

    def handle(self, *args, **options):
        Category.truncate_table_restart_id()
        Product.objects.all().delete()

        category_create = []
        products_create = []

        category = Command.load_categories()
        for item in category:
            category_create.append(
                Category(
                    name_category=item["fields"]["name_category"],
                    description=item["fields"]["description"],
                )
            )
        Category.objects.bulk_create(category_create)

        product = Command.load_products()
        for item in product:
            products_create.append(
                Product(
                    name_product=item["fields"]["name_product"],
                    description=item["fields"]["description"],
                    preview=item["fields"]["preview"],
                    category=Category.objects.get(pk=item["fields"]["category"]),
                    price=item["fields"]["price"],
                    created_at=item["fields"]["created_at"],
                    updated_at=item["fields"]["updated_at"],
                )
            )
        Product.objects.bulk_create(products_create)
