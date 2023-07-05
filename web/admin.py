from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html

from .models import *


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    fields = ('thumbnail', 'image')
    readonly_fields = ('thumbnail',)
    exclude = ('content_type', 'object_id')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="auto" height="150" />', obj.image.url)
        return ''
    thumbnail.short_description = 'Фото'


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline]
    form = ProductAdminForm
    list_display = ('combined_fields',)

    def combined_fields(self, obj):
        return f"{obj.type} {obj.category} {obj.brand}, цвет {obj.color}"

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


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
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
