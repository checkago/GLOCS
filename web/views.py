from django.shortcuts import render
from django import views
from web.models import *


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        title = 'GLOCS'
        meta_description = 'Описание'
        brands = Brand.objects.all()
        categories = Category.objects.all()
        sliders = Banner.objects.all()
        products = Product.objects.all()
        featured = Product.objects.filter(featured=True)
        contact_data = Organization.objects.filter(active=True)
        context = {
            'title': title,
            'meta_description': meta_description,
            'brands': brands,
            'categories': categories,
            'products': products,
            'sliders': sliders,
            'featured': featured,
            'contact_data': contact_data
        }
        return render(request, 'index.html', context)


def about(request):
    title = 'О нас'
    description = 'Описание страницы'

    return render(request, 'about.html', {'title': title, 'description': description})


def contact(request):
    title = 'Контакты'
    description = 'Описание страницы'
    contact_data = Organization.objects.filter(name='Санрайз')

    return render(request, 'contacts.html', {'title': title, 'description': description, 'contact_data': contact_data})


class BrandGlocsView(views.View):
    model = Brand

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        brand = Brand.objects.get(name='GLOCS')
        products = Product.objects.filter(brand=brand)
        context = {
            'categories': categories,
            'products': products,
            'brand': brand,
        }
        return render(request, 'brand.html', context)


class BrandSunriseView(views.View):
    model = Brand

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        brand = Brand.objects.get(name='SUNRISE')
        products = Product.objects.filter(brand=brand)
        context = {
            'categories': categories,
            'products': products,
            'brand': brand,
        }
        return render(request, 'brand.html', context)
