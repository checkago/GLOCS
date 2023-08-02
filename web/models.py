from typing import Type

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from utils import upload_function


class ImageGallery(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to=upload_function)

    class Meta:
        verbose_name = 'Галерея изображений'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Изображение для {self.content_object}"

    def image_url(self):
        return mark_safe(f'<img src="{self.image.url}" width="auto" height="100px" />')


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    inn = models.CharField(max_length=50, verbose_name='ИНН', blank=True, null=True)
    postcode = models.CharField(max_length=150, verbose_name='Почтовый индекс')
    town = models.CharField(max_length=150, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    logo = models.ImageField(upload_to='media/organization/logo', verbose_name='Логотип', blank=True, null=True)
    active = models.BooleanField(default=False, verbose_name='Основная')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/about', verbose_name='Фото')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'Раздел О нас'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')

    class Meta:
        verbose_name = 'Вид обуви'
        verbose_name_plural = 'Виды обуви'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Бренд')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=2, verbose_name='Название')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Djibits(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название')

    class Meta:
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Вид обуви')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Бренд')
    djibits = models.ForeignKey(Djibits, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Опции')
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет')
    size = models.ManyToManyField(Size, blank=True, verbose_name='Размеры')
    sort = models.FloatField(unique=True, blank=True, null=True, verbose_name='Очередь сортировки')
    wb_link = models.URLField(verbose_name='Ссылка на маркетплейс', null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name='Виден в рекомендуемых')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image_gallery = GenericRelation('imagegallery')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.type} {self.category} {self.brand}"

    @property
    def ct_model(self):
        return self._meta.model_name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'category_slug': self.category.slug, 'brand_slug': self.brand.slug})


class Color(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    tag = models.CharField(max_length=50, blank=True, verbose_name='Тег цвета')
    multycolor = models.BooleanField(default=False, verbose_name='Мультиколор')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class BannerColor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    tag = models.CharField(max_length=50, blank=True, verbose_name='Тег цвета')

    class Meta:
        verbose_name = 'Цвет фона слайдера'
        verbose_name_plural = 'Фоновое цвета для слайдера'

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название баннера')
    bg_color = models.ForeignKey(BannerColor, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Цвет фона')
    image_desktop = models.ImageField(upload_to='media/banners', null=True, blank=True,
                                      verbose_name='Изображение для ПК')
    image_mobile = models.ImageField(upload_to='media/banners', null=True, blank=True,
                                     verbose_name='Изображение для МОБ')
    active = models.BooleanField(default=True, verbose_name='Показывать на главной')
    title = models.CharField(max_length=150, verbose_name='Заголовок', blank=True, null=True)
    subtitle = models.CharField(max_length=250, verbose_name='Подзаголовок', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    link = models.URLField(verbose_name='Ссылка', blank=True, null=True)
    button_name = models.CharField(max_length=20, verbose_name='Название кнопки', default='Подробнее')

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='media/partners', verbose_name='Логотип')
    link = models.URLField(verbose_name='Ссылка на сайт партнера', null=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    link = models.URLField(verbose_name='Ссылка')
    icon = models.CharField(max_length=10, verbose_name='Тег иконки')

    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сети'

    def __str__(self):
        return self.name
