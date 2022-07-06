from cgitb import lookup
from dataclasses import field
import django_filters
from .models import Car 

class CarFilter(django_filters.FilterSet):
    car_make = django_filters.CharFilter(lookup_expr ='iexact')
    car_name = django_filters.CharFilter(lookup_expr ='iexact')

    class Mata:
        model = Car
        field = ['body_type','price','year_of_make']