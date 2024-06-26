# Generated by Django 2.2.19 on 2024-06-22 01:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230305_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 22, 1, 41, 7, 689528, tzinfo=utc)),
        ),
    ]
