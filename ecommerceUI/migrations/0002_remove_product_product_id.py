# Generated by Django 5.1 on 2024-08-10 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceUI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]
