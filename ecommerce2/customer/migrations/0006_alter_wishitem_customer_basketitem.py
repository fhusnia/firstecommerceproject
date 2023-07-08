# Generated by Django 4.1.7 on 2023-05-17 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_color_title_alter_size_title'),
        ('customer', '0005_wishitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishitem',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='customer.customer'),
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.color')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
    ]
