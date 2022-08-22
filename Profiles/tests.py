from django.test import SimpleTestCase, TestCase
from .forms import ProfileForm
# Create your tests here.
class TextForms(SimpleTestCase):
    def test_form(self):
        form =ProfileForm(data={
            'fname':'lucas',
            'lname':'obwi',
            'email':'admin@admin.com',
            'id_passport':1234567,
            'tell':254714900233,
            'county':'kisi',
            'location_city_town':'kerub',
            'profile_photo':'profile.png'
        })
        self.assertTrue(form.is_valid)
    def test_form_empty(self):
        form = ProfileForm(data={}) 
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),7)
        
