from django.test import TestCase
from pytz import timezone
from datetime import datetime
from Bids.models import Bid
from Cars.models import Category
from .models import User,Car

# Create your tests here.
class BidModels(TestCase):
    @classmethod
    def setUpTestData(self):
        user =User.objects.create(
            username= 'johb',
            email= 'admin@admin.com',
            password =12345
        
        )
        category = Category.objects.create(
            name = 'Toyota' ,         
            description = 'RichTextField',
            created_date = datetime.now(),
        )
        car = Car.objects.create(
            user = user,
            stock_id = 'A45H2W',
            category = category,            
            body_type ='Sedan',
            car_name = 'Vitz', 
            transmission = 'Manul',
            drive = 'rhd',
            engine_type = 'boxer',
            engine_size = '2700cc',
            fuel = 'petrol',
            color= 'white',

            steering= 'rhd',
            number_of_ownership= '3',
            imperfection= 'RichTextField(blank=True,null=True)',
            platenumber= 'kcr456',
            vehicle_weight = 555,
            max_load_capacity = 777,
            body_length =666,
            chasis_number = '77777',

            vendor_county = 'kisi',
            vendor_location = 'kissi',

            year_of_make = 5,
            mileage = '34445',
            price =45567,
            status = "PENDING",
            published = False,
            is_cancelled = False,
            
            created_date = datetime.now(),
            

        )
       
        bid =Bid.objects.create(
                bid_uuid ='1175ad88-afef-497e-afcb-23dedac219e0',
                user = user,
                car = car,
                price = 20000,
                slug ='20000-1',
                description = 'its old',
                status = 'PENDING',
                cancel_reject_time = datetime.now(),
                accept_time =datetime.now(),
                created_date = datetime.now(),

                # bid.save()

        )
        bid.save()
        self.assertEquals(self.bid.price ,20000) 
    # def test_bid1(self):
    #     self.assertEquals(bid.slug ,'bid-1')    
class URLTests(TestCase):
    def test_car_search_url(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code,200)