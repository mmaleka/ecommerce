# Generated by Django 2.1.1 on 2018-10-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addBanner', '0004_addbanner_description1'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbanner',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addbanner',
            name='description3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
