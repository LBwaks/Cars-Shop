from rest_framework import serializers
from .models import Car,CarAccesories,CarImages

class CarSerializer(serializers.ModelSerializer):
    class Meta :
        Model = Car 
        fields = '__all__'

class  CarAccesoriesSerializer(serializers.ModelSerializer):
    class Meta :
        Model =  CarAccesories
        fields = '__all__'

class  CarImagesSerializer(serializers.ModelSerializer):
    class Meta :
        Model =  CarImages
        fields = '__all__'