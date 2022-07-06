from audioop import reverse
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from sweetify.views import SweetifySuccessMixin
from django.utils import timezone
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
class CarsView(ListView):
    model =Car
    template_name='cars/cars.html'
    queryset = Car.objects.all().order_by('created_date')

class CarDetailView(HitCountDetailView):
    model =Car
    template_name ='cars/car_details.html'
    count_hit = True

    # def get_related_vehicles(self):
    #      return Car.objects.filter(status='PENDING',category_id=self.category_id).exclude(slug=self.slug).order_by('-created_date')[:8]

  
    def get_context_data(self, *args,**kwargs):
        context=super(CarDetailView,self).get_context_data(**kwargs)
        car = get_object_or_404(Car,slug=self.kwargs['slug'])
       
        fav =bool        
        if car.favourites.filter(id=self.request.user.id).exists():
            fav =True
       
       
        context ={
          'car':car,'fav':fav
        }
        return context

class AddVehicleView(LoginRequiredMixin,CreateView):
    template_name = 'cars/add_car.html'
    form_class = CarForm   
   
    def form_valid(self,form):
            files = self.request.FILES.getlist('images')
            f = form.save(commit=False)
            f.user = self.request.user
            f.save()
            for i in files:
                CarImages.objects.create(car=f,image=i)
            return super(AddVehicleView,self).form_valid(form)







class EditVehicleView(LoginRequiredMixin,UpdateView):
    model = Car
    template_name ='cars/edit_cars.html'
    form_class = CarEditForm
    success_message = 'Cooohjjjjhfdfcghbj'

class DeleteVehicleView(LoginRequiredMixin,DeleteView):
    model = Car
    template_name ='cars/delete_vehicle.html'
    success_url =reverse_lazy('cars')


@ login_required
def AddFavouriteView(request,slug):
    car =get_object_or_404(Car,slug=slug)
    if car.favourites.filter(id=request.user.id).exists():
        car.favourites.remove(request.user)
    else:
        car.favourites.add(request.user)  
    return HttpResponseRedirect(request.META['HTTP_REFERER'])  

class FavouritesView(LoginRequiredMixin,ListView):
    model = Car
    template_name = 'cars/favourites.html' 

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
        all_cars =Car.objects.filter(user = self.request.user).order_by('-created_date')
        page=self.request.GET.get('page',1)
        paginator =Paginator(all_cars,2)
        try:
                all_cars=paginator.page(page)
        except PageNotAnInteger:
                all_cars=paginator.page(1)
        except EmptyPage:
              all_cars=paginator.page(paginator.num_pages) 
        sold_cars =Car.objects.filter(user =self.request.user, status='SOLD').order_by('-created_date')
        not_sold_cars =Car.objects.filter(user=self.request.user,status='PENDING').order_by('-created_date')
        waiting_payments_cars =Car.objects.filter(user =self.request.user,status='WAITING PAYMENT').order_by('-created_date')
       
        context = {
            'all_cars':all_cars,'sold_cars':sold_cars,'not_sold_cars':not_sold_cars,
            'waiting_payments_cars':waiting_payments_cars
        } 
        return context


       
    

def add_vehicle_image(request):
    if request.method == 'POST':
        # form = None
        # imageform = None
        form = ImageForm(request.POST,request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            
            for i in files:
               img= CarImages.objects.create(car=5,image=i)
               img.save()
            
            return HttpResponseRedirect('/cars')   
      
    else:
        form =ImageForm()
    return render(request,'cars/add_car.html',{
        # "imageform":imageform,
        'form':form})

class AddVehicleImagesView(CreateView):  
    template_name = 'cars/car_images.html'
    form_class = ImageForm
    # success_url =' '

    def form_valid(self,form):                   
        f =form.save(commit=False)         
        f.car_id =5
        # self.kwargs['job_id']      
        f.save()        
        if  f.save():
         files = self.request.FILES.getlist('image []')  
         for i in files:
            h= CarImages.objects.create(car=f,image='hey' )
            h.save()
        #  print(i)
        return super(AddVehicleImagesView,self).form_valid(form)

    # def post(self,request, *args, **kwargs):
    #     # try:
    #         form_class= self.get_form_class()
    #         form= self.get_form(form_class)
    #         images = request.FILES.getlist('image')  
    #         # car= Car.objects.get(id)
    #         car_id=1
    #         if form.is_valid():
    #             for image in images:
    #              car_images = CarImages.objects.create(car=car_id,image=image)
    #              car_images.save()
    #             return self.form_valid(form)
    #         else:
    #             return self.form_invalid(form)
        # except Exception as e:
        #     print(e)

   
    
def add_vehicle(request):
    if request.method == 'POST':
        # form = None
        # imageform = None
        form = CarForm(request.POST,request.FILES)
        files = request.FILES.getlist('images')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                CarImages.objects.create(car=f,image=i)
            messages.success(request,"New Vehicle Added")
            return HttpResponseRedirect('/cars')   
      
    else:
        form =CarForm()
        # imageform = ImageForm()
    return render(request,'cars/add_car.html',{
        # "imageform":imageform,
        'form':form})
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
    if bid.save() :
        car = get_object_or_404(Car,id=car_id)
        car.status ='WAITING PAYMENT'
        car.save()
        messages.success(request,'Bid Approved')
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
        car.status='PENDING'
        car.save()
        bid.status ='Cancelled'
        bid.cancel_reject_time = timezone.now()
        bid.save()
        messages.success(request,'Bid Cancelled')

    # if bid.save():
    #     car=get_object_or_404(Car,id=car_id)
    #     car.status ='PENDING'
    #     car.save()
    #     messages.success(request,'Bid Cancelled')
    return redirect('this_car_bids',slug=car.slug)



    
class CarCategoryView(ListView):
    model = Category
    template_name = 'category/category.html'
    def get_context_data(self, **kwargs):
        context = super(CarCategoryView,self).get_context_data(**kwargs)
        category = get_object_or_404(Category,slug=self.kwargs['slug'])
        cars =Car.objects.filter(category=category)
        context ={
            'cars':cars
        }
        return context
class CarUserView(ListView):
    model = User
    template_name = 'category/category.html'
    def get_context_data(self, **kwargs):
        context = super(CarUserView,self).get_context_data(**kwargs)
        user = get_object_or_404(User,username=self.kwargs['username'])
        cars =Car.objects.filter(user=user)
        context ={
            'cars':cars
        }
        return context