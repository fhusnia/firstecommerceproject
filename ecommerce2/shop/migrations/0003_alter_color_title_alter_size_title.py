# Generated by Django 4.1.7 on 2023-04-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_image_product_featured_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
