from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user_type','fname','lname','email',
        'id_passport','tell','county','address',
        'location_city_town','address','profile_photo')

admin.site.register(Profile,ProfileAdmin)
