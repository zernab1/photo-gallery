# Generated by Django 4.1.4 on 2022-12-12 04:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Topic',
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='category',
            new_name='topic',
        ),
    ]
