from django import forms
from django.core.exceptions import ValidationError
# from django.forms import forms
from .models import Bid
from ckeditor.widgets import CKEditorWidget

class BidForm(forms.ModelForm):
    class Meta:
        model =Bid 
        fields =('price','description')

        labels ={
            'price':'Your Offer Price (ksh)',
            'description':'Why That Offer'
        }
        widgets ={
            'price':forms.NumberInput(attrs={'class':'form-control' 'required' }),
            'description':forms.CharField(widget=CKEditorWidget(attrs={'class':'form-control description '})),
        }
 
def clean(self):
            cleaned_data=super(BidForm,self).clean()
            price = cleaned_data.get('price')
            description= cleaned_data.get('description')

            if len(description) < 10:
                raise ValidationError('Description Should Have Atleast 10 characters')
            if len(price) <6 :
                raise ValidationError('The Price should be atleast 6 characters')
            return self.cleaned_data

class BidEditForm(forms.ModelForm):
    class Meta:
        model =Bid 
        fields =('price','description')

        labels ={
            'price':'Your Offer Price (ksh)',
            'description':'Why That Offer'
        }
        widgets ={
            'price':forms.NumberInput(attrs={'class':'form-control' 'required'}),
            'description':forms.CharField(widget=CKEditorWidget()),
        }
 
def clean(self):
            cleaned_data=super(BidEditForm,self).clean()
            price = cleaned_data.get('price')
            description= cleaned_data.get('description')

            if len(description) < 10:
                raise ValidationError('Description Should Have Atleast 10 characters')
            if len(price) <6 :
                raise ValidationError('The Price should be atleast 6 characters')
            return self.cleaned_data