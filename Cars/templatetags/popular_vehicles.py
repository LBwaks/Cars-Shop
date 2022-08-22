from django import template
from Cars.models import Car
from django.db.models import Count
register = template.Library()
@register.simple_tag

def popular_vehicles():
    return Car.objects.select_related('user','category').filter(published=True).order_by('-hit_count_generic')[:5]