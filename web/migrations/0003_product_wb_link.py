# Generated by Django 4.2.1 on 2023-05-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_about_organization_product_brand_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wb_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на маркетплейс'),
        ),
    ]
