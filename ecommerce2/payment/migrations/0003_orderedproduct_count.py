# Generated by Django 4.1.7 on 2023-05-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_order_used_coupon_order_coupon_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproduct',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
