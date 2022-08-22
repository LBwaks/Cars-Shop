from dataclasses import field
from pickle import FALSE
from charset_normalizer import from_path
from django import forms
from django.forms import widgets
from .models import Car,CarImages
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from datetime import datetime 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Row,Column,ButtonHolder

class CarForm(forms.ModelForm):
    images= forms.FileField(required=True,widget=forms.FileInput(attrs={
        'required'
        'class':'form-control images',
        'multiple' : True 
        
    }))
    class Meta:
        model = Car
        fields =['category','car_name','body_type','transmission','steering','number_of_ownership','imperfection','platenumber',
        'vehicle_weight','max_load_capacity','body_length','chasis_number',
        'drive','engine_type','engine_size','fuel','color','vendor_county',
        'vendor_location','year_of_make',
        'mileage','price'


        ,'air_bag','grill_guard','power_steerring','sun_roof','navigation',
        'rear_spoiler','power_windows','leather_seats','roof_rails','dual_air_bags',
        'fog_lights','back_tire','alloy_wheels','air_conditioner','anti_lock_brake_system'
        ]

   
        labels={
            'category':'Vehicle Model',
                'imperfection':'Problems Associated with The Vehicle',
                'vendor_county':'County Where Vehicles Is',
                'vendor_location':'Location Where Vehicles Is',
                'platenumber':'Number Plate',
                'vehicle_weight':'Vehicle Weight (kgs)',
                'max_load_capacity':'Maximum Load Capacity (kgs)',
                'body_length':'Body Length (metres)',
                'mileage':'Mileage (kms)',
                'price':'Price (ksh)',
        # 'car_name','body_type','transmission','steering','number_of_ownership','imperfection',
        # 'vehicle_weight','chasis_number',
        # 'drive','engine_type','engine_size','fuel','color','vendor_county',
        # 'vendor_location','year_of_make',
        # 

        }

        widgets ={

            'category':forms.Select(attrs={'required''class':'form-control category','placeholder':'eg Toyota, BMW'}),
            'car_name':forms.TextInput(attrs={'required''class':'form-control car_name', 'placeholder':'eg Vitz,M5'}),            
            'body_type':forms.Select(attrs={'required''class':'form-control body_type'}),
            'transmission':forms.Select(attrs={'required''class':'form-control transmission'}), 

            'steering':forms.Select(attrs={ 'required''class':'form-control steering'}),   
            'color':forms.TextInput(attrs={ 'required''class':'form-control color','placeholder':'eg White'}),   
            'platenumber':forms.TextInput(attrs={ 'required''class':'form-control platenumber','placeholder':'eg KBB 123X'}),   
            'vehicle_weight':forms.TextInput(attrs={'class':'form-control vehicle_weight','placeholder':'eg 2000' }),   
            'max_load_capacity':forms.TextInput(attrs={'validators':'[only_digit]','class':'form-control max_load_capacity','placeholder':'eg 1000'}),  
            'body_length':forms.TextInput(attrs={'class':'form-control body_length','placeholder':'eg 1.9' }), 
            'chasis_number':forms.TextInput(attrs={'required''class':'form-control chasis_number','placeholder':'eg 1234adc' }),   
            'number_of_ownership':forms.NumberInput(attrs={'class':'form-control number_of_ownership'}),   
            'imperfection':forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control imperfection '})),   
            

            'drive':forms.Select(attrs={ 'required''class':'form-control drive'}),
            'engine_type':forms.TextInput(attrs={ 'required''class':'form-control engine_type','placeholder':'eg 2JZ'}),
            'engine_size':forms.TextInput(attrs={'required''class':'form-control engine_size','placeholder':'eg 2000CC'}),
            'fuel':forms.Select(attrs={ 'required''class':'form-control fuel'}),
            'vendor_county':forms.Select(attrs={ 'required''class':'form-control vendor_county'}),
            'vendor_location':forms.TextInput(attrs={'required''class':'form-control vendor_location','placeholder':'Constituency, Town or Estate' }),
            'vendor_address':forms.TextInput(attrs={'required''class':'form-control vendor_address' }),
            'year_of_make':forms.DateInput(attrs={ 'required''class':'form-control year_of_make'}),
            'mileage':forms.TextInput(attrs={ 'required''class':'form-control mileage','placeholder':'eg 20,000'}),
            'price':forms.TextInput(attrs={ 'required''class':'form-control price','placeholder':'eg 2,000,000'}),

        }
    def __init__(self,*args, **kwargs):
            super(CarForm,self).__init__(*args, **kwargs)
            self.helper =FormHelper(self)
            self.helper.form_method='POST'
            self.helper.layout= Layout(
                Row(
                    Column('category',css_class='form-group col-md-4 md-0'),
                    Column('car_name',css_class='form-group col-md-4 md-0'),
                    Column('body_type',css_class='form-group col-md-4 md-0'),
                    
                ),
                'platenumber',
                Row(
                    Column('transmission',css_class='form-group col-md-4 md-0'),
                    Column('drive',css_class='form-group col-md-4 md-0'),
                    Column('fuel',css_class='form-group col-md-4 md-0'),

                   
                ),
                'steering',
                Row(
                    Column('engine_type',css_class='form-group col-md-6 md-0'),
                    Column('engine_size',css_class='form-group col-md-6 md-0'),
                    
                ),
                'color',
                'year_of_make',
              
                'imperfection',
                 Row(
                    Column('vendor_county',css_class='form-group col-md-6 md-0'),
                    Column('vendor_location',css_class='form-group col-md-6 md-0'),
                   
                ),
                'chasis_number',
                Row(
                    Column('vehicle_weight',css_class='form-group col-md-4 md-0'),
                    Column('max_load_capacity',css_class='form-group col-md-4 md-0'),
                    Column('body_length',css_class='form-group col-md-4 md-0'),
                   
                ),
                'number_of_ownership',
                Row(
                    Column('mileage',css_class='form-group col-md-6 md-0'),
                    Column('price',css_class='form-group col-md-6 md-0'),
                   
                ),
                'images',
                Row( 
                    Column('air_bag','grill_guard','power_steerring','sun_roof','alloy_wheels',
                                    'rear_spoiler','power_windows',
                    css_class='form-group d-flex justify-content-between flex-wrap md-0  px-0 '),
                     css_class=' mt-2 pt-2 ',                       
                   
                ),
                Row( 
                    Column('leather_seats','roof_rails','dual_air_bags',
                    'fog_lights','back_tire','navigation','air_conditioner','anti_lock_brake_system',
                                css_class='form-group d-flex justify-content-evenly flex-wrap md-0  px-0 '),
                                css_class=' mb-2 pb-2 ',),
                Submit('submit','Submit',css_class='btn-dark mx-auto')
            )
            

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
            
            if len(mileage) < 3:
                raise ValidationError('Mileage should contain a minimum of 3 characters ')

            if len(color) < 3:
                raise ValidationError('Vehicle Color should contain a minimum of 3 characters ')
            if len(platenumber) < 6:
                raise ValidationError('Vehicle Plate Number should contain a minimum of 6 characters ')
            if imperfection and len(imperfection) < 10:
                raise ValidationError('Vehicle Imperfections Descriptions  should contain a minimum of 10 characters ')
            if len(chasis_number) < 6:   
                raise ValidationError('Vehicle Chasis Number should contain a minimum of 6 characters ')
            # if len(year_of_make) != 4 : 
            #     raise ValidationError('Year Of Make  should contain 4 digits')
            # if year_of_make.date() > datetime.date.today().year:
            #     raise ValidationError('Vehicle Year Of Make Is Invalid ')





