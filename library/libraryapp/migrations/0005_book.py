# Generated by Django 2.2.6 on 2019-10-17 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_auto_20191017_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('book_name', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_copy', models.IntegerField(default=1)),
                ('stock', models.IntegerField(default=1)),
                ('availability', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Author')),
            ],
        ),
    ]