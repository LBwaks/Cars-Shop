# Generated by Django 4.0.3 on 2022-06-27 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_rename_car_make_car_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.category', verbose_name='Category'),
        ),
    ]
