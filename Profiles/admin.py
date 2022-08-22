from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('fname','lname','email',
        'id_passport','tell','county',
        'location_city_town','profile_photo')

admin.site.register(Profile,ProfileAdmin)
