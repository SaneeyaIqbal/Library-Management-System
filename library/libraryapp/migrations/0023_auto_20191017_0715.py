# Generated by Django 2.2.6 on 2019-10-17 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0022_auto_20191017_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='stock',
            new_name='in_stock',
        ),
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 7, 15, 37, 267057)),
        ),
    ]