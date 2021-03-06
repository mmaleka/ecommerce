# Generated by Django 2.1.1 on 2018-10-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_auto_20181008_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemsCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=150)),
                ('ip_address', models.CharField(blank=True, max_length=220, null=True)),
                ('address', models.CharField(blank=True, max_length=220, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('cartItems', models.CharField(db_index=True, max_length=150)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-time_stamp'],
            },
        ),
    ]
