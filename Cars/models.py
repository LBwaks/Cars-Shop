import datetime
from unicodedata import category
from Cars.choises import  car_models,fuel_type,body_type,transmission_type,drive_type,steering_type
from pyexpat import model
from autoslug import AutoSlugField
from django.db import models
from  ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.forms import CharField, ValidationError
from django.urls import reverse
from hitcount.models import HitCountMixin
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.settings import MODEL_HITCOUNT
from django.contrib.auth.models import User
import random,string
from django.db.models.signals import pre_save 
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField


class Category(models.Model): 

    name = models.CharField(choices=car_models,max_length=100)
    slug =AutoSlugField(populate_from='name',unique=True)
    description = RichTextField(blank=True,null=True)
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    def get_absolute_url(self):
        return reverse("category",kwargs={'slug':self.slug})
    


def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_stock_id_generator(instance):
    # code to get unique stock id
    new_stock_id =random_string_generator().upper()
    Klass = instance.__class__
    qs_exists =Klass.objects.filter(stock_id =new_stock_id).exists()
    if qs_exists:
        return unique_stock_id_generator(instance)
    return new_stock_id




def current_year():
        return datetime.datetime.now().year
def only_digit(value):
        if value.isdigit() == False:
            raise ValidationError('Only Digits Allowed')

def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)


