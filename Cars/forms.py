from dataclasses import field
from charset_normalizer import from_path
from django import forms
from django.forms import widgets
from .models import Car,CarImages
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from datetime import datetime 

class CarForm(forms.ModelForm):
    images= forms.FileField(required=False,widget=forms.FileInput(attrs={
        'class':'form-control',
        'multiple' : True
    }))
    class Meta:
        model = Car
        fields =('category','car_name','body_type','transmission','steering','number_of_ownership','imperfection','platenumber',
        'vehicle_weight','max_load_capacity','body_length','chasis_number',
        'drive','engine_type','engine_size','fuel','color','vendor_county',
        'vendor_location','vendor_address','year_of_make',
        'mileage','price'
        # ,'air_bag','grill_guard','power_steerring','sun_roof','navigation',
        # 'rear_spoiler','power_windows','leather_seats','roof_rails','dual_air_bags',
        # 'fog_lights','back_tire','alloy_wheels','air_conditioner','anti_lock_brake_system'
        )

   
        labels={

        }

        widgets ={

            'category':forms.Select(attrs={'class':'form-control category' 'required'}),
            'car_name':forms.TextInput(attrs={'class':'form-control car_name' 'required'}),            
            'body_type':forms.Select(attrs={'class':'form-control body_type' 'required'}),
            'transmission':forms.Select(attrs={'class':'form-control transmission' 'required'}), 

            'steering':forms.Select(attrs={'class':'form-control steering' 'required'}),   
            'color':forms.TextInput(attrs={'class':'form-control color' 'required'}),   
            'platenumber':forms.TextInput(attrs={'class':'form-control platenumber' 'required'}),   
            'vehicle_weight':forms.TextInput(attrs={'class':'form-control vehicle_weight' }),   
            'max_load_capacity':forms.TextInput(attrs={'class':'form-control max_load_capacity'}),  
            'body_length':forms.TextInput(attrs={'class':'form-control body_length' }), 
            'chasis_number':forms.TextInput(attrs={'class':'form-control chasis_number' 'required'}),   
            'number_of_ownership':forms.NumberInput(attrs={'class':'form-control number_of_ownership'}),   
            'imperfection':forms.CharField(widget=CKEditorWidget()),   

            'drive':forms.Select(attrs={'class':'form-control drive' 'required'}),
            'engine_type':forms.TextInput(attrs={'class':'form-control engine_type' 'required'}),
            'engine_size':forms.TextInput(attrs={'class':'form-control engine_size' 'required'}),
            'fuel':forms.Select(attrs={'class':'form-control fuel' 'required'}),
            'vendor_county':forms.Select(attrs={'class':'form-control vendor_county' 'required'}),
            'vendor_location':forms.TextInput(attrs={'class':'form-control vendor_location' 'required'}),
            'vendor_address':forms.TextInput(attrs={'class':'form-control vendor_address' 'required'}),
            'year_of_make':forms.DateInput(attrs={'class':'form-control year_of_make' 'required'}),
            'mileage':forms.TextInput(attrs={'class':'form-control mileage' 'required'}),
            'price':forms.TextInput(attrs={'class':'form-control price' 'required'}),

        }

    def clean(self):
            cleaned_data=super(CarForm,self).clean()            
            car_name=cleaned_data.get('car_name')
            category= cleaned_data.get('category')          
            engine_type=cleaned_data.get('engine_type')
            engine_size= cleaned_data.get('engine_size') 
            color= cleaned_data.get('color')  
            platenumber= cleaned_data.get('platenumber')  
            vehicle_weight= cleaned_data.get('vehicle_weight')  
            max_load_capacity= cleaned_data.get('max_load_capacity')  
            body_length= cleaned_data.get('body_length')  
            chasis_number= cleaned_data.get('chasis_number')  
            number_of_ownership= cleaned_data.get('number_of_ownership')  
            imperfection= cleaned_data.get('imperfection')  
            vendor_location=cleaned_data.get('vendor_location')
            vendor_address=cleaned_data.get('vendor_address')
            year_of_make=cleaned_data.get('year_of_make')
            mileage =cleaned_data.get('mileage')
            price=cleaned_data.get('price')

            if len(car_name) < 3:
                raise ValidationError('Vehicle Name should contain a minimum of 3 characters ')

            # if len(category) < 3:
            #                 raise ValidationError('Vehicle Model should contain a minimum of 3 characters ')
            if len(engine_type) < 3:
                raise ValidationError('Vehicle Engine Type  should contain a minimum of 3 characters ')

            if len(engine_size) < 3:
                raise ValidationError('Vehicle Engine Size should contain a minimum of 3 characters ')
            if len(vendor_location) < 3:
                raise ValidationError('Seller Location should contain a minimum of 3 characters ')
            if len(vendor_address) < 3:
                raise ValidationError('Seller Address should contain a minimum of 3 characters ')
            if len(mileage) < 3:
                raise ValidationError('Title should contain a minimum of 3 characters ')

            if len(color) < 3:
                raise ValidationError('Vehicle Color should contain a minimum of 3 characters ')
            if len(platenumber) < 6:
                raise ValidationError('Vehicle Plate Number should contain a minimum of 6 characters ')
            if len(imperfection) < 10:
                raise ValidationError('Vehicle Imperfections Descriptions  should contain a minimum of 10 characters ')
            if len(chasis_number) < 6:   
                raise ValidationError('Vehicle Chasis Number should contain a minimum of 6 characters ')
            # if year_of_make.date() > datetime.date.today().year:
            #     raise ValidationError('Vehicle Year Of Make Is Invalid ')





