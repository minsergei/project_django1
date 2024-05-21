from django.db import models, connection


class Category(models.Model):
    name_category = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите категорию"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )

    def __str__(self):
        return f"{self.name_category}"

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name_product = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Введите продукт"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    preview = models.ImageField(
        upload_to="media/",
        null=True,
        blank=True,
        verbose_name="Изображение",
        help_text="Укажите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку"
    )
    created_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    def __str__(self):
        return f"{self.name_product} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["category"]
