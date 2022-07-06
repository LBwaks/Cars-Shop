from django.shortcuts import render
from .forms import  ProfileForm, EditProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django .views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.
class ProfileAddView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    form_class = ProfileForm
    template_name ='profiles/add_profiles.html'
    success_message = 'Profile Successfully'

    def form_valid(self,form):        
        profile =form.save(commit=False)
        form.instance.user = self.request.user
        self.object =form.save()        
        profile.save()
       
        return super(ProfileAddView,self).form_valid(form)
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model =Profile
    template_name ='profiles/profile.html'
    slug_url_kwarg = 'profile_uuid'
    slug_field ='profile_uuid'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView,self).get_context_data(**kwargs)
        my_profile =get_object_or_404(Profile,profile_uuid=self.kwargs['profile_uuid'])
        context["my_profile"] = my_profile
        return context

class EditProfileView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=Profile
    template_name ='profiles/edit_profile.html'
    form_class = EditProfileForm
    slug_url_kwarg = "profile_uuid"
    slug_field = "profile_uuid"