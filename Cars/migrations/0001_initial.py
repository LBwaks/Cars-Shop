# Generated by Django 4.0.3 on 2022-06-23 08:34

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.CharField(blank=True, max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='car_name', unique=True)),
                ('body_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Pick Up', 'Pick Up'), ('Bus', 'Bus'), ('Hatchback', 'Hatchback'), ('Station Wagon', 'Station Wagon'), ('SUV', 'SUV'), ('Van', 'Van'), ('Mini Van', 'Mini Van'), ('Wagon', 'Wagon'), ('Convertible', 'Convertible'), ('Truck', 'Truck'), ('Heavy Equipment', 'Heavy Equipment'), ('Other', 'Other')], max_length=50)),
                ('car_name', models.CharField(max_length=250)),
                ('transmission', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], max_length=50)),
                ('drive', models.CharField(choices=[('4wd', '4wd'), ('2wd', '2wd')], max_length=50)),
                ('engine_type', models.CharField(max_length=250)),
                ('engine_size', models.CharField(max_length=250)),
                ('fuel', models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('electric', 'Electric'), ('gas', 'Gas'), ('Hybrid', 'Hybrid')], max_length=50)),
                ('color', models.CharField(max_length=250)),
                ('steering', models.CharField(choices=[('RHD', 'Right Hand Drive'), ('LHD', 'Left Hand Drive')], max_length=50)),
                ('number_of_ownership', models.IntegerField(blank=True, null=True)),
                ('imperfection', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('platenumber', models.CharField(max_length=250)),
                ('vehicle_weight', models.CharField(blank=True, max_length=250, null=True)),
                ('max_load_capacity', models.CharField(blank=True, max_length=250, null=True)),
                ('body_length', models.CharField(blank=True, max_length=250, null=True)),
                ('chasis_number', models.CharField(max_length=250)),
                ('vendor_county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('MERU', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Muranga', "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', ' West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], max_length=50)),
                ('vendor_location', models.CharField(max_length=250)),
                ('vendor_address', models.CharField(max_length=250)),
                ('year_of_make', models.PositiveIntegerField(max_length=250)),
                ('mileage', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('status', models.CharField(blank=True, default='PENDING', max_length=250, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('air_bag', models.BooleanField(default=False, max_length=50)),
                ('grill_guard', models.BooleanField(default=False, max_length=50)),
                ('power_steerring', models.BooleanField(default=False, max_length=50)),
                ('sun_roof', models.BooleanField(default=False, max_length=50)),
                ('navigation', models.BooleanField(default=False, max_length=50)),
                ('rear_spoiler', models.BooleanField(default=False, max_length=50)),
                ('power_windows', models.BooleanField(default=False, max_length=50)),
                ('leather_seats', models.BooleanField(default=False, max_length=50)),
                ('roof_rails', models.BooleanField(default=False, max_length=50)),
                ('dual_air_bags', models.BooleanField(default=False, max_length=50)),
                ('fog_lights', models.BooleanField(default=False, max_length=50)),
                ('back_tire', models.BooleanField(default=False, max_length=50)),
                ('alloy_wheels', models.BooleanField(default=False, max_length=50)),
                ('air_conditioner', models.BooleanField(default=False, max_length=50)),
                ('anti_lock_brake_system', models.BooleanField(default=False, max_length=50)),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Toyota', 'Toyota'), ('Nissan', 'Nissan'), ('Suzuki', 'Suzuki'), ('Honda', 'Honda'), ('Mazda', 'Mazda'), ('Subaru', 'Subaru'), ('Mitsubishi', 'Mitsubishi'), ('Volkswagen', 'Volkswagen'), ('BMW', 'BMW'), ('Audi', 'Audi'), ('Mercedes', 'Mercedes'), ('Volvo', 'Volvo'), ('Lexus', 'Lexus'), ('Ford', 'Ford'), ('Peugeot', 'Peugeot'), ('Isuzu', 'Isuzu'), ('Fiat', 'Fiat'), ('Mini', 'Mini'), ('Land Rover', 'Land Rover'), ('Renault', 'Renault'), ('Chrysler Jeep', 'Chrysler Jeep'), ('Porsche', 'Porsche'), ('Hino', 'Hino'), ('Jaguar', 'Jaguar'), ('Maserati', 'Maserati'), ('Chrysler', 'Chrysler'), ('Chevrolet', 'Chevrolet'), ('Alfa Romeo', 'Alfa Romeo'), ('Kia', 'Kia'), ('Scania', 'Scania'), ('Hyundai', 'Hyundai'), ('Range Rover', 'Range Rover'), ('Rover', 'Rover'), ('Amg', 'Amg'), ('Bentley', 'Bentley'), ('Dodge', 'Dodge'), ('Man', 'Man'), ('Jeep', 'Jeep'), ('Tesla', 'Tesla')], max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='cars/car_images/car.jpg', null=True, upload_to='cars/car_images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.car', verbose_name='Car_images')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
