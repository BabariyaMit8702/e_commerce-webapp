# Generated by Django 5.2.1 on 2025-05-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecwapp', '0004_product_category_product_image_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
