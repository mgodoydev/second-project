# Generated by Django 5.1 on 2024-08-31 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_second_app', '0002_auto_20240831_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.TextField(max_length=20),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('publication_date', models.DateField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_second_app.publisher')),
            ],
        ),
    ]
