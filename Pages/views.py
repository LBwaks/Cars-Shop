from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from Cars.models import Car
from Pages.forms import CarSearchForm,ContactForm
from django .views.generic import ListView,CreateView,FormView
from django.contrib.postgres.search import SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HomeView(ListView):
    model =Car
    template_name ='pages/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
       
        recent_cars = Car.objects.filter(status='PENDING').order_by('-created_date')[:4]
        most_viewed = Car.objects.filter(status='PENDING').order_by('hit_count_generic')[:4]
       
        context["recent_cars"] = recent_cars
        context["most_viewed"] = most_viewed
       
        return context
class ContactView(SuccessMessageMixin, CreateView):
    # model =Contact 
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_message='Your message has been sent. Thank you!'

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

def find(request):
    form = CarSearchForm
    results =[]
    
    # if form.is_valid('self'):
        # form = JobSearchForm(request.GET)
    if request.method =='GET':            
            q=request.GET.get('q')           
            results = Car.objects.annotate(search=SearchVector('stock_id','car_make','vendor_county','car_name','body_type','engine_size','year_of_make','mileage','price' ,'vendor_location','vendor_address','drive','transmission'),).filter(search=q).order_by('-created_date')
            page=request.GET.get('page',1)
            paginator = Paginator(results,30)
            try:
                results =paginator.page(page)
            except PageNotAnInteger:
                results=paginator.page(1)
            except EmptyPage:
                results=paginator.page(paginator.num_pages)
            
    return render(request,'pages/search.html',{'form':form,'results':results,'q':q })

def search(request):
    form = CarSearchForm
    results =[]
    
    if request.method == 'GET':
            
            # tag= request.GET.get('tag',None)
            car_make=request.GET.get('car_make')
            # car_make = form.cleaned_data['car_make']
            
            body_type=request.GET.get('body_type')
            # body_type = form.cleaned_data['body_type']

            car_name=request.GET.get('car_name')
            # car_name = form.cleaned_data['car_name']

            year_of_make =request.GET.get('year_of_make ')
            # year_of_make  = form.cleaned_data['year_of_make ']

            location =request.GET.get('location ')
            # location  = form.cleaned_data['location ']

            results=Car.objects.all()
            
            # if tag != '0':
            #     tag=get_object_or_404(Tag,pk=tag)            
            #     results = results.filter(tag__name__icontains=tag.name).order_by('-created_date')
                
            #     if title:
            #         results = Job.objects.annotate(search=SearchVector('title'),).filter(search=title,tag__name__icontains=tag.name).order_by('-created_date')
            #     if location:
            #         results = Job.objects.annotate(search=SearchVector('county','location','address'),).filter(search=location,tag__name__icontains=tag.name).order_by('-created_date')
            # else:
            if car_make:
                results = Car.objects.annotate(search=SearchVector('car_make'),).filter(search=car_make).order_by('-created_date')
            if location:
                results = Car.objects.annotate(search=SearchVector('vendor_county','vendor_location','vendor_address'),).filter(search=location).order_by('-created_date')
            if year_of_make:
                results = Car.objects.annotate(search=SearchVector('year_of_make'),).filter(search=year_of_make).order_by('-created_date')

            if body_type:
                results = Car.objects.annotate(search=SearchVector('body_type'),).filter(search=body_type).order_by('-created_date')

            if car_name:
                results = Car.objects.annotate(search=SearchVector('car_name'),).filter(search=car_name).order_by('-created_date')
                    
            # results = Job.objects.annotate(search=SearchVector('title','county','location','address','tag'),).filter(search=q).order_by('-created_date')
            page=request.GET.get('page',1)
            paginator = Paginator(results,30)
            try:
                results =paginator.page(page)
            except PageNotAnInteger:
                results=paginator.page(1)
            except EmptyPage:
                results=paginator.page(paginator.num_pages)
            
    return render(request,'pages/search.html',{'form':form,'results':results,'car_make':car_make,
    'car_name':car_name,'body_type':body_type,'year_of_make':year_of_make,'location':location })
 