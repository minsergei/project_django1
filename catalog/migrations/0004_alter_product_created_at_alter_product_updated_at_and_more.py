# Generated by Django 5.0.6 on 2024-06-10 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_options_remove_product_id_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                auto_now_add=True,
                help_text="Введите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now_add=True,
                help_text="Введите дату последнего изменения",
                null=True,
                verbose_name="Дата последнего изменения",
            ),
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number_version",
                    models.PositiveIntegerField(
                        help_text="Введите версию продукта", verbose_name="Номер версии"
                    ),
                ),
                (
                    "name_version",
                    models.CharField(
                        help_text="Введите название",
                        max_length=150,
                        verbose_name="Название",
                    ),
                ),
                (
                    "active_version",
                    models.BooleanField(
                        default=False,
                        help_text="Укажите признак версии",
                        verbose_name="Признак активной версии",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        help_text="Выберите продукт",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
                "ordering": ["active_version"],
            },
        ),
    ]
