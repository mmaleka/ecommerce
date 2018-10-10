# Generated by Django 2.1.1 on 2018-10-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.CharField(choices=[('FD', 'Free delivery (Free) - 20 to 37 days'), ('PL', 'Priority delivery (R 120.00) - 9 to 20 days')], default='Free delivery - 20 to 37 days', max_length=2),
        ),
    ]
