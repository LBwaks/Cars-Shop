import email
from django import forms
from django.forms import widgets
from .models import Profile
from phonenumber_field.modelfields import PhoneNumberField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('fname','lname','email',
        'id_passport','tell','county',
        'location_city_town','profile_photo')
        labels ={
            # 'user_type':'Type Of The User :' ,
            'fname': 'Firstname',
            'lname':'LastName' ,
            'email':'Email' ,
            'id_passport':'ID/Passport:' ,
            'tell': 'Phonenumber:',
            'county': 'County:',            
            'location_city_town':'Location /Town/ City' ,
            
            'profile_photo':'Profile Photo',
        }
        widgets = {
            # 'user_type':forms.Select(attrs={'class':'form-select'}),
            'fname': forms.TextInput(attrs={'required''class':'form-control fname','placeholder':'eg John'}),
            'lname':forms.TextInput(attrs={'required''class':'form-control','placeholder':'eg Doe'}),
            'email':forms.EmailInput(attrs={'required''class':'form-control','placeholder':'eg johndoe@gmail.com'}),
            'id_passport':forms.TextInput(attrs={'required''class':'class-control','placeholder':'eg AB123456' }) ,
            # 'tell': PhoneNumberField(),
            'county': forms.Select(attrs={'class':'form-select','placeholder':'eg Nairobi'}),           
            'location_city_town':forms.TextInput(attrs={'required''class':'form-control','placeholder':'eg Starehe'}),
          
            'profile_photo': forms.ClearableFileInput(attrs={'class':'form-control image '}),
        }

def clean(self):
    cleaned_data = super(ProfileForm,self).clean()
    fname =cleaned_data.get('fname')
    lname=cleaned_data.get('lname')
    email=cleaned_data.get('email')
    id_passport =cleaned_data.get('id_passport')
    tell =cleaned_data.get('tell')
    location=cleaned_data.get('location_city_town')
 

    if len(fname)<3:
        raise forms.ValidationError('First Name should have a minimum of 3 characters')
    if len(lname)<3:
            raise forms.ValidationError('Last Name should have a minimum of 3 characters')

    if len(id_passport)< 8 or len(id_passport) > 12 :
            raise forms.ValidationError('Id or Passport should have a minimum of 8 characters')

    if len(tell)<3:
            raise forms.ValidationError('Phone Number should have a minimum of 3 characters')

    if len(location)<3:
            raise forms.ValidationError('Location Town Or City should have a minimum of 3 characters')

    
   
    return self.cleaned_data
    

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('fname','lname','email',
        'id_passport','tell','county',
        'location_city_town','profile_photo')
        labels ={
            # 'user_type':'Type Of The User :' ,
            'fname': 'Firstname',
            'lname':'LastName' ,
            'email':'Email' ,
            'id_passport':'ID/Passport:' ,
            'tell': 'Phonenumber:',
            'county': 'County:',            
            'location_city_town':'Location /Town/ City' ,
          
            'profile_photo':'Profile Photo',
        }
        widgets = {
            # 'user_type':forms.Select(attrs={'class':'form-select'}),
            'fname': forms.TextInput(attrs={'required''class':'form-control fname','placeholder':'eg John'}),
            'lname':forms.TextInput(attrs={'required''class':'form-control','placeholder':'eg Doe'}),
            'email':forms.EmailInput(attrs={'required''class':'form-control','placeholder':'eg johndoe@gmail.com'}),
            'id_passport':forms.TextInput(attrs={'required''class':'class-control','placeholder':'eg AB123456' }) ,
            # 'tell': PhoneNumberField(),
            'county': forms.Select(attrs={'class':'form-select','placeholder':'eg Nairobi'}),           
            'location_city_town':forms.TextInput(attrs={'required''class':'form-control','placeholder':'eg Starehe'}),
            
            'profile_photo': forms.ClearableFileInput(attrs={'class':'form-control image '}),
        }

def clean(self):
    cleaned_data = super(EditProfileForm,self).clean()
    fname =cleaned_data.get('fname')
    lname=cleaned_data.get('lname')
    email=cleaned_data.get('email')
    id_passport =cleaned_data.get('id_passport')
    tell =cleaned_data.get('tell')
    location=cleaned_data.get('location_city_town')


    if len(fname)<3:
        raise forms.ValidationError('First Name should have a minimum of 3 characters')
    if len(lname)<3:
            raise forms.ValidationError('Last Name should have a minimum of 3 characters')

    if len(id_passport)< 8 or len(id_passport) > 12 :
            raise forms.ValidationError('Id or Passport should have a minimum of 8 characters')

    if len(tell)<3:
            raise forms.ValidationError('Phone Number should have a minimum of 3 characters')

    if len(location)<3:
            raise forms.ValidationError('Location Town Or City should have a minimum of 3 characters')

    
   
    return self.cleaned_data