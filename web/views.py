from django.shortcuts import render
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
        partners = Partner.objects.all()
        exclusive = Product.objects.filter(color__multycolor=True)
        excluded_names = ['Кайма', 'Высокие', 'Низкие', 'Вкладыш']
        accessories = Product.objects.filter(djibits__isnull=False).exclude(djibits__name__in=excluded_names)
        featured = Product.objects.filter(featured=True).order_by('sort')
        contact_data = Organization.objects.filter(active=True)
        sabo = Product.objects.filter(type__name='Сабо').exclude(color__multycolor=True).exclude(djibits__isnull=False)
        shlyopki = Product.objects.filter(type__name='Шлепки')
        context = {
            'title': title,
            'meta_description': meta_description,
            'brands': brands,
            'partners': partners,
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
    contact_data = Organization.objects.all()

    return render(request, 'contacts.html', {'title': title, 'description': description, 'contact_data': contact_data})


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CatalogView(views.View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        types = Type.objects.all()
        colors = Color.objects.all()
        brands = Brand.objects.all()
        models = Model.objects.all()
        products = Product.objects.all().order_by('?')
        djibitss = Djibits.objects.all()
        brands_selected = request.GET.getlist('brands')
        models_selected = request.GET.getlist('model')
        categories_selected = request.GET.getlist('category')
        types_selected = request.GET.getlist('type')
        colors_selected = request.GET.getlist('color')
        djibits_selected = request.GET.getlist('djibits')
        if brands_selected:
            products = products.filter(brand__name__in=brands_selected)
        if models_selected:
            products = products.filter(model__name__in=models_selected)
        if categories_selected:
            products = products.filter(category__name__in=categories_selected)
        if types_selected:
            products = products.filter(type__name__in=types_selected)
        if colors_selected:
            products = products.filter(color__name__in=colors_selected)
        if djibits_selected:
            products = products.filter(djibits__name__in=djibits_selected)

        paginator = Paginator(products, 28)
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
        image = ImageGallery.objects.filter(id=1, content_type=ContentType.objects.get_for_model(Product))
        context = {
            'categories': categories,
            'types': types,
            'colors': colors,
            'products': page_obj,
            'brands': brands,
            'djibitss': djibitss,
            'paginator': paginator,
            'page_obj': page_obj,
            'image': image,
            'brands_selected': brands_selected,
            'models': models,
            'models_selected': models_selected,
            'categories_selected': categories_selected,
            'types_selected': types_selected,
            'colors_selected': colors_selected,
            'djibits_selected': djibits_selected,
        }
        return render(request, 'catalog.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['sizes'] = self.object.size.all().order_by('name')
        return context


def agreement(request):
    text = Text.objects.filter(id=1)

    return render(request, 'text.html', {'text': text})

