# Generated by Django 5.1 on 2024-08-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_second_app', '0001_initial'),
    ]

    operations = [
         migrations.AddField(
            model_name='car',
            name='color',
            field=models.TextField(max_length=20, default=''),
        ),
    ]
