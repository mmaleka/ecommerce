# Generated by Django 2.1.1 on 2018-10-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20181010_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productUrl',
            field=models.CharField(default='https://www.aliexpress.com/', max_length=220),
        ),
    ]
