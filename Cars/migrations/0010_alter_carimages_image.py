# Generated by Django 3.2.14 on 2022-07-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0009_alter_car_year_of_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carimages',
            name='image',
            field=models.ImageField(default='car.jpeg', upload_to='cars/car_images/'),
        ),
    ]