# Generated by Django 2.1.1 on 2018-10-30 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addBanner', '0007_auto_20181030_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbanner',
            name='product',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
