
from itertools import count
from unicodedata import category
from urllib import request
from django import template
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from pytz import timezone
from Cars.forms import CarForm, ImageForm, CarEditForm
from .models import Car, CarImages,Category
from Bids.models import Bid
from hitcount.views import HitCountDetailView
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView,TemplateView,FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sweetify.views import SweetifySuccessMixin
from django.utils import timezone
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.cache import cache
import os
from twilio.rest import Client
from django.core.mail import send_mail

# Create your views here.
class CarsView(ListView):
    model =Car
    template_name='cars/cars.html'
    paginate_by = 6
    queryset = Car.objects.select_related('user','category').filter(published=True).order_by('-created_date')
    def get_context_data(self, **kwargs):
        context = super(CarsView,self).get_context_data(**kwargs)
        categories =Category.objects.all()
        context["categories"] = categories
        return context
    
class CarDetailView(HitCountDetailView):
    model =Car
    template_name ='cars/car_details.html'
    count_hit = True

    def get_context_data(self, *args,**kwargs):
        context=super(CarDetailView,self).get_context_data(**kwargs)
        
       
        # .exclude(slug=self.slug).order_by('-created_date')[:8]
        car_slug=self.kwargs['slug']
        if cache.get(car_slug):
            car=cache.get(car_slug)
            print('hit the cache')
        else:

            # try:
                car = get_object_or_404(Car.objects.select_related('user','category'),slug=self.kwargs['slug'])
                cache.set(car_slug,car)
                print('hit the db')
       
        fav =bool        
        if car.favourites.filter(id=self.request.user.id).exists():
            fav =True
        cars_id = car.id
        existing_bid = Bid.objects.filter(user_id=self.request.user.id,car_id =car.id )
        context ={
          'car':car,'fav':fav,'existing_bid':existing_bid
        }
        return context

class AddVehicleView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    template_name = 'cars/add_car.html'
    form_class = CarForm 
    success_message='Vehicle Upload Successful !'  
   
    def form_valid(self,form):
            files = self.request.FILES.getlist('images')
            f = form.save(commit=False)
            f.user = self.request.user
            f.save()
            for i in files:
                CarImages.objects.create(car=f,image=i)
            return super(AddVehicleView,self).form_valid(form)


class EditVehicleView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Car
    template_name ='cars/edit_cars.html'
    form_class = CarEditForm
    success_message='Vehicle  Edit Successful !' 
    def form_valid(self,form):
            files = self.request.FILES.getlist('images')
            f = form.save(commit=False)
            # f.user = self.request.user
            f.save()
            for i in files:
                CarImages.objects.create(car=f,image=i)
            return super(EditVehicleView,self).form_valid(form)

class DeleteVehicleView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Car
    template_name ='cars/delete_vehicle.html'
    success_message='Vehicle Delete Successful !' 
    success_url =reverse_lazy('cars')


@ login_required
def AddFavouriteView(request,slug):
    car = get_object_or_404(Car,slug=slug)
    if car.favourites.filter(id=request.user.id).exists():
        car.favourites.remove(request.user)
    else:
        car.favourites.add(request.user) 
        messages.success(request,'Bookmark Successfull !' )
    return HttpResponseRedirect(request.META['HTTP_REFERER'])  

