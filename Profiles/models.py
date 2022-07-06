from ctypes import addressof
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.urls import reverse
from PIL import Image
# Create your models here.

users_type=[
    ('Buyer','Buyer'),
    ('Seller','Seller'),
    ]
user_gender =[
    ('male','Male'),
    ('female','Female'),
    ('Other','Other')
]

def user_profile_path(instance, filename):
     return 'users/profile/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
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

    county_choice= [
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

    profile_uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type =models.CharField(choices=users_type,max_length=30)
    fname =models.CharField(max_length=30)
    lname =models.CharField(max_length=30)
    email =models.EmailField(max_length=255,unique=True)
    id_passport =models.CharField(max_length=250)
    tell = PhoneNumberField()
    county =models.CharField(max_length=30,choices=county_choice)
    location_city_town=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    profile_photo =models.ImageField(upload_to =user_profile_path,blank=True,null=True,default='users/profile/user_0/profile.png')
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_passport

    @property
    def profile_photo_url(self):
        if self.profile_photo and hasattr(self.profile_photo,'url'):
            return self.profile_photo.url
    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_uuid": self.profile_uuid})
    

#     from django_resized import ResizedImageField

# class MyModel(models.Model):
#     ...
#     image1 = ResizedImageField(size=[500, 300], upload_to='whatever')
#     image2 = ResizedImageField(size=[100, 100], crop=['top', 'left'], upload_to='whatever')
#     image3 = ResizedImageField(size=[100, None], crop=['middle', 'center'], upload_to='whatever')
#     image4 = ResizedImageField(scale=0.5, quality=75, upload_to='whatever')
#     image5 = ResizedImageField(size=None, upload_to='whatever', force_format='PNG')