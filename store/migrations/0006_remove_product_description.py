# Generated by Django 4.2.6 on 2024-03-17 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
