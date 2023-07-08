from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0006_product_slug'),
    ]
    operations = [TrigramExtension()]