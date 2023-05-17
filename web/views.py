from django.shortcuts import render
from django import views
from web.models import *


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        brands = Brand.objects.all()
        categories = Category.objects.all()
        sliders = Banner.objects.all()
        products = Product.objects.all()
        featured = Product.objects.filter(featured=True)
        context = {
            'brands': brands,
            'categories': categories,
            'products': products,
            'sliders': sliders,
            'featured': featured
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


class CategoryView(views.View):
    model = Category
    categories = Category.objects.all()

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()
        brands = Brand.objects.all()
        context = {
            'categories': categories,
            'products': products,
            'brands': brands,
        }
        return render(request, 'category_detail.html', context)
