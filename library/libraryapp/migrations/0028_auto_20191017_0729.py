# Generated by Django 2.2.6 on 2019-10-17 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0027_auto_20191017_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 7, 29, 32, 724200)),
        ),
    ]
