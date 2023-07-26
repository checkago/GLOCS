from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django import views
from django.views.generic import DetailView

from web.models import *


class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        title = 'GLOCS'
        meta_description = 'Описание'
        brands = Brand.objects.all()
        categories = Category.objects.all()
        sliders = Banner.objects.all()
        products = Product.objects.all()
        exclusive = Product.objects.filter(color__multycolor=True)
        accessories = Product.objects.filter(djibits__isnull=False)
        featured = Product.objects.filter(featured=True).order_by('sort')
        contact_data = Organization.objects.filter(active=True)
        sabo = Product.objects.filter(type__name='Сабо').exclude(color__multycolor=True).exclude(djibits__isnull=False)
        shlyopki = Product.objects.filter(type__name='Шлепки')
        context = {
            'title': title,
            'meta_description': meta_description,
            'brands': brands,
            'categories': categories,
            'products': products,
            'sabo': sabo,
            'shlyopki': shlyopki,
            'sliders': sliders,
            'featured': featured,
            'contact_data': contact_data,
            'exclusive': exclusive,
            'accessories': accessories
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


class CatalogView(views.View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        types = Type.objects.all()
        colors = Color.objects.all()
        brands = Brand.objects.all()
        products = Product.objects.all()
        brands_selected = request.GET.getlist('brands')
        categories_selected = request.GET.getlist('category')
        types_selected = request.GET.getlist('type')
        colors_selected = request.GET.getlist('color')
        if brands_selected:
            products = products.filter(brand__name__in=brands_selected)
        if categories_selected:
            products = products.filter(category__name__in=categories_selected)
        if types_selected:
            products = products.filter(type__name__in=types_selected)
        if colors_selected:
            products = products.filter(color__name__in=colors_selected)
        image = ImageGallery.objects.filter(id=1, content_type=ContentType.objects.get_for_model(Product))
        context = {
            'categories': categories,
            'types': types,
            'colors': colors,
            'products': products,
            'brands': brands,
            'image': image
        }
        return render(request, 'catalog.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['sizes'] = self.object.size.all()
        return context

