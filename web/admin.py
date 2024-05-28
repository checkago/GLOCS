from copy import deepcopy

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export.admin import ImportExportModelAdmin

from .models import *




class ImageGalleryInline(GenericTabularInline):
    model = ImageGallery
    readonly_fields = ('image_url',)


def dublicate_product(modeladmin, request, queryset):
    for product in queryset:
        # Создание копии объекта Product
        duplicate_product = deepcopy(product)
        duplicate_product.pk = None
        duplicate_product.save()

        # Копирование связанных данных
        for size in product.size.all():
            duplicate_product.size.add(size)

        # Копирование других связанных полей
        duplicate_product.type = product.type
        duplicate_product.category = product.category
        duplicate_product.brand = product.brand
        duplicate_product.djibits = product.djibits
        duplicate_product.color = product.color
        duplicate_product.sort = product.sort
        duplicate_product.wb_link = product.wb_link
        duplicate_product.featured = product.featured
        duplicate_product.description = product.description

        # Сохранение копии объекта Product
        duplicate_product.save()

dublicate_product.short_description = "Дублировать объект"


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'), required=False)

    class Meta:
        verbose_name = 'Текст'
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    actions = [dublicate_product]
    inlines = [ImageGalleryInline]
    form = ProductAdminForm
    list_display = ('combined_fields', 'featured', 'sort', 'wb_link',)
    list_filter = ['type', 'category', 'brand', 'model', 'djibits']

    def combined_fields(self, obj):
        return f"{obj.type} {obj.category} {obj.brand} {obj.model} {obj.djibits}, цвет {obj.color}"

    combined_fields.short_description = 'Combined Fields'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Model)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Djibits)
class DjibitsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BannerColor)
class BannerColorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name',)
