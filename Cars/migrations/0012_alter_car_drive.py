# Generated by Django 3.2.14 on 2022-07-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0011_alter_carimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drive',
            field=models.CharField(choices=[('4wd', '4wd'), ('2wd', '2wd'), ('FWD', 'FWD'), ('RWD', 'RWD')], max_length=50),
        ),
    ]