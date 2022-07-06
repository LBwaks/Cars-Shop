from django import template
from Cars.models import Category
from django.db.models import Count
register = template.Library()
@register.simple_tag

def vehicle_categories():
    return Category.objects.all().annotate(tags_count=Count('car'))