from audioop import reverse
# from multiprocessing.connection import Client
from urllib import response
from django.test import SimpleTestCase, TestCase,Client
from Cars.views import CarsView,AddVehicleView
from django.urls import reverse, resolve

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_car_url_is_resolved(self):
        url =reverse('cars')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CarsView)



        

class TestViews(TestCase):
    def test_carviews(self):
        client = Client()
        response = client.get(reverse('cars'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cars/cars.html')











        
