# Generated by Django 4.1.7 on 2023-05-23 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_resetpassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resetpassword',
            old_name='customer',
            new_name='user',
        ),
    ]
