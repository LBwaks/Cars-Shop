from django.contrib import admin
from .models import Car,CarImages,Category
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display=('stock_id','category','car_name','vendor_county','vendor_location','mileage','price','status','published','is_cancelled','created_date','air_bag','grill_guard','power_steerring','sun_roof','navigation',
        'rear_spoiler','power_windows','leather_seats','roof_rails','dual_air_bags',
        'fog_lights','back_tire','alloy_wheels','air_conditioner','anti_lock_brake_system')
    list_editable=('published','is_cancelled')
    list_filter=('category','body_type','transmission','drive','engine_size','fuel','vendor_county','year_of_make')
    search_fields=('car_name','mileage','price')

    # def save_model(self,request,obj,form,change):
    #     if not obj.user_id:
    #         obj.user =request.user
    #     obj.save()
admin.site.register(Car,CarAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'description','created_date')
   
admin.site.register(Category,CategoryAdmin)


class CarImagesAdmin(admin.ModelAdmin):
    def ImageThumbnail(self,object):
        return format_html('<img src ="{}" width = "60" class="img-thumbail"/>'.format(object.image.url))
    ImageThumbnail.short_description = 'Vehicle Images'
    list_display =('car','ImageThumbnail','created_date')
admin.site.register(CarImages,CarImagesAdmin)
# class CarAdmin(admin.ModelAdmin):
#     list_display('')
#     list_editable('')
#     list_filter('')
#     search_fields('')

#     def save_model(self,request,obj,form,change):
#         if not obj.user_id:
#             obj.user =request.user
#         obj.save()
# admin.site.register(Car,CarAdmin)
# class CarAdmin(admin.ModelAdmin):
#     list_display('')
#     list_editable('')
#     list_filter('')
#     search_fields('')

#     def save_model(self,request,obj,form,change):
#         if not obj.user_id:
#             obj.user =request.user
#         obj.save()
# admin.site.register(Car,CarAdmin)