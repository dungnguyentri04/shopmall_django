# Generated by Django 4.2.6 on 2024-03-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_productimage_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Related',
        ),
    ]
