# Generated by Django 4.1.7 on 2023-03-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
