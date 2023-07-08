# Generated by Django 4.1.7 on 2023-05-19 16:52

from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]


operations = [TrigramExtension()]
