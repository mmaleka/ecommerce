# Generated by Django 2.1.1 on 2018-09-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(default='No barcode yet', max_length=100),
        ),
    ]
