# Generated by Django 2.2.6 on 2019-10-17 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20191017_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 10, 19, 50, 922136)),
        ),
    ]