class Car(models.Model,HitCountMixin):
    Mombasa = 'Mombasa'
    Kwale= 'Kwale'
    Kilifi= 'Kilifi'
    TanaRiver= 'Tana River'
    Lamu= 'Lamu'
    TaitaTaveta= 'Taita-Taveta'
    Garissa ='Garissa'
    Wajir= 'Wajir'
    Mandera= 'Mandera'
    Marsabit= 'Marsabit'
    Isiolo= 'Isiolo'
    MERU= 'MERU'
    TharakaNithi= 'Tharaka-Nithi'
    Embu= 'Embu'
    Kitui ='Kitui'
    Machakos= 'Machakos'
    Makueni= 'Makueni'
    Nyandarua= 'Nyandarua'
    Nyeri= 'Nyeri'
    Kirinyaga='Kirinyaga'
    Muranga="Muranga"
    Kiambu= 'Kiambu'
    Turkana ='Turkana'
    WestPokot='West Pokot'
    Samburu= 'Samburu'
    TransNzoia ='Trans Nzoia'
    UasinGishu= 'Uasin Gishu'
    ElgeyoMarakwet= 'Elgeyo-Marakwet'
    Nandi ='Nandi'
    Baringo= 'Baringo'
    Laikipia ='Laikipia'
    Nakuru= 'Nakuru'
    Narok= 'Narok'
    Kajiado= 'Kajiado'
    Kericho= 'Kericho'
    Bomet= 'Bomet'
    Kakamega ='Kakamega'
    Vihiga= 'Vihiga'
    Bungoma= 'Bungoma'
    Busia= 'Busia'
    Siaya= 'Siaya'
    Kisumu ='Kisumu'
    HomaBay= 'Homa Bay'
    Migori= 'Migori'
    Kisii= 'Kisii'
    Nyamira= 'Nyamira'
    Nairobi= 'Nairobi'

    county= [
        (Mombasa, 'Mombasa'),
        (Kwale, 'Kwale'),
        (Kilifi, 'Kilifi'),
        (TanaRiver, 'Tana River'),
        (Lamu, 'Lamu'),
        (TaitaTaveta, 'Taita-Taveta'),
        (Garissa ,'Garissa'),
        (Wajir, 'Wajir'),
        (Mandera, 'Mandera'),
        (Marsabit, 'Marsabit'),
        (Isiolo, 'Isiolo'),
        (MERU, 'Meru'),
        (TharakaNithi, 'Tharaka-Nithi'),
        (Embu, 'Embu'),
        (Kitui ,'Kitui'),
        (Machakos, 'Machakos'),
        (Makueni, 'Makueni'),
        (Nyandarua, 'Nyandarua'),
        (Nyeri, 'Nyeri'),
        (Kirinyaga,'Kirinyaga'),
        (Muranga,"Murang'a"),
        (Kiambu, 'Kiambu'),
        (Turkana ,'Turkana'),
        (WestPokot,' West Pokot'),
        (Samburu, 'Samburu'),
        (TransNzoia ,'Trans Nzoia'),
        (UasinGishu, 'Uasin Gishu'),
        (ElgeyoMarakwet, 'Elgeyo-Marakwet'),
        (Nandi ,'Nandi'),
        (Baringo, 'Baringo'),
        (Laikipia ,'Laikipia'),
        (Nakuru, 'Nakuru'),
        (Narok, 'Narok'),
        (Kajiado, 'Kajiado'),
        (Kericho, 'Kericho'),
        (Bomet, 'Bomet'),
        (Kakamega ,'Kakamega'),
        (Vihiga, 'Vihiga'),
        (Bungoma, 'Bungoma'),
        (Busia, 'Busia'),
        (Siaya, 'Siaya'),
        (Kisumu ,'Kisumu'),
        (HomaBay, 'Homa Bay'),
        (Migori, 'Migori'),
        (Kisii, 'Kisii'),
        (Nyamira, 'Nyamira'),
        (Nairobi, 'Nairobi'),
    ]
    
   
    

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    stock_id = models.CharField(blank=True,max_length=30)
    category = models.ForeignKey(Category,verbose_name="Category",on_delete=models.CASCADE)
    slug =AutoSlugField(populate_from='car_name',unique=True)
    body_type = models.CharField(choices=body_type, max_length= 50)
    car_name = models.CharField(max_length=250)   
    transmission = models.CharField(choices=transmission_type, max_length= 50)
    drive = models.CharField(choices=drive_type, max_length= 50)
    engine_type = models.CharField(max_length=250)
    engine_size = models.CharField(max_length=250)
    fuel = models.CharField(choices=fuel_type, max_length= 50)
    color= models.CharField(max_length=250)

    steering= models.CharField(choices=steering_type, max_length=50)
    number_of_ownership= models.IntegerField(blank=True,null=True)
    imperfection= RichTextField(blank=True,null=True)
    platenumber= models.CharField(max_length=250)
    vehicle_weight = models.CharField(max_length=250,blank=True,null=True,validators=[only_digit])
    max_load_capacity = models.CharField(max_length=250,blank=True,null=True,validators=[only_digit])
    body_length = models.CharField(max_length=250,blank=True,null=True,validators=[only_digit])
    chasis_number = models.CharField(max_length=250)

    vendor_county = models.CharField(choices=county, max_length= 50)
    vendor_location = models.CharField(max_length=250)
    # vendor_address = models.CharField(max_length=250)
    year_of_make = models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(1984),max_value_current_year])
    mileage = models.CharField(max_length=250,validators=[only_digit])
    price =models.CharField(max_length=250,validators=[only_digit])
    status = models.CharField(max_length=250,blank=True,null=True,default="NOT SOLD")
    published = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False) 
    hit_count_generic =GenericRelation(MODEL_HITCOUNT,object_id_field='object_pk',related_query_name='hit_count_generic_relation')   
    created_date = models.DateTimeField(auto_now_add=True)
    favourites = models.ManyToManyField(User,related_name='favourites',default=None,blank=True)

    # accesories      
    air_bag =  models.BooleanField(max_length = 50,default=False)
    # dual_air_bag =  models.BooleanField(max_length = 50,default=False)    
    grill_guard = models.BooleanField(max_length = 50,default=False)
    power_steerring = models.BooleanField(max_length = 50,default=False)
    sun_roof =  models.BooleanField(max_length = 50,default=False)
    navigation =  models.BooleanField(max_length = 50,default=False)
    rear_spoiler = models.BooleanField(max_length = 50,default=False)
    power_windows =  models.BooleanField(max_length = 50,default=False)
    leather_seats=  models.BooleanField(max_length = 50,default=False)
    roof_rails=  models.BooleanField(max_length = 50,default=False)
    dual_air_bags =  models.BooleanField(max_length = 50,default=False) 
    fog_lights =  models.BooleanField(max_length = 50,default=False)
    back_tire =  models.BooleanField(max_length = 50,default=False)
    alloy_wheels =  models.BooleanField(max_length = 50,default=False)
    air_conditioner =  models.BooleanField(max_length = 50,default=False)
    anti_lock_brake_system =  models.BooleanField(max_length = 50,default=False)

   


    # class Meta:
        # ordering = 'descending',
    def __str__(self):
        return self.car_name
    def get_absolute_url(self):
        return reverse("vehicle_details",kwargs={'slug':self.slug})
    
    # def get_related_vehicle_by_category(self):
    #     return Car.objects.filter(category_id=self.category_id)
    #     # .exclude(pk=self.pk).order_by('-created_date')[:8]
   
# ,tag_id =self.tag_id

def pre_save_stock_id(sender,instance,*args,**kwargs):
        if not instance.stock_id:
            instance.stock_id =unique_stock_id_generator(instance)
pre_save.connect(pre_save_stock_id,sender=Car)

   
    
   

class CarImages(models.Model):
    car = models.ForeignKey(Car, verbose_name='Car_images',on_delete=models.CASCADE)
    image =ResizedImageField(quality=90,upload_to='cars/car_images/')
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("cars")

    @property 
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url 
    

