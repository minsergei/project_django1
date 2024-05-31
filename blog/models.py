from django.db import models


class Blog(models.Model):
    heading_blog = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    slug = models.CharField(
        null=True,
        blank=True,
        verbose_name="Человекопонятный URL",
        help_text="Человекопонятный URL",
    )
    content_blog = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="media/blog/",
        null=True,
        blank=True,
        verbose_name="Изображение",
        help_text="Укажите изображение",
    )
    created_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    published = models.BooleanField(
        default=True,
        verbose_name="Признак публикации",
        help_text="Укажите признак публикации",
    )
    count_views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        return self.heading_blog

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
