from django.contrib import admin
from .models import Bid
# Register your models here.
class BidAdmin(admin.ModelAdmin):
    list_display =('user','car','price','description','status','cancel_reject_time','accept_time','created_date')
admin.site.register(Bid,BidAdmin)