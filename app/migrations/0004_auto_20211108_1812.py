# Generated by Django 3.2.9 on 2021-11-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='rating',
        ),
        migrations.AlterField(
            model_name='likequestion',
            name='is_like',
            field=models.BooleanField(default=True, verbose_name='Лайк или дизлайк'),
        ),
    ]
