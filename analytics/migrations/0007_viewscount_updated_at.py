# Generated by Django 2.1.1 on 2018-10-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_viewscount_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewscount',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
