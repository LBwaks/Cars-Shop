from django.urls import path
from .import views

from .views import ProfileAddView,ProfileDetailView,EditProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_profile',ProfileAddView.as_view(), name="add_profile"),
    # path('<profile_uuid>/my_profile/',MyProfileView.as_view(), name='profile'),
    path('<slug:profile_uuid>/my-profile/',ProfileDetailView.as_view(), name='profile'),
    path('edit/<profile_uuid>', EditProfileView.as_view(), name='edit_profile'),
    # path('<profile_uuid>/update_account/', EditAccountView.as_view(), name='update_account'),
   
    
]
#