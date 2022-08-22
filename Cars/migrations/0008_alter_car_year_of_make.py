# Generated by Django 3.2.14 on 2022-07-09 07:34

import Cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0007_auto_20220709_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year_of_make',
            field=models.PositiveIntegerField(default=2022, validators=[django.core.validators.MinValueValidator(1984), Cars.models.max_value_current_year, Cars.models.only_digit]),
        ),
    ]
