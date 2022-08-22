from django.conf import settings
from django.urls import path
from .import views
from .views import  CarUserView,CarCategoryView, cancel_approval,approve_bid,CarBids,CarsView,MyCarsView,AddVehicleView,CarDetailView,DeleteVehicleView,EditVehicleView,AddFavouriteView,FavouritesView, approve_bid
from django.conf.urls.static import static
urlpatterns = [
    path('',CarsView.as_view(),name="cars"),

    path('add_car',AddVehicleView.as_view(),name="add_vehicles"),
    path('<slug>',CarDetailView.as_view(),name="vehicle_details"), 
    path('edit/<slug>',EditVehicleView.as_view(),name="edit_vehicle"), 
    path('delete/<slug>',DeleteVehicleView.as_view(),name="delete_vehicle"), 
    path('favourite/<slug>',AddFavouriteView,name="add_favourite"), 
    path('user/favourites/',FavouritesView.as_view(),name="favourites"),
    # path('<slug>',AddVehicleImagesView.as_view(),name="add_images"),   
    path('my_cars/',MyCarsView.as_view(),name="my_cars"),
    path('this_car_bids/<slug>',CarBids.as_view(),name='this_car_bids'),
    path("<slug>/approve", approve_bid, name="approve_bid"), 
    path('<slug>/cancel',cancel_approval,name="cancel_bid"),
      # path('<slug>',add_vehicle_image,name="add_imagess"),
    path('category/<slug>/',CarCategoryView,name='category'),
    path('user/<username>/',CarUserView,name='user_cars')
    
]

  
  
