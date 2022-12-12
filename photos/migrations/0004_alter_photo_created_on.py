# Generated by Django 4.1.4 on 2022-12-12 05:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]