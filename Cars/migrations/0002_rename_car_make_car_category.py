# Generated by Django 4.0.3 on 2022-06-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_make',
            new_name='category',
        ),
    ]
