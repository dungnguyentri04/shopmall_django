# Generated by Django 4.2.6 on 2024-03-18 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_brand_product_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='related_product/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_images', to='store.product')),
            ],
        ),
    ]
