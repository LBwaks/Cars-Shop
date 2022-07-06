from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView,DeleteView,UpdateView,CreateView,DetailView
from .models import Bid
from Cars.models import Car
from Bids.forms import BidForm,BidEditForm
from django.utils import timezone
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


class BidsView(ListView):
    model = Bid
    template_name = 'bids/my_cars.html' 

    def get_context_data(self, **kwargs):
        context = super(BidsView,self).get_context_data(**kwargs)
        car = get_object_or_404(Car,slug=self.kwargs['slug'])
        car_bid_count = Bid.objects.filter(car=car)
        context["car_bid_count"] = car_bid_count
        return context

class BidDetailView(SuccessMessageMixin,LoginRequiredMixin,DetailView):
    model = Bid 
    template_name = 'bids/bid_details.html'

    def get_context_data(self, **kwargs):
        context = super(BidDetailView,self).get_context_data(**kwargs)
        bid = get_object_or_404(Bid,slug=self.kwargs['slug'])
        context["bid"] = bid
        return context
class DeleteBidView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Bid
    template_name= 'bids/delete_bid.html'
    success_url =reverse_lazy('cars')
    success_message='Bid Deleted'

    
class AddBidView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Bid 
    form_class= BidForm
    template_name = 'bids/add_bids.html'
    success_message = 'Bid Car Successful !'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = 
    #     return context
    
    def form_valid(self,form):
        bid = form.save(commit=False)
        bid.user = self.request.user
        bid.car_id =self.kwargs['car_id']
        bid.save()
        return super(AddBidView,self).form_valid(form)
        

class EditBidView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Bid 
    template_name ='bids/edit_bid.html'
    form_class = BidEditForm
    success_message ='Bid Edit Successfull'

class MyBidsView(LoginRequiredMixin,ListView):
    model = Bid
    template_name= 'bids/my_bids.html'

    def get_context_data(self, **kwargs):
        context = super(MyBidsView,self).get_context_data(**kwargs)
        all_bids = Bid.objects.filter(user = self.request.user).order_by('-created_date')
        page=self.request.GET.get('page',1)
        paginator =Paginator(all_bids,2)
        try:
                all_bids=paginator.page(page)
        except PageNotAnInteger:
                all_bids=paginator.page(1)
        except EmptyPage:
              all_bids=paginator.page(paginator.num_pages) 
              
        accepted_bids = Bid.objects.filter(user = self.request.user,status='APPROVED').order_by('-created_date')
        pending_bids = Bid.objects.filter(user = self.request.user ,status='PENDING').order_by('-created_date')
        rejected_bids = Bid.objects.filter(user = self.request.user,status ='REJECTED').order_by('-created_date')
        waiting_payment_bids = Bid.objects.filter(user = self.request.user,status ='WAITING PAYMENT').order_by('-created_date')
        context = {
            'all_bids':all_bids,'accepted_bids':accepted_bids,'pending_bids':pending_bids,'rejected_bids':rejected_bids,'waiting_payment_bids':waiting_payment_bids
        }
        return context
    
def reject_approval(request,slug):
    bid =get_object_or_404(Bid,slug = slug)
    if bid.status == 'WAITING PAYMENT':
        car_id = bid.car_id
        car = get_object_or_404(Car,id = car_id)
        car.status = 'PENDING'
        car.save()        
    bid.status ='REJECTED'
    bid.cancel_reject_time=timezone.now()
    bid.save()
    messages.success(request,'Approval Rejected!')
    return redirect('my_bids')    