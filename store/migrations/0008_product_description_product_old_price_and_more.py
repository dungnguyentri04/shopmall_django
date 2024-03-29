# Generated by Django 4.2.6 on 2024-03-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_old_price_remove_product_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='this is a product', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='2.99', max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=7),
        ),
    ]
