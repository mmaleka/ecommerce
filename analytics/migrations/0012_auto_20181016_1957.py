# Generated by Django 2.1.1 on 2018-10-16 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0011_blogviewscount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogViewsCount',
            new_name='PostViewsCount',
        ),
    ]