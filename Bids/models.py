from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.urls import reverse
from Cars.models import Car
from autoslug import AutoSlugField
# Create your models here.
class Bid(models.Model):
    bid_uuid =models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User ,related_name='user_bid',on_delete=models.CASCADE)
    car = models.ForeignKey(Car,related_name='car',on_delete=models.CASCADE)
    price = models.IntegerField()
    slug =AutoSlugField(populate_from='price',unique=True)
    description = RichTextField(blank=True,null=True)
    status = models.CharField(max_length=40,default='PENDING')
    cancel_reject_time =models.DateTimeField(blank=True,null=True)
    accept_time =models.DateTimeField(blank=True,null=True)
    created_date =models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("my_bids")
    