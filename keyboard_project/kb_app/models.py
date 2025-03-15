from django.db import models
from django.urls import reverse


class KeyBoard(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (
            0,
            "Черновик",
        )
        PUBLISHED = (
            1,
            "Опубликовано",
        )

    name = models.CharField(
        max_length=100,
        verbose_name="Название клавиатуры",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Слаг",
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m,%d/",
        verbose_name="Фото",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name="Статус",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="category",
        verbose_name="Категория",
    )
    counter = models.IntegerField(
        default=1,
        verbose_name="Количество единиц на складе",
    )
    specifications = models.OneToOneField(
        "Specification",
        on_delete=models.CASCADE,
        related_name="specifications",
        verbose_name="Характеристики",
    )
    equipments = models.TextField(
        max_length=255,
        verbose_name="Комплектация",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования",
    )

    class Meta:
        verbose_name = "Клавиатура"
        verbose_name_plural = "Клавиатуры"
        indexes = [models.Index(fields=["-created_at"])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("keyboard", kwargs={"keyboard_slug": self.slug})


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Название категории",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Слаг",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


class Specification(models.Model):
    name = models.CharField(
        max_length=50,
        default=None,
        verbose_name="Название клавиатуры",
    )
    key_material = models.CharField(
        max_length=50,
        verbose_name="Материал клавиш",
    )
    size = models.IntegerField(
        verbose_name="Размер клавиатуры",
    )
    number_of_keys = models.IntegerField(
        verbose_name="Количество клавиш",
    )
    os_compatibility = models.CharField(
        max_length=255,
        verbose_name="Совместимость ОС",
    )
    backlight = models.CharField(
        max_length=50,
        verbose_name="Подсветка",
    )
    connection_interface = models.CharField(
        max_length=255,
        verbose_name="Интерфейс подключения",
    )
    weight = models.FloatField(
        verbose_name="Вес",
    )
    country_of_manufacture = models.CharField(
        max_length=255,
        verbose_name="Страна производитель",
    )
    brand = models.CharField(
        max_length=255,
        verbose_name="Бренд",
    )

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return f"{self.brand}, {self.size}% - {self.number_of_keys} клавиш, {self.key_material}, {self.connection_interface}"
