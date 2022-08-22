# Generated by Django 3.2.14 on 2022-07-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_alter_car_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='is_featured',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='carimages',
            name='image',
            field=models.ImageField(blank=True, default='cars/car_images/car.jpeg', null=True, upload_to='cars/car_images/'),
        ),
    ]
