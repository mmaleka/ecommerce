# Generated by Django 2.1.1 on 2018-10-10 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_category_slogan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('updated_at',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
