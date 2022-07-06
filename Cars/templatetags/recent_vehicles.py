from django import template
from Cars.models import Car
from django.db.models import Count
register = template.Library()
@register.simple_tag

def recent_vehicles():
    return Car.objects.filter().order_by('-created_date')[:5]