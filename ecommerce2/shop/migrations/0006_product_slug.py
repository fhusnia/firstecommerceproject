# Generated by Django 4.1.7 on 2023-05-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
