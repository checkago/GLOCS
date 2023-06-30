from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', about, name='about'),
    path('contacts', contact, name='contact'),
    path('brand-glocs/', BrandGlocsView.as_view(), name='brand-glocs'),
    path('brand-sunrise/', BrandSunriseView.as_view(), name='brand-sunrise'),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

