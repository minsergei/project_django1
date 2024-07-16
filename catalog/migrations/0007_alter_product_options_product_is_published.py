# Generated by Django 4.2 on 2024-07-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category"],
                "permissions": [
                    ("can_publish_product", "Can publish product"),
                    ("change_description_product,", "Change description product"),
                    ("change_category_product", "Change category product"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Укажите статус публикации",
                null=True,
                verbose_name="Публикация",
            ),
        ),
    ]