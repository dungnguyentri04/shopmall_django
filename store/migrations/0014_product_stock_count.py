# Generated by Django 4.2.6 on 2024-03-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_count',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
