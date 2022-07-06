from email import message
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=50)
    email =models.EmailField(max_length=100)
    subject =models.CharField(max_length=255)
    message = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    def get_absolute_url(self):
        return reverse("contact")
    