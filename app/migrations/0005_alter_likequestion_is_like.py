# Generated by Django 3.2.9 on 2021-11-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211108_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likequestion',
            name='is_like',
            field=models.BooleanField(default=True, verbose_name='Лайк'),
        ),
    ]
