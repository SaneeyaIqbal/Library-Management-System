# Generated by Django 2.2.6 on 2019-10-17 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0031_auto_20191017_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 8, 29, 13, 468268)),
        ),
    ]
