from django.db import models


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


class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name='Бренд')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Бренд')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
    color = models.ForeignKey('Color', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет')
    size = models.CharField(max_length=150, verbose_name='Размеры')
    image = models.ImageField(upload_to='media/products', verbose_name='Фото')
    wb_link = models.URLField(verbose_name='Ссылка на маркетплейс', null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name='Виден в рекомендуемых')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    tag = models.CharField(max_length=10, verbose_name='Тег цвета')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название баннера')
    image = models.ImageField(upload_to='media/banners', verbose_name='Изображение')
    active = models.BooleanField(default=True, verbose_name='Показывать на главной')
    title = models.CharField(max_length=150, verbose_name='Заголовок', null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    link = models.URLField(verbose_name='Ссылка', null=True)
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