class CarEditForm(forms.ModelForm):
  
    class Meta:
        model = Car
        fields =('category','car_name','category','body_type','transmission','steering','number_of_ownership','imperfection','platenumber',
        'vehicle_weight','max_load_capacity','body_length','chasis_number',
        'drive','engine_type','engine_size','fuel','color','vendor_county',
        'vendor_location','vendor_address','year_of_make',
        'mileage','price'
        ,'air_bag','grill_guard','power_steerring','sun_roof','navigation',
        'rear_spoiler','power_windows','leather_seats','roof_rails','dual_air_bags',
        'fog_lights','back_tire','alloy_wheels','air_conditioner','anti_lock_brake_system'
        )

   
        labels={

        }

        widgets ={
            'category':forms.Select(attrs={'class':'form-control category' 'required'}),
            'car_name':forms.TextInput(attrs={'class':'form-control car_name' 'required'}),           
            'body_type':forms.Select(attrs={'class':'form-control body_type' 'required'}),
            'transmission':forms.Select(attrs={'class':'form-control transmission' 'required'}), 

            'steering':forms.Select(attrs={'class':'form-control steering' 'required'}),   
            'color':forms.TextInput(attrs={'class':'form-control color' 'required'}),   
            'platenumber':forms.TextInput(attrs={'class':'form-control platenumber' 'required'}),   
            'vehicle_weight':forms.TextInput(attrs={'class':'form-control vehicle_weight' }),   
            'max_load_capacity':forms.TextInput(attrs={'class':'form-control max_load_capacity'}),  
            'body_length':forms.TextInput(attrs={'class':'form-control body_length' }), 
            'chasis_number':forms.TextInput(attrs={'class':'form-control chasis_number' 'required'}),   
            'number_of_ownership':forms.NumberInput(attrs={'class':'form-control number_of_ownership'}),   
            'imperfection':forms.CharField(widget=CKEditorWidget()),   

            'drive':forms.Select(attrs={'class':'form-control drive' 'required'}),
            'engine_type':forms.TextInput(attrs={'class':'form-control engine_type' 'required'}),
            'engine_size':forms.TextInput(attrs={'class':'form-control engine_size' 'required'}),
            'fuel':forms.Select(attrs={'class':'form-control fuel' 'required'}),
            'vendor_county':forms.Select(attrs={'class':'form-control vendor_county' 'required'}),
            'vendor_location':forms.TextInput(attrs={'class':'form-control vendor_location' 'required'}),
            'vendor_address':forms.TextInput(attrs={'class':'form-control vendor_address' 'required'}),
            'year_of_make':forms.TextInput(attrs={'class':'form-control year_of_make' 'required'}),
            'mileage':forms.TextInput(attrs={'class':'form-control mileage' 'required'}),
            'price':forms.TextInput(attrs={'class':'form-control price' 'required'}),

        }

    def clean(self):
            cleaned_data=super(CarEditForm,self).clean()            
            car_name=cleaned_data.get('car_name')
            category= cleaned_data.get('category')          
            engine_type=cleaned_data.get('engine_type')
            engine_size= cleaned_data.get('engine_size') 
            color= cleaned_data.get('color')  
            platenumber= cleaned_data.get('platenumber')  
            vehicle_weight= cleaned_data.get('vehicle_weight')  
            max_load_capacity= cleaned_data.get('max_load_capacity')  
            body_length= cleaned_data.get('body_length')  
            chasis_number= cleaned_data.get('chasis_number')  
            number_of_ownership= cleaned_data.get('number_of_ownership')  
            imperfection= cleaned_data.get('imperfection')  
            vendor_location=cleaned_data.get('vendor_location')
            vendor_address=cleaned_data.get('vendor_address')
            year_of_make=cleaned_data.get('year_of_make')
            mileage =cleaned_data.get('mileage')
            price=cleaned_data.get('price')

            if len(car_name) < 3:
                raise ValidationError('Vehicle Name should contain a minimum of 3 characters ')

            # if len(category) < 3:
            #                 raise ValidationError('Vehicle Model should contain a minimum of 3 characters ')
            if len(engine_type) < 3:
                raise ValidationError('Vehicle Engine Type  should contain a minimum of 3 characters ')

            if len(engine_size) < 3:
                raise ValidationError('Vehicle Engine Size should contain a minimum of 3 characters ')
            if len(vendor_location) < 3:
                raise ValidationError('Seller Location should contain a minimum of 3 characters ')
            if len(vendor_address) < 3:
                raise ValidationError('Seller Address should contain a minimum of 3 characters ')
            if len(mileage) < 3:
                raise ValidationError('Title should contain a minimum of 3 characters ')

            if len(color) < 3:
                raise ValidationError('Vehicle Color should contain a minimum of 3 characters ')
            if len(platenumber) < 6:
                raise ValidationError('Vehicle Plate Number should contain a minimum of 6 characters ')
            if len(imperfection) < 10:
                raise ValidationError('Vehicle Imperfections Descriptions  should contain a minimum of 10 characters ')
            if len(chasis_number) < 6:   
                raise ValidationError('Vehicle Chasis Number should contain a minimum of 6 characters ')
            # if year_of_make.date() > datetime.date.today():
            #     raise ValidationError('Vehicle Year Of Make Is Invalid ')






class ImageForm(forms.ModelForm):

    class Meta:
        model = CarImages
        fields = ('image',)
        labels = {
            'image': 'OOP'
        }
        widgets={
            'image':forms.ClearableFileInput(attrs={'class':'form-control image ','multiple' :True}),
            
        }