class CarEditForm(forms.ModelForm):
    images= forms.FileField(required=False,widget=forms.FileInput(attrs={
        'required'
        'class':'form-control images',
        'multiple' : True 
        
    }))
  
    class Meta:
        model = Car
        fields =['category','car_name','body_type','transmission','steering','number_of_ownership','imperfection','platenumber',
        'vehicle_weight','max_load_capacity','body_length','chasis_number',
        'drive','engine_type','engine_size','fuel','color','vendor_county',
        'vendor_location','year_of_make',
        'mileage','price'


        ,'air_bag','grill_guard','power_steerring','sun_roof','navigation',
        'rear_spoiler','power_windows','leather_seats','roof_rails','dual_air_bags',
        'fog_lights','back_tire','alloy_wheels','air_conditioner','anti_lock_brake_system'
        ]

   
        labels={
            'category':'Vehicle Model',
                'imperfection':'Problems Associated with The Vehicle',
                'vendor_county':'County Where Vehicles Is',
                'vendor_location':'Location Where Vehicles Is',
                'platenumber':'Number Plate',
                'vehicle_weight':'Vehicle Weight (kgs)',
                'max_load_capacity':'Maximum Load Capacity (kgs)',
                'body_length':'Body Length (metres)',
                'mileage':'Mileage (kms)',
                'price':'Price (ksh)',
        # 'car_name','body_type','transmission','steering','number_of_ownership','imperfection',
        # 'vehicle_weight','chasis_number',
        # 'drive','engine_type','engine_size','fuel','color','vendor_county',
        # 'vendor_location','year_of_make',
        # 

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
    def __init__(self,*args, **kwargs):
            super(CarEditForm,self).__init__(*args, **kwargs)
            self.helper =FormHelper(self)
            self.helper.form_method='POST'
            self.helper.layout= Layout(
                Row(
                    Column('category',css_class='form-group col-md-4 md-0'),
                    Column('car_name',css_class='form-group col-md-4 md-0'),
                    Column('body_type',css_class='form-group col-md-4 md-0'),
                    
                ),
                'platenumber',
                Row(
                    Column('transmission',css_class='form-group col-md-4 md-0'),
                    Column('drive',css_class='form-group col-md-4 md-0'),
                    Column('fuel',css_class='form-group col-md-4 md-0'),

                   
                ),
                'steering',
                Row(
                    Column('engine_type',css_class='form-group col-md-6 md-0'),
                    Column('engine_size',css_class='form-group col-md-6 md-0'),
                    
                ),
                'color',
                'year_of_make',
              
                'imperfection',
                 Row(
                    Column('vendor_county',css_class='form-group col-md-6 md-0'),
                    Column('vendor_location',css_class='form-group col-md-6 md-0'),
                   
                ),
                'chasis_number',
                Row(
                    Column('vehicle_weight',css_class='form-group col-md-4 md-0'),
                    Column('max_load_capacity',css_class='form-group col-md-4 md-0'),
                    Column('body_length',css_class='form-group col-md-4 md-0'),
                   
                ),
                'number_of_ownership',
                Row(
                    Column('mileage',css_class='form-group col-md-6 md-0'),
                    Column('price',css_class='form-group col-md-6 md-0'),
                   
                ),
                'images',
                Row( 
                    Column('air_bag','grill_guard','power_steerring','sun_roof','alloy_wheels',
                                    'rear_spoiler','power_windows',
                    css_class='form-group d-flex justify-content-between flex-wrap md-0  px-0 '),
                     css_class=' mt-2 pt-2 ',                       
                   
                ),
                Row( 
                    Column('leather_seats','roof_rails','dual_air_bags',
                    'fog_lights','back_tire','navigation','air_conditioner','anti_lock_brake_system',
                                css_class='form-group d-flex justify-content-evenly flex-wrap md-0  px-0 '),
                                css_class=' mb-2 pb-2 ',),
                Submit('submit','Submit',css_class='btn-dark mx-auto')
            )
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
            
            if len(mileage) < 3:
                raise ValidationError('Title should contain a minimum of 3 characters ')

            if len(color) < 3:
                raise ValidationError('Vehicle Color should contain a minimum of 3 characters ')
            if len(platenumber) < 6:
                raise ValidationError('Vehicle Plate Number should contain a minimum of 6 characters ')
            if imperfection and len(imperfection) < 10:
                raise ValidationError('Vehicle Imperfections Descriptions  should contain a minimum of 10 characters ')
            if len(chasis_number) < 6:   
                raise ValidationError('Vehicle Chasis Number should contain a minimum of 6 characters ')
            # if len(year_of_make) != 4 : 
            #     raise ValidationError('Year Of Make  should contain 4 digits')
            # if year_of_make.date() > datetime.date.today().year:
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