class FavouritesView(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'cars/favourites.html' 
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super(FavouritesView,self).get_context_data(**kwargs)
        favourite_cars =Car.objects.filter(favourites=self.request.user.id)
        context["favourite_cars"] = favourite_cars
        return context

class MyCarsView(LoginRequiredMixin, ListView): 
    model = Car
    template_name ='cars/my_cars.html'
    def get_context_data(self, **kwargs):
        context = super(MyCarsView,self).get_context_data(**kwargs)
        all_cars =Car.objects.select_related('user','category').filter(user = self.request.user).order_by('created_date')
        page=self.request.GET.get('page',1)
        paginator =Paginator(all_cars,10)
        try:
                all_cars=paginator.page(page)
        except PageNotAnInteger:
                all_cars=paginator.page(1)
        except EmptyPage:
              all_cars=paginator.page(paginator.num_pages) 
        sold_cars =Car.objects.select_related('user','category').filter(user =self.request.user, status='SOLD').order_by('-created_date')
        not_sold_cars =Car.objects.select_related('user','category').filter(user=self.request.user,status='NOT SOLD').order_by('-created_date')
        waiting_payments_cars =Car.objects.select_related('user','category').filter(user =self.request.user,status='WAITING PAYMENT').order_by('-created_date')
       
        context = {
            'all_cars':all_cars,'sold_cars':sold_cars,'not_sold_cars':not_sold_cars,
            'waiting_payments_cars':waiting_payments_cars
        } 
        return context


    

class CarBids(ListView):
    model = Car 
    template_name ='bids/this_car_bids.html'
    
    def get_context_data(self, **kwargs):
        context = super(CarBids,self).get_context_data(**kwargs)
        car =get_object_or_404(Car,slug=self.kwargs['slug'])
        car_bids =Bid.objects.filter(car=car)

        context  =  {
            'car_bids':car_bids, 'car':car,
        }
        return context

def approve_bid(request,slug):
    bid = get_object_or_404(Bid,slug=slug)  
    bidder_id =bid.user_id
    bidder = get_object_or_404(User,id=bidder_id) 
    
    bid.status ='WAITING PAYMENT'
    car_id=bid.car_id
    bid.accept_time=timezone.now()
    car = get_object_or_404(Car,id=car_id)
    
    car.status ='WAITING PAYMENT'
    car.save()
    bid.save()
    # message details

    bidder_user= bidder.username
    car_cat = car.category
    car_name =car.car_name

    account_sid = 'AC9287fcbe5e65979be825a87a5b835654'
    auth_token = '40e7af4e722d4d536b3952b87ee593b9'
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #                         #   body='Hello',
    #                           body= f'Hello {bidder_user}, your bid on  {car_cat} {car_name}  is approved please proceed to make payments.',
    #                           from_='+18782066029',
    #                           to='+254714900634'
    #                       )
    # print(message.sid)

    send_mail(
            'Car Bid Approved',
            f'Hello {bidder_user}, your bid on  {car_cat} {car_name}  is approved please proceed to make payments.',
            'obwakuvictor@gmail.com',
            ['obwakuvictor@yahoo.com'],
        )    
    
    if bid.save() :
        car = get_object_or_404(Car,id=car_id)
        car.status ='WAITING PAYMENT'
        car.save()
        messages.success(request,'Bid Approved')
        message = Client.messages.create(
                              body='Hi there',
                              from_='+18782066029',
                              to='+254714900634'
                          )

        print(message.sid)
    return redirect('this_car_bids',slug=car.slug)    

def cancel_approval(request,slug):
    bid = get_object_or_404(Bid,slug=slug)  
    car_id = bid.car_id
    car = get_object_or_404(Car,id=car_id)
    # bidder_id =bid.user_id
    # bidder = get_object_or_404(User,id=bidder_id)
    if bid.status == 'WAITING PAYMENT':
        car_id = bid.car_id
        car = get_object_or_404(Car,id=car_id)
        car.status='NOT SOLD'
        car.save()
        bid.status ='Cancelled'
        bid.cancel_reject_time = timezone.now()
        bid.save()
        messages.success(request,'Bid Cancelled')

    # if bid.save():
    #     car=get_object_or_404(Car,id=car_id)
    #     car.status ='NOT SOLD'
    #     car.save()
    #     messages.success(request,'Bid Cancelled')
    return redirect('this_car_bids',slug=car.slug)




def CarCategoryView(request,slug):
    category = get_object_or_404(Category,slug=slug)
    cars =Car.objects.filter(category=category)
    page=request.GET.get('page',1)
    paginator = Paginator(cars,16)
    try:
        cars =paginator.page(page)
    except PageNotAnInteger:
        cars=paginator.page(1)
    except EmptyPage:
        cars=paginator.page(paginator.num_pages)

    return render(request,'category/category.html',{'slug':slug,'cars':cars,'tags':category})

def CarUserView(request,username):
    user = get_object_or_404(User,username=username)
    cars =Car.objects.filter(user=user)
    page=request.GET.get('page',1)
    paginator = Paginator(cars,16)
    try:
        cars =paginator.page(page)
    except PageNotAnInteger:
        cars=paginator.page(1)
    except EmptyPage:
        cars=paginator.page(paginator.num_pages)

    return render(request,'users/users.html',{'username':username,'cars':cars,'user':user})



# class CarUserView(ListView):
#     model = User
#     template_name = 'users/users.html'
#     paginate_by = 16
#     def get_context_data(self, **kwargs):
#         context = super(CarUserView,self).get_context_data(**kwargs)
#         user = get_object_or_404(User,username=self.kwargs['username'])
#         cars =Car.objects.filter(user=user)
#         context ={
#             'cars':cars
#         }
#         return context