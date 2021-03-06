# Generated by Django 2.1.1 on 2018-10-14 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='available',
        ),
        migrations.RemoveField(
            model_name='post',
            name='stock',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
