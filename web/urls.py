from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views
from .views import IndexView, about, contact, CategoryView, BrandGlocsView, BrandSunriseView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', about, name='about'),
    path('contacts', contact, name='contact'),
    path('catalog/', CategoryView.as_view(), name='categories'),
    path('brand-glocs/', BrandGlocsView.as_view(), name='brand-glocs'),
    path('brand-sunrise/', BrandSunriseView.as_view(), name='brand-sunrise'